"""
Indian GST Calculator - Streamlit Web Application
A clean, modern, and user-friendly GST calculator for Indian consumers and businesses
"""

import streamlit as st
import os
from database_gst_service import get_category_list, get_category_scenarios, gst_db_service
from utils import format_currency, calculate_gst, calculate_gst_breakdown, validate_amount

@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_cached_categories():
    """Get categories with caching for faster loading"""
    return get_category_list()

@st.cache_data(ttl=300)  # Cache for 5 minutes  
def get_cached_scenarios(category):
    """Get scenarios with caching for faster loading"""
    return get_category_scenarios(category)

def inject_google_analytics():
    """Google Analytics is now loaded directly in the page head"""
    pass

# Page configuration
st.set_page_config(
    page_title="Indian GST Calculator Online - Accurate Rates | GSTCalcIndia",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add meta tag for crawler-friendly rendering
st.markdown("""
<meta name="fragment" content="!">
<meta name="prerender-status-code" content="200">
""", unsafe_allow_html=True)

# Set page title using components
st.markdown("""
<script>
setTimeout(function() {
    document.title = "Indian GST Calculator Online - Accurate Rates | GSTCalcIndia";
}, 100);
</script>
""", unsafe_allow_html=True)

# Google Analytics - Enhanced loading method
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=G-561C8F8S4P"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-561C8F8S4P');
</script>
""", unsafe_allow_html=True)

# Additional Google Analytics injection using JavaScript
st.components.v1.html("""
<script async src="https://www.googletagmanager.com/gtag/js?id=G-561C8F8S4P"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-561C8F8S4P');
  
  // Send initial page view
  gtag('event', 'page_view', {
    page_title: 'Indian GST Calculator',
    page_location: window.location.href
  });
</script>
""", height=0)

# SEO Meta Tags and Schema Markup
st.markdown("""
<link rel="canonical" href="https://gstcalcindia.com/" />
<meta name="description" content="Calculate GST online for goods & services in India with GSTCalcIndia.com. Fast, accurate, and up-to-date with official CBIC rates. Mobile-friendly GST calculator.">
<meta name="keywords" content="GST calculator India, Indian GST calculator, online GST calculator, GST rates India, GST calculation, HSN code GST, SAC code GST, CBIC rates">
<meta name="author" content="GSTCalcIndia.com">
<meta name="robots" content="index, follow">
<meta name="language" content="English">
<meta name="geo.region" content="IN">
<meta name="geo.country" content="India">

<!-- Open Graph Tags for Social Media -->
<meta property="og:title" content="Indian GST Calculator Online - Accurate Rates | GSTCalcIndia">
<meta property="og:description" content="Calculate GST online for goods & services in India. Fast, accurate, and up-to-date with official CBIC rates.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://gstcalcindia.com">
<meta property="og:locale" content="en_IN">

<!-- Twitter Card Tags -->
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Indian GST Calculator Online - Accurate Rates">
<meta name="twitter:description" content="Calculate GST online for goods & services in India. Fast, accurate, and up-to-date with official CBIC rates.">

<!-- Schema.org Structured Data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Indian GST Calculator",
  "description": "Online GST calculator for goods and services in India with official CBIC rates",
  "url": "https://gstcalcindia.com",
  "applicationCategory": "FinanceApplication",
  "operatingSystem": "Web Browser",
  "inLanguage": "en-IN",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "INR"
  },
  "author": {
    "@type": "Organization",
    "name": "GSTCalcIndia.com"
  },
  "geo": {
    "@type": "Country",
    "name": "India"
  }
}
</script>

<!-- Google Analytics will be injected here when GOOGLE_ANALYTICS_ID is provided -->

