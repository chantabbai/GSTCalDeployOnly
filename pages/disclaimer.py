"""
⚠️ Disclaimer
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Disclaimer - GSTCalcIndia.com",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Set page title using JavaScript.
st.markdown("""
<script>
setTimeout(function() {
    document.title = "Disclaimer - GSTCalcIndia.com";
}, 100);
</script>
""", unsafe_allow_html=True)

# Google Analytics
st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-561C8F8S4P"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-561C8F8S4P');
</script>
""", unsafe_allow_html=True)

# Styling
st.markdown("""
<style>
    /* Import clean fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
    
    /* Light theme base */
    .stApp {
        background-color: #ffffff;
        color: #1f2937;
        font-family: 'Inter', sans-serif;
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
</style>
""", unsafe_allow_html=True)

# Header with back link
st.markdown("""
<div style="background-color: #f8fafc; border-bottom: 2px solid #e2e8f0; padding: 1.5rem 0; margin-bottom: 2rem;">
    <div style="max-width: 800px; margin: 0 auto; padding: 0 1rem;">
        <a href="/" style="color: #3b82f6; text-decoration: none; font-weight: 500;">
            ← Back to GST Calculator
        </a>
        <h1 style="font-size: 2rem; font-weight: 700; color: #1e40af; margin: 1rem 0 0.5rem 0;">
            ⚠️ Important Disclaimer
        </h1>
        <p style="color: #6b7280; margin: 0;">GSTCalcIndia.com - Legal Information</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content
st.markdown("""
<div style="max-width: 800px; margin: 0 auto; padding: 0 1rem; line-height: 1.6;">
""", unsafe_allow_html=True)

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

Users are strongly encouraged to consult with a qualified tax professional, chartered accountant, or other appropriate financial advisor for advice tailored to their specific situation before making any financial decisions or taking any action based on the information or calculations provided by this website. Users should also refer to the official GST laws, rules, circulars, and notifications issued by the Government of India and the GST Council for definitive guidance.
""")

st.subheader("🛡️ Limitation of Liability")
st.write("""
In no event will GSTCalcIndia.com, its owners, or operators be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of this website or its calculator.
""")

st.subheader("🔗 External Links")
st.write("""
From time to time, this website may include links to other websites. These links are provided for your convenience to provide further information. They do not signify that we endorse the website(s). We have no responsibility for the content of the linked website(s).
""")

st.subheader("📝 Changes to Disclaimer")
st.write("""
We reserve the right to make changes to this Disclaimer at any time. Any such modifications will be effective immediately upon posting on the website. Your continued use of the website after any changes have been made constitutes your acceptance of the new Disclaimer.
""")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem 0; background-color: #f8fafc; margin-top: 3rem; border-top: 1px solid #e2e8f0;">
    <div style="margin-bottom: 1rem;">
        <a href="/" style="color: #3b82f6; text-decoration: none; margin: 0 1rem; font-weight: 500;">GST Calculator</a> |
        <a href="/privacy-policy" style="color: #3b82f6; text-decoration: none; margin: 0 1rem; font-weight: 500;">Privacy Policy</a>
    </div>
    <p style="color: #6b7280; font-size: 0.875rem; margin: 0;">
        © 2025 GSTCalcIndia.com - All rights reserved
    </p>
</div>
""", unsafe_allow_html=True)