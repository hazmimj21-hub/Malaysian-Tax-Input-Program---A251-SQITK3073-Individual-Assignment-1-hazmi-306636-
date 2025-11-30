import pandas as pd
from functions import verify_user, calculate_tax, save_to_csv, read_from_csv

def display_tax_records():
    """Display all tax records from the CSV file."""
    df = read_from_csv()
    if df is None or df.empty:
        print("\nNo tax records found.")
    else:
        print("\n=== Tax Records ===")
        print(df.to_string(index=False))

def main():
    print("=== Malaysian Tax Input Program ===")
    
    while True:
        print("\n1. Register/Login")
        print("2. View Tax Records")
        print("3. Exit")
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            # Registration/Login
            ic_number = input("\nEnter your IC number (12 digits): ").strip()
            password = input("Enter your password (last 4 digits of IC): ").strip()
            
            if not verify_user(ic_number, password):
                print("Invalid IC number or password. Please try again.")
                continue
                
            print("\nLogin successful!")
            
            # Get user details
            try:
                income = float(input("\nEnter your annual income (RM): "))
                tax_relief = float(input("Enter your total tax relief (RM): "))
                
                if income < 0 or tax_relief < 0:
                    print("Income and tax relief cannot be negative.")
                    continue
                    
                # Calculate tax
                tax_payable = calculate_tax(income, tax_relief)
                print(f"\nYour calculated tax payable: RM{tax_payable:,.2f}")
                
                # Save to CSV
                user_data = {
                    'IC_Number': ic_number,
                    'Income_RM': income,
                    'Tax_Relief_RM': tax_relief,
                    'Tax_Payable_RM': tax_payable
                }
                save_to_csv(user_data)
                print("Your tax record has been saved successfully!")
                
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                
        elif choice == '2':
            display_tax_records()
            
        elif choice == '3':
            print("\nThank you for using the Malaysian Tax Input Program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()