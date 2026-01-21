# Bank Management System

accounts = {}

def create_account():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Account already exists!")
    else:
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Balance: "))
        accounts[acc_no] = {"name": name, "balance": balance}
        print("Account created successfully!")

def deposit():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter Amount to Deposit: "))
        accounts[acc_no]["balance"] += amount
        print("Amount deposited successfully!")
    else:
        print("Account not found!")

def withdraw():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter Amount to Withdraw: "))
        if amount <= accounts[acc_no]["balance"]:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def check_balance():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Account Holder:", accounts[acc_no]["name"])
        print("Current Balance:", accounts[acc_no]["balance"])
    else:
        print("Account not found!")

def view_accounts():
    if not accounts:
        print("No accounts available.")
    else:
        for acc_no, details in accounts.items():
            print("Account No:", acc_no,
                  "| Name:", details["name"],
                  "| Balance:", details["balance"])

# Main Menu
while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        view_accounts()
    elif choice == "6":
        print("Thank you for using Bank Management System")
        break
    else:
        print("Invalid choice! Try again.")
