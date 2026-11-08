def calculate_vat(amount, rate=0.16):
    """Return the VAT portion of an amount(Kenya standard VAT = 16%),"""
    return round(amount * rate,2)
print(calculate_vat(2000))
print(calculate_vat(3600, 0.09))