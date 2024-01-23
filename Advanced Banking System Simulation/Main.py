from customers import *
from account import Account
from account_types import *
from transactions import *

def menu():
    print("1. Register as Customer")
    print("2. Create an Account")
    print("3. Choose Account Type (Saving/Checking)")
    print("4. Deposit")
    print("5. Withdrawal")
    print("6. View Transaction History")
    print("7. Exit")

def main():
    choice:int = 0
    while choice != 7:
        menu()
        choice = int(input("Choose: "))

        if choice == 1:
            name = input("Enter your Name: ")
            contactinfo = input("Enter your Contact Information: ")
            customer = Customer(name, contactinfo)
            customer.register_as_customer()
            print(Customer.BankAccountData)

        elif choice == 2:
            name = input("Enter your Name: ")
            account = Account()
            account.accnumbercheck(name)
            print(Customer.BankAccountData)

        elif choice == 3:
            acc_type = input("Saving Account or Checking Account: ")
            if acc_type == "Saving Account":
                amount = int(input("Amount that you want to save in your account: "))
                obj = Saving_Account(amount)
                name = input("Enter your Account Name: ")
                obj.saving_account(name)
            if acc_type == "Checking Account":
                amount = int(input("Amount that you want to save in your account: "))
                obj = Checking_Account(amount)
                name = input("Enter your Account Name: ")
                obj.checking_account(name)

            print(Customer.BankAccountData)

        elif choice == 4:
            name = input("Enter your Account Name: ")
            amount = int(input("Amount of Money you want to add: "))
            deposit = Transactions()
            deposit.deposit(name, amount)
            print(Customer.BankAccountData)


        elif choice == 5:
            name = input("Enter your Account Name: ")
            amount = int(input("Amount of Money you want to withdraw: "))
            withdraw = Transactions()
            withdraw.withdrawal(name, amount)
            print(Customer.BankAccountData)

        elif choice == 6:
            name = input("Enter your Name: ")
            customer = Customer(name, 0)
            print(customer.view_transaction_history(name))

        elif choice == 7:
            break

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(f"An error occurred: {e}")

        try_again = input("Do you want to try again? (y/n): ").lower()
        if try_again != 'y':
            break

