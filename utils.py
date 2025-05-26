"""
Utility functions for GST calculations and formatting
"""

def format_currency(amount):
    """Format amount in Indian currency format"""
    if amount == 0:
        return "₹0"
    
    # Convert to string and handle decimal places
    amount_str = f"{amount:,.2f}"
    
    # Add rupee symbol
    return f"₹{amount_str}"

def calculate_gst(base_amount, gst_rate):
    """Calculate GST amount and total"""
    gst_amount = (base_amount * gst_rate) / 100
    total_amount = base_amount + gst_amount
    
    return {
        "base_amount": base_amount,
        "gst_rate": gst_rate,
        "gst_amount": gst_amount,
        "total_amount": total_amount
    }

def calculate_gst_breakdown(base_amount, breakdown):
    """Calculate CGST and SGST breakdown"""
    cgst_amount = (base_amount * breakdown["CGST"]) / 100
    sgst_amount = (base_amount * breakdown["SGST"]) / 100
    
    return {
        "cgst_rate": breakdown["CGST"],
        "sgst_rate": breakdown["SGST"],
        "cgst_amount": cgst_amount,
        "sgst_amount": sgst_amount,
        "total_gst": cgst_amount + sgst_amount
    }

def validate_amount(amount_str):
    """Validate and convert amount string to float"""
    try:
        amount = float(amount_str.replace(",", "").replace("₹", ""))
        if amount <= 0:
            return None, "Amount must be greater than zero"
        if amount > 10000000:  # 1 crore limit
            return None, "Amount cannot exceed ₹1,00,00,000"
        return amount, None
    except ValueError:
        return None, "Please enter a valid amount"