<!-- Clean Light Mode Styling -->
<style>
    /* Import clean fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
    
    /* Override all default fonts with Inter */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Light theme base */
    .stApp {
        background-color: #ffffff;
        color: #1f2937;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Explicitly override Streamlit's default font references */
    body, html, div, span, h1, h2, h3, h4, h5, h6, p, a, button, input, select, textarea {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Main content styling */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        color: #1f2937;
        font-weight: 600;
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.025em;
    }
    
    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Calculator container - remove background */
    .calculator-container {
        background-color: transparent;
        border: none;
        padding: 2rem;
        margin: 1.5rem 0;
    }
    
    /* Input styling - make consistent */
    .stNumberInput > div > div > input {
        background-color: #f9fafb;
        border: 1px solid #d1d5db;
        color: #1f2937;
        border-radius: 6px;
        font-size: 1rem;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #6b7280;
        outline: none;
        box-shadow: 0 0 0 1px #6b7280;
    }
    
    /* Selectbox styling - make consistent with input */
    .stSelectbox > div > div {
        background-color: #f9fafb;
        border: 1px solid #d1d5db;
        border-radius: 6px;
    }
    
    .stSelectbox > div > div > div {
        background-color: #f9fafb;
        color: #1f2937;
    }
    
    .stSelectbox > div > div > div > div {
        background-color: #f9fafb;
        color: #1f2937;
    }
    
    /* Dropdown options */
    .stSelectbox [data-baseweb="select"] {
        background-color: #f9fafb;
        color: #1f2937;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        background-color: #f9fafb;
        border-color: #d1d5db;
        color: #1f2937;
    }
    
    /* Dropdown menu - fix white background issue */
    [data-baseweb="popover"] {
        background-color: #f9fafb;
        border: 1px solid #d1d5db;
    }
    
    [data-baseweb="menu"] {
        background-color: #f9fafb;
        border: 1px solid #d1d5db;
    }
    
    [data-baseweb="menu"] > li {
        background-color: #f9fafb;
        color: #1f2937;
    }
    
    [data-baseweb="menu"] > li:hover {
        background-color: #e5e7eb;
        color: #1f2937;
    }
    
    /* Fix selectbox text color */
    .stSelectbox div[data-baseweb="select"] span {
        color: #1f2937;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #f3f4f6;
        color: #1f2937;
        border: 1px solid #d1d5db;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: #e5e7eb;
        border-color: #9ca3af;
    }
    
    /* Table styling */
    .dataframe {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
    }
    
    /* Metrics styling */
    [data-testid="metric-container"] {
        background-color: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 1rem;
    }
    
    [data-testid="metric-container"] [data-testid="metric-value"] {
        color: #1f2937;
    }
    
    [data-testid="metric-container"] [data-testid="metric-label"] {
        color: #6b7280;
    }
    
    /* Info box styling */
    .stInfo {
        background-color: #eff6ff;
        border-left: 4px solid #3b82f6;
        color: #1f2937;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #f9fafb;
        border: 1px solid #e5e7eb;
        color: #1f2937;
    }
    
    /* Simple badges */
    .feature-badge {
        display: inline-block;
        background-color: #f3f4f6;
        color: #1f2937;
        padding: 0.25rem 0.75rem;
        border-radius: 4px;
        font-size: 0.875rem;
        font-weight: 500;
        margin: 0.25rem;
        border: 1px solid #d1d5db;
    }
    
    .success-badge {
        display: inline-block;
        background-color: #ecfdf5;
        color: #065f46;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.125rem;
        border: 1px solid #a7f3d0;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Text colors */
    h1, h2, h3, h4, h5, h6 {
        color: #1f2937;
    }
    
    p, div, span {
        color: #1f2937;
    }
    
    /* Divider */
    hr {
        border-color: #e5e7eb;
    }
    
    .disclaimer {
        background-color: #f9fafb;
        border: 1px solid #d1d5db;
        color: #1f2937;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def show_disclaimer():
    """Show disclaimer content"""
    st.markdown("### ⚠️ Important Disclaimer")
    st.write("**Last Updated:** May 25, 2025")
    
    st.write("""
    Welcome to GSTCalcIndia.com. The information and tools provided on this website, including but not limited to the GST calculator, are for general guidance and informational purposes only.
    """)
    
    st.subheader("📊 Accuracy of Information")
    st.write("""
    While we strive to provide accurate and up-to-date information and base our calculations on official notifications from the Central Board of Indirect Taxes and Customs (CBIC) and common interpretations of GST law in India, GSTCalcIndia.com makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability with respect to the website or the information, products, services, or related graphics contained on the website for any purpose.
    """)
    
    st.subheader("🔢 Estimates Only")
    st.write("""
    The GST calculations provided by our tool are estimates based on the input you provide and common scenarios. GST rates, rules, and their applicability can vary significantly based on many factors, including but not limited to:
    
    - Specific product specifications and HSN/SAC classifications
    - The exact nature of the service or goods
    - Applicable exemptions or concessions
    - Changes in state or central government regulations and notifications
    - The place of supply and other transactional details
    
    Our calculator may not account for all such specific nuances, conditions, or the most recent changes that may not yet be universally implemented or reflected in general public data.
    """)
    
    st.subheader("⚖️ Not Professional Advice")
    st.write("""
    The content on GSTCalcIndia.com is not intended to be a substitute for professional tax, legal, or financial advice. All content is for informational purposes only.
    
    Users are strongly encouraged to consult with a qualified tax professional, chartered accountant, or other appropriate financial advisor for advice tailored to their specific situation before making any financial decisions or taking any action based on the information or calculations provided by this website.
    """)
    
    st.subheader("🛡️ Limitation of Liability")
    st.write("""
    In no event will GSTCalcIndia.com, its owners, or operators be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of this website or its calculator.
    """)
    
    if st.button("← Back to Calculator"):
        st.session_state.show_page = "calculator"
        st.rerun()

def show_privacy_policy():
    """Show privacy policy content"""
    st.markdown("### 🔒 Privacy Policy")
    st.write("**Last Updated:** May 25, 2025")
    
    st.write("""
    **GSTCalcIndia.com Privacy Policy**
    
    **Information We Collect:**
    - We use Google Analytics to understand how visitors use our calculator
    - No personal information is collected or stored
    - No registration or login is required
    
    **How We Use Information:**
    - Analytics data helps us improve the calculator
    - We do not sell or share any data with third parties
    - All usage data is anonymized
    
    **Cookies:**
    - We use Google Analytics cookies to track website usage
    - You can disable cookies in your browser settings
    
    **Data Security:**
    - All calculations are performed locally in your browser
    - We do not store your calculation data
    - No sensitive information is transmitted or stored
    
    **Contact Us:**
    - For privacy questions, please contact us through our website
    
    **Changes to Policy:**
    - We may update this policy occasionally
    - Changes will be posted on this page
    """)
    
    if st.button("← Back to Calculator"):
        st.session_state.show_page = "calculator"
        st.rerun()

def main():
    """Main application function"""
    
    # Inject Google Analytics if tracking ID is available
    inject_google_analytics()
    
    # Initialize session state
    if 'show_page' not in st.session_state:
        st.session_state.show_page = "calculator"
    
    # Show disclaimer page if requested
    if st.session_state.show_page == "disclaimer":
        show_disclaimer()
        return
    
    # Show privacy policy page if requested
    if st.session_state.show_page == "privacy":
        show_privacy_policy()
        return
    
    # Clear Professional Header
    st.markdown("""
    <div style="background-color: #f8fafc; border-bottom: 2px solid #e2e8f0; padding: 2rem 0; margin-bottom: 2rem; text-align: center;">
        <h1 style="font-size: 2.5rem; font-weight: 700; color: #1e40af; margin-bottom: 0.5rem; text-shadow: 0 1px 2px rgba(0,0,0,0.05);">
            🧮 Indian GST Calculator
        </h1>
        <p style="font-size: 1.2rem; color: #475569; margin-bottom: 1rem; font-weight: 500;">
            Calculate GST accurately with official government rates
        </p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
            <span style="background: #dbeafe; color: #1e40af; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">
                ✅ Official CBIC Data
            </span>
            <span style="background: #dcfce7; color: #166534; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">
                🏷️ 30+ Categories
            </span>
            <span style="background: #fef3c7; color: #92400e; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">
                📊 100+ HSN/SAC Codes
            </span>
            <span style="background: #fce7f3; color: #be185d; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">
                🚀 Lightning Fast
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'calculated' not in st.session_state:
        st.session_state.calculated = False
    if 'results' not in st.session_state:
        st.session_state.results = None
    
    # Calculator section
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.subheader("💰 Calculate Your GST")
            
            # Amount input
            amount_input = st.text_input(
                "Enter Amount (₹)",
                placeholder="e.g., 50000",
                help="Enter the base amount for GST calculation"
            )
            
            # Category selection
            categories = get_cached_categories()
            selected_category = st.selectbox(
                "Select Product/Service Category",
                options=["Select a Category..."] + categories,
                help="Choose the category that best matches your product or service"
            )
            
            # Calculate button
            calculate_btn = st.button("🔢 Calculate GST", type="primary", use_container_width=True)
            
            # Process calculation
            if calculate_btn:
                # Check if amount is entered
                if not amount_input:
                    st.error("⚠️ Please enter a valid amount to calculate GST")
                elif selected_category == "Select a Category...":
                    st.error("⚠️ Please select a product/service category")
                else:
                    amount, error = validate_amount(amount_input)
                    
                    if error:
                        st.error(f"❌ {error}")
                    else:
                        # Store results in session state
                        st.session_state.calculated = True
                        st.session_state.results = {
                            'amount': amount,
                            'category': selected_category,
                            'scenarios': get_cached_scenarios(selected_category)
                        }
                        st.rerun()
        

    
    # Results section
    if st.session_state.calculated and st.session_state.results:
        display_results(st.session_state.results)
    
    # Information sections
    display_info_sections()

def display_results(results):
    """Display GST calculation results in tabular format"""
    
    st.markdown("---")
    st.subheader(f"📊 GST Calculation Results")
    
    # Input summary
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info(f"**Amount:** {format_currency(results['amount'])} | **Category:** {results['category']}")
    
    # Scenarios
    scenarios = results['scenarios']
    
    if not scenarios:
        st.warning("No GST scenarios available for this category.")
        return
    
    # Prepare data for the table
    table_data = []
    for scenario in scenarios:
        # Calculate GST
        gst_calc = calculate_gst(results['amount'], scenario['gst_rate'])
        breakdown = calculate_gst_breakdown(results['amount'], scenario['breakdown'])
        
        # Get HSN/SAC code if available
        hsn_sac_code = scenario.get('hsn_code') or scenario.get('sac_code') or 'N/A'
        
        # Build row data with HSN/SAC code
        row = {
            "Item/Service": scenario["name"],
            "HSN/SAC Code": hsn_sac_code,
            "GST Rate": f"{scenario['gst_rate']}%",
            "Base Amount": format_currency(gst_calc["base_amount"]),
            "CGST": f"{breakdown['cgst_rate']}% = {format_currency(breakdown['cgst_amount'])}",
            "SGST": f"{breakdown['sgst_rate']}% = {format_currency(breakdown['sgst_amount'])}",
            "Total GST": format_currency(gst_calc["gst_amount"]),
            "Final Amount": format_currency(gst_calc["total_amount"])
        }
        table_data.append(row)
    
    # Display as table
    import pandas as pd
    df = pd.DataFrame(table_data)
    
    # Style the dataframe for better readability
    st.markdown("### 📋 Complete GST Breakdown")
    
    # Display the table with custom styling
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Item/Service": st.column_config.TextColumn("Item/Service", width="large"),
            "HSN/SAC Code": st.column_config.TextColumn("HSN/SAC Code", width="small"),
            "GST Rate": st.column_config.TextColumn("GST Rate", width="small"),
            "Base Amount": st.column_config.TextColumn("Base Amount", width="medium"),
            "CGST": st.column_config.TextColumn("CGST", width="medium"),
            "SGST": st.column_config.TextColumn("SGST", width="medium"),
            "Total GST": st.column_config.TextColumn("Total GST", width="medium"),
            "Final Amount": st.column_config.TextColumn("Final Amount", width="medium")
        }
    )
    
    # Summary card below the table
    st.markdown("### 💡 Key Information")
    
    # Create summary metrics
    total_scenarios = len(scenarios)
    min_gst = min(scenario['gst_rate'] for scenario in scenarios)
    max_gst = max(scenario['gst_rate'] for scenario in scenarios)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        # Better terminology based on feedback
        if total_scenarios == 1:
            st.metric("Items Calculated", total_scenarios)
        elif min_gst == max_gst:
            st.metric("Items Calculated", total_scenarios)
        else:
            st.metric("Rate Variations Found", total_scenarios)
    
    with col2:
        st.metric("Lowest GST Rate", f"{min_gst}%")
    
    with col3:
        st.metric("Highest GST Rate", f"{max_gst}%")
    
    with col4:
        st.metric("✅ Official CBIC Data", "Verified")
    
    # Additional notes
    st.info("💡 **Note:** Rates are sourced from official CBIC notifications. GST rules can be complex and vary. Please ensure the chosen scenario accurately reflects your specific item/service, and always verify with official GST documents or a tax professional before making financial decisions.")
    
    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Start New Calculation", use_container_width=True):
            st.session_state.calculated = False
            st.session_state.results = None
            st.rerun()

def display_info_sections():
    """Display informational sections"""
    
    st.markdown("---")
    
    # About section with enhanced styling
    with st.expander("ℹ️ About This Calculator"):
        st.markdown("""
        This GST calculator helps Indian consumers and small business owners quickly estimate 
        GST amounts for common products and services using **official CBIC notification data**.
        
        While we strive for accuracy with official data, this tool provides estimates for guidance and informational purposes only. Users are strongly encouraged to verify all calculations and consult official CBIC resources or a tax professional for decisions.
        
        **Key Features:**
        
        <span class="success-badge">✅ Official GST rates</span> from CBIC notifications  
        <span class="success-badge">📦 HSN codes</span> for goods with authentic rates  
        <span class="success-badge">🏪 SAC codes</span> for services with authentic rates  
        <span class="success-badge">🏷️ CGST and SGST breakdown</span> as per government structure  
        <span class="success-badge">📱 Mobile-friendly design</span>  
        <span class="success-badge">🇮🇳 Designed for Indian GST common transactions</span>
        
        **Data Sources:**
        Our data is sourced from official CBIC notifications, including foundational ones like No. 1/2017-Central Tax (Rate) and No. 11/2017-Central Tax (Rate), and is regularly updated with subsequent amendments and current HSN/SAC classifications. Last Data Review: May 2025
        """, unsafe_allow_html=True)
    
    # How it works
    with st.expander("🔧 How It Works"):
        st.write("""
        1. **Enter Amount**: Input the base amount in Indian Rupees (₹)
        2. **Select Category**: Choose from popular product/service categories
        3. **View Results**: See GST calculations for different scenarios in your selected category - always cross-verify these estimations with official sources for your specific needs
        4. **Understand Breakdown**: Review CGST and SGST components. Remember, these are estimates based on common interpretations
        5. **Start Fresh**: Use "Start New Calculation" for additional calculations
        """)
    
    # Disclaimer
    st.markdown("**⚠️ Important Disclaimer**")
    st.write("""
    This calculator provides estimated GST calculations based on current rates and common scenarios. 
    GST rates and rules may vary based on specific product specifications, state regulations, and 
    other factors. Always consult with a qualified tax professional or refer to official GST 
    documentation for accurate tax calculations for your specific situation.
    """)
    
    # Calculator coverage section
    with st.expander("📊 Our Calculator's Current Coverage"):
        try:
            stats = gst_db_service.get_database_stats()
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("HSN Codes for Goods Supported", f"70+")
            with col2:
                st.metric("SAC Codes for Services Supported", f"25+")
            with col3:
                st.metric("Available Product/Service Categories", f"30+")
                
            if stats.get('last_updated'):
                st.write(f"**Content & Tax Rates Last Reviewed:** {stats['last_updated'].strftime('%B %Y')}")
            
            st.write("**Tax rate information is sourced from official CBIC notifications.**")
        except Exception as e:
            st.write("Coverage statistics temporarily unavailable.")
    
    st.markdown("---") # Separator before footer content begins

    # Footer content starts here
    footer_container = st.container()
    with footer_container:
        # Navigation for Disclaimer and Privacy Policy
        col1, col2, col3 = st.columns([1,1,3]) # Adjust column ratios as needed
        with col1:
            if st.button("Disclaimer", key="footer_disclaimer_btn", help="View our Disclaimer"):
                st.session_state.show_page = "disclaimer" # Assuming 'disclaimer' shows your disclaimer content
                st.rerun()
        with col2:
            if st.button("Privacy Policy", key="footer_privacy_btn", help="View our Privacy Policy"):
                # You'll need a function like show_privacy_policy() and set show_page accordingly
                st.session_state.show_page = "privacy" # Assuming 'privacy' shows your privacy policy
                st.rerun()
        # col3 can be empty or used for other links if needed

        # Copyright and additional info
        st.markdown("""
        <div style="text-align: center; padding-top: 20px; margin-top: 20px; border-top: 1px solid #e2e8f0;">
            <p style="color: #6b7280; font-size: 0.875rem; margin: 0;">
                © {current_year} GSTCalcIndia.com - All rights reserved
            </p>
            <p style="color: #9ca3af; font-size: 0.75rem; margin: 0.5rem 0 0 0;">
                For educational and estimation purposes only. Consult tax professionals for official calculations.
            </p>
        </div>
        """.format(current_year=2025), unsafe_allow_html=True)
    
    # Final title override to ensure it changes from Streamlit default
    st.markdown("""
    <script>
    // Override Streamlit's default title
    document.addEventListener('DOMContentLoaded', function() {
        document.title = "Indian GST Calculator Online - Accurate Rates | GSTCalcIndia";
    });
    // Also try immediate change
    document.title = "Indian GST Calculator Online - Accurate Rates | GSTCalcIndia";
    </script>
    """, unsafe_allow_html=True)
    


if __name__ == "__main__":
    main()
