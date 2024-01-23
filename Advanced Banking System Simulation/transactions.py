from abc import ABC, abstractmethod
from customers import Customer

class TransactionType(ABC):
    @abstractmethod
    def deposit(self, name, amount):
        pass

    @abstractmethod
    def withdrawal(self, name, amount):
        pass

class Transactions(TransactionType):

    def deposit(self, name, amount):
        if name in Customer.BankAccountData:
            Customer.BankAccountData[name]["Balance"] += amount

            if "Transactions" not in Customer.BankAccountData[name]:
                Customer.BankAccountData[name]["Transactions"] = {"Withdrawals": {}, "Deposits": {}}

            if "Deposit" not in Customer.BankAccountData[name]["Transactions"]["Deposits"]:
                Customer.BankAccountData[name]["Transactions"]["Deposits"]["Deposit"] = amount
            else:
                Customer.BankAccountData[name]["Transactions"]["Deposits"]["Deposit"] += amount

    def withdrawal(self, name, amount):
        if name in Customer.BankAccountData:
            if Customer.BankAccountData[name]["Balance"] >= amount:
                Customer.BankAccountData[name]["Balance"] -= amount

                if "Transactions" not in Customer.BankAccountData[name]:
                    Customer.BankAccountData[name]["Transactions"] = {"Withdrawals": {}, "Deposits": {}}

                if "Withdrawal" not in Customer.BankAccountData[name]["Transactions"]["Withdrawals"]:
                    Customer.BankAccountData[name]["Transactions"]["Withdrawals"]["Withdrawal"] = amount
                else:
                    Customer.BankAccountData[name]["Transactions"]["Withdrawals"]["Withdrawal"] -= amount
