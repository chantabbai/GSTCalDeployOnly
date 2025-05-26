import streamlit as st

st.set_page_config(
    page_title="Privacy Policy - Indian GST Calculator",
    page_icon="🔒", 
    layout="wide"
)

st.title("🔒 Privacy Policy")

st.markdown("""
## Privacy Policy - GSTCalcIndia.com

**Effective Date**: May 2024  
**Last Updated**: May 2024

### Introduction
This Privacy Policy describes how GSTCalcIndia.com ("we", "our", or "us") collects, uses, and protects information when you use our GST calculator service. We are committed to protecting your privacy and ensuring transparency about our data practices.

### Information We Collect

#### Information We DO NOT Collect
- **Personal Identification**: We do not collect names, email addresses, phone numbers, or any personal identification information
- **Calculation Data**: We do not store, save, or retain any amounts, GST calculations, or transaction details you enter
- **Account Information**: We do not require user accounts, registrations, or login credentials
- **Payment Information**: We do not process payments or collect financial information

#### Information We MAY Collect
- **Anonymous Usage Analytics**: We may use Google Analytics to collect anonymous information about:
  - Pages visited and time spent on the site
  - Browser type and device information (anonymized)
  - General geographic location (country/region level only)
  - User interactions with calculator features (anonymized)

#### Technical Information
- **Server Logs**: Our hosting service may automatically collect standard server log information including:
  - IP addresses (not linked to personal identity)
  - Browser type and version
  - Referring websites
  - Date and time of access

### How We Use Information

#### Analytics and Improvement
- **Service Enhancement**: Anonymous usage data helps us understand how users interact with the calculator to improve functionality
- **Performance Optimization**: Technical data helps us optimize loading speeds and fix technical issues
- **Feature Development**: Usage patterns help us prioritize new features and improvements

#### We DO NOT Use Information For
- **Marketing**: We do not send promotional emails or marketing communications
- **Selling Data**: We do not sell, rent, or share any user information with third parties
- **Profiling**: We do not create user profiles or track individual behavior
- **Advertising**: We do not use collected data for targeted advertising

### Data Storage and Security

#### Local Processing
- **Client-Side Calculations**: All GST calculations are performed in your browser
- **No Server Storage**: Calculation inputs and results are not transmitted to or stored on our servers
- **Temporary Session**: Data exists only during your browser session and is cleared when you close the page

#### Database Security
- **Official Rates Only**: Our database contains only official GST rates from CBIC notifications
- **No User Data**: Our database does not contain any user-entered information
- **Secure Infrastructure**: Database is hosted on secure, encrypted infrastructure

### Third-Party Services

#### Google Analytics
- **Purpose**: Anonymous website usage analytics
- **Data Collected**: Anonymized usage patterns, page views, session duration
- **Privacy Controls**: Users can opt-out using browser settings or ad blockers
- **Google's Policy**: Subject to Google's Privacy Policy

#### Hosting Services
- **Infrastructure**: Website hosted on secure cloud infrastructure
- **Data Handling**: Hosting provider may have access to standard server logs
- **Security**: Industry-standard security measures and encryption

### Your Rights and Choices

#### Data Control
- **No Account Deletion Needed**: Since we don't store personal data, there's nothing to delete
- **Browser Controls**: You can clear browser cache and cookies at any time
- **Analytics Opt-out**: You can disable analytics using browser settings or ad blockers

#### Access and Correction
- **No Personal Data**: Since we don't collect personal information, there's no personal data to access or correct
- **Rate Accuracy**: If you notice incorrect GST rates, please contact us for verification

### Children's Privacy
- **Age Restrictions**: Our service is not specifically directed at children under 13
- **No Collection**: We do not knowingly collect information from children
- **Parental Guidance**: Parents should supervise children's internet usage

### International Users
- **Indian Focus**: This calculator is designed for Indian GST calculations
- **Global Access**: International users can access the tool but should note it's specific to Indian tax regulations
- **Data Location**: Data processing occurs on servers that may be located outside your country

### Changes to This Policy
- **Updates**: We may update this privacy policy to reflect changes in our practices or legal requirements
- **Notification**: Material changes will be posted on this page with an updated effective date
- **Continued Use**: Continued use of the calculator after changes constitutes acceptance of the updated policy

### Legal Basis for Processing
- **Legitimate Interest**: We process anonymous usage data based on our legitimate interest in improving the service
- **Consent**: By using the calculator, you consent to the data practices described in this policy
- **Compliance**: We comply with applicable data protection laws

### Data Retention
- **No Personal Data Retention**: Since we don't collect personal data, there's no retention period
- **Analytics Data**: Anonymous analytics data may be retained according to Google Analytics retention settings
- **Server Logs**: Standard server logs may be retained for security and technical purposes for limited periods

### Contact Information
If you have questions about this Privacy Policy or our data practices, please contact us through our website contact form.

### Compliance and Jurisdiction
- **Indian Law**: This privacy policy is governed by Indian data protection laws
- **Jurisdiction**: Any disputes related to privacy will be subject to Indian jurisdiction
- **Regulatory Compliance**: We comply with applicable Indian privacy and data protection regulations

---

**Acknowledgment**: By using our GST calculator, you acknowledge that you have read and understood this Privacy Policy and agree to our data practices as described herein.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem 0; color: #666;">
    <p><a href="/" style="color: #1f77b4; text-decoration: none;">← Back to GST Calculator</a></p>
</div>
""", unsafe_allow_html=True)