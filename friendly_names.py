"""
User-friendly scenario name conversions
Convert technical GST scenario names to everyday language
"""

def create_friendly_name(technical_name: str) -> str:
    """Convert technical scenario names to user-friendly names"""
    
    # Direct replacements for common scenarios
    friendly_replacements = {
        # Vehicle scenarios
        "Passenger Cars - Petrol (Engine ≤1200cc)": "Small Petrol Car (up to 1200cc)",
        "Passenger Cars - Petrol (Engine >1200cc)": "Large Petrol Car (above 1200cc)",
        "Passenger Cars - Diesel (Engine ≤1500cc)": "Small Diesel Car (up to 1500cc)",
        "Passenger Cars - Diesel (Engine >1500cc)": "Large Diesel Car (above 1500cc)",
        "SUVs (Length >4m, Engine >1500cc, Ground clearance ≥170mm)": "SUV or Large Vehicle",
        "Electric Vehicles (All types)": "Electric Car",
        "Motorcycles (Engine ≤150cc)": "Small Motorcycle/Scooter",
        "Motorcycles (Engine >150cc ≤350cc)": "Medium Motorcycle",
        "Motorcycles (Engine >350cc)": "Large Motorcycle",
        
        # Hotel scenarios
        "Luxury Hotels (Above ₹7,500/night)": "Luxury Hotel Stay",
        "Premium Hotels (₹2,500-7,500/night)": "Premium Hotel Stay", 
        "Standard Hotels (₹1,000-2,500/night)": "Standard Hotel Stay",
        
        # Restaurant scenarios
        "Non-AC Restaurants": "Regular Restaurant",
        "AC Restaurants": "Air-Conditioned Restaurant",
        "Small Restaurants, Dhaba, Mess": "Small Restaurant/Dhaba",
        
        # Property scenarios
        "Renting Residential Property": "House/Apartment Rent",
        "Renting Commercial Property": "Office/Shop Rent",
        "Under-construction Property Sale": "New Property Purchase",
        "Real Estate Brokerage": "Property Agent Service",
        
        # Electronics
        "Air Conditioning Machines": "Air Conditioner",
        "Computers, Laptops": "Computer/Laptop",
        "Telephone Sets, Smartphones": "Mobile Phone/Smartphone",
        
        # Food items
        "Soft Drinks, Fruit Juices": "Soft Drinks & Juices",
        "Food Preparations": "Processed Foods",
        
        # Textiles
        "T-shirts, Singlets, Tank Tops": "T-shirts & Casual Tops",
        "Mens Suits, Jackets, Trousers": "Men's Formal Wear",
        "Womens Suits, Jackets, Dresses": "Women's Formal Wear",
        "Mens Shirts": "Men's Shirts",
        "Womens Blouses, Shirts": "Women's Shirts & Blouses",
        
        # Footwear
        "Sports Footwear": "Sports Shoes",
        "Leather Footwear": "Leather Shoes",
        "Textile Footwear": "Canvas/Fabric Shoes",
        
        # Home items
        "Living Room Furniture": "Sofa & Living Room",
        "Bedroom Furniture": "Bed & Mattress",
        "Kitchen Plastic": "Plastic Kitchen Items",
        "Storage Items": "Storage Containers",
        "Ceramic Dishes": "Plates & Bowls",
        "Knives & Cutlery": "Kitchen Knives",
        "Spoons & Forks": "Spoons & Forks",
        
        # Services
        "Basic Banking": "Bank Account Services",
        "Credit Card Services": "Credit Card",
        "Investment Services": "Investment & Mutual Funds",
        "Life Insurance": "Life Insurance Policy",
        "General Insurance": "Car/Health Insurance",
        "Mobile Services": "Mobile Phone Bill",
        "Internet Services": "Internet Connection",
        "TV & Entertainment": "Cable/DTH TV",
        
        # Transportation
        "Taxi, Cab, Auto Rickshaw": "Taxi/Auto/Cab Ride",
        "Bus Transportation": "Bus Travel",
        
        # Other common items
        "Tissue Paper": "Toilet Paper & Tissues",
        "Paper Plates": "Paper Plates & Cups",
        "Soaps & Detergents": "Soap & Cleaning",
        "House Paints": "Paint for Home",
        "Car Tyres": "Car Tyres",
        "String Instruments": "Guitar/Violin",
        "Keyboards": "Piano/Keyboard"
    }
    
    # Check if we have a direct friendly replacement
    if technical_name in friendly_replacements:
        return friendly_replacements[technical_name]
    
    # If no direct match, clean up the name
    friendly_name = technical_name
    
    # Remove technical terms and make more readable
    replacements = [
        (" - reduced to ", " "),
        (" - maintained at ", " "),
        (" (exempt)", " (No GST)"),
        (" services", ""),
        (" Products", ""),
        (" Items", ""),
        (" Articles", "")
    ]
    
    for old, new in replacements:
        friendly_name = friendly_name.replace(old, new)
    
    return friendly_name.strip()