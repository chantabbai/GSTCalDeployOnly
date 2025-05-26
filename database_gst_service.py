"""
Database-driven GST service that fetches official rates from PostgreSQL
"""

import psycopg2
import os
from typing import List, Dict, Optional
from friendly_names import create_friendly_name

class DatabaseGSTService:
    def __init__(self):
        self.connection_string = os.getenv('DATABASE_URL')
        self._fallback_data = None
        self._cached_categories = None  # Add caching
    
    def get_connection(self):
        """Get database connection with proper SSL configuration for DigitalOcean"""
        try:
            # Enhanced SSL configuration for cloud deployment
            if self.connection_string:
                # Parse connection string and add SSL settings
                import urllib.parse
                
                # For DigitalOcean deployment, use specific SSL settings
                ssl_params = {
                    'sslmode': 'require',
                    'sslcert': None,
                    'sslkey': None,
                    'sslrootcert': None,
                    'connect_timeout': 30
                }
                
                return psycopg2.connect(self.connection_string, **ssl_params)
            else:
                # Fallback connection parameters with SSL
                return psycopg2.connect(
                    host=os.getenv('PGHOST', 'localhost'),
                    port=os.getenv('PGPORT', '5432'),
                    user=os.getenv('PGUSER'),
                    password=os.getenv('PGPASSWORD'),
                    database=os.getenv('PGDATABASE'),
                    sslmode='require',
                    connect_timeout=30
                )
        except Exception as e:
            print(f"Database connection failed: {e}")
            raise
    
    def get_categories_with_scenarios(self) -> Dict[str, List[Dict]]:
        """Get all product categories and their scenarios from database with optimized single query"""
        # Always fetch fresh data - no caching for accurate rates
        self._cached_categories = None
            
        try:
            conn = self.get_connection()
            cur = conn.cursor()
        except Exception as e:
            print(f"Database connection error: {e}")
            return {}
        
        try:
            categories = {}
            
            # Single optimized query with JOINs to get all data at once
            cur.execute("""
                SELECT 
                    pc.category_name,
                    pc.subcategory_name,
                    pc.hsn_code,
                    pc.sac_code,
                    COALESCE(g.cgst_rate, s.cgst_rate) as cgst_rate,
                    COALESCE(g.sgst_rate, s.sgst_rate) as sgst_rate,
                    COALESCE(g.igst_rate, s.igst_rate) as igst_rate,
                    COALESCE(g.description, s.description) as description
                FROM product_categories pc
                LEFT JOIN LATERAL (
                    SELECT cgst_rate, sgst_rate, igst_rate, description
                    FROM gst_goods_rates 
                    WHERE hsn_code = pc.hsn_code AND is_active = TRUE
                    ORDER BY effective_from DESC 
                    LIMIT 1
                ) g ON pc.hsn_code IS NOT NULL
                LEFT JOIN LATERAL (
                    SELECT cgst_rate, sgst_rate, igst_rate, description
                    FROM gst_services_rates 
                    WHERE sac_code = pc.sac_code AND is_active = TRUE
                    ORDER BY effective_from DESC 
                    LIMIT 1
                ) s ON pc.sac_code IS NOT NULL
                WHERE (g.cgst_rate IS NOT NULL OR s.cgst_rate IS NOT NULL)
                ORDER BY pc.category_name, pc.subcategory_name
            """)
            
            results = cur.fetchall()
            
            # Group results by category
            for row in results:
                category_name, subcat_name, hsn_code, sac_code, cgst_rate, sgst_rate, igst_rate, description = row
                
                if category_name not in categories:
                    categories[category_name] = {"scenarios": []}
                
                # Create user-friendly scenario names
                friendly_name = create_friendly_name(subcat_name)
                
                scenario = {
                    "name": friendly_name,
                    "description": description[:100] + "..." if description and len(description) > 100 else description or "",
                    "gst_rate": float(igst_rate) if igst_rate else 0.0,
                    "breakdown": {
                        "CGST": float(cgst_rate) if cgst_rate else 0.0,
                        "SGST": float(sgst_rate) if sgst_rate else 0.0
                    },
                    "hsn_code": hsn_code,
                    "sac_code": sac_code,
                    "official_source": True
                }
                
                categories[category_name]["scenarios"].append(scenario)
            
            # Cache the results for faster subsequent access
            self._cached_categories = categories
            return categories
            
        except Exception as e:
            print(f"Error fetching categories: {e}")
            return {}
        finally:
            cur.close()
            conn.close()
    
    def search_gst_by_hsn(self, hsn_code: str) -> Optional[Dict]:
        """Search GST rate by HSN code"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            cur.execute("""
                SELECT hsn_code, description, cgst_rate, sgst_rate, igst_rate, compensation_cess
                FROM gst_goods_rates 
                WHERE hsn_code = %s
            """, (hsn_code,))
            
            result = cur.fetchone()
            if result:
                return {
                    "hsn_code": result[0],
                    "description": result[1],
                    "cgst_rate": float(result[2]),
                    "sgst_rate": float(result[3]),
                    "igst_rate": float(result[4]),
                    "compensation_cess": float(result[5]),
                    "type": "goods"
                }
            return None
            
        except Exception as e:
            print(f"Error searching HSN: {e}")
            return None
        finally:
            cur.close()
            conn.close()
    
    def search_gst_by_sac(self, sac_code: str) -> Optional[Dict]:
        """Search GST rate by SAC code"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            cur.execute("""
                SELECT sac_code, description, cgst_rate, sgst_rate, igst_rate
                FROM gst_services_rates 
                WHERE sac_code = %s
            """, (sac_code,))
            
            result = cur.fetchone()
            if result:
                return {
                    "sac_code": result[0],
                    "description": result[1],
                    "cgst_rate": float(result[2]),
                    "sgst_rate": float(result[3]),
                    "igst_rate": float(result[4]),
                    "type": "services"
                }
            return None
            
        except Exception as e:
            print(f"Error searching SAC: {e}")
            return None
        finally:
            cur.close()
            conn.close()
    
    def get_database_stats(self) -> Dict:
        """Get database statistics"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            stats = {}
            
            # Count unique HSN codes
            cur.execute("SELECT COUNT(DISTINCT hsn_code) FROM gst_goods_rates WHERE hsn_code IS NOT NULL")
            stats['goods_count'] = cur.fetchone()[0]
            
            # Count unique SAC codes
            cur.execute("SELECT COUNT(DISTINCT sac_code) FROM gst_services_rates WHERE sac_code IS NOT NULL")
            stats['services_count'] = cur.fetchone()[0]
            
            # Count categories
            cur.execute("SELECT COUNT(DISTINCT category_name) FROM product_categories")
            stats['categories_count'] = cur.fetchone()[0]
            
            # Last update
            cur.execute("SELECT MAX(last_updated) FROM gst_goods_rates")
            last_goods_update = cur.fetchone()[0]
            
            cur.execute("SELECT MAX(last_updated) FROM gst_services_rates")
            last_services_update = cur.fetchone()[0]
            
            stats['last_updated'] = max(last_goods_update, last_services_update) if last_goods_update and last_services_update else None
            
            return stats
            
        except Exception as e:
            print(f"Error getting stats: {e}")
            return {}
        finally:
            cur.close()
            conn.close()

# Global instance
gst_db_service = DatabaseGSTService()

def get_category_list():
    """Return list of available categories from database"""
    categories = gst_db_service.get_categories_with_scenarios()
    return list(categories.keys())

def get_category_scenarios(category):
    """Get scenarios for a specific category from database"""
    categories = gst_db_service.get_categories_with_scenarios()
    return categories.get(category, {}).get("scenarios", [])
