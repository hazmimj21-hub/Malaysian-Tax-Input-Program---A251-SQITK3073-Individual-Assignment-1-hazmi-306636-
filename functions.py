import pandas as pd

def verify_user(ic_number, password):
    """
    Verify user credentials.
    Returns True if IC is 12 digits and password matches last 4 digits of IC, else False.
    """
    if len(ic_number) != 12 or not ic_number.isdigit():
        return False
    return password == ic_number[-4:]

def calculate_tax(income, tax_relief):
    """
    Calculate tax based on Malaysian tax rates for 2024.
    Returns the calculated tax amount.
    """
    chargeable_income = max(0, income - tax_relief)
    
    if chargeable_income <= 5000:
        return 0
    elif chargeable_income <= 20000:
        return chargeable_income * 0.01
    elif chargeable_income <= 35000:
        return 150 + (chargeable_income - 20000) * 0.03
    elif chargeable_income <= 50000:
        return 600 + (chargeable_income - 35000) * 0.08
    elif chargeable_income <= 70000:
        return 1800 + (chargeable_income - 50000) * 0.13
    elif chargeable_income <= 100000:
        return 4400 + (chargeable_income - 70000) * 0.21
    elif chargeable_income <= 250000:
        chargeable_income -= 100000
        return 10900 + (chargeable_income * 0.24)
    elif chargeable_income <= 400000:
        chargeable_income -= 250000
        return 46900 + (chargeable_income * 0.245)
    elif chargeable_income <= 600000:
        chargeable_income -= 400000
        return 83650 + (chargeable_income * 0.25)
    elif chargeable_income <= 1000000:
        chargeable_income -= 600000
        return 133650 + (chargeable_income * 0.26)
    else:
        chargeable_income -= 1000000
        return 237650 + (chargeable_income * 0.28)

def save_to_csv(data, filename='tax_records.csv'):
    """
    Save user data to a CSV file.
    If file exists, append data. If not, create new file with header.
    """
    import os
    df = pd.DataFrame([data])
    
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)
    return True

def read_from_csv(filename='tax_records.csv'):
    """
    Read data from CSV file and return as DataFrame.
    Returns None if file doesn't exist.
    """
    import os
    if not os.path.exists(filename):
        return None
    return pd.read_csv(filename)
