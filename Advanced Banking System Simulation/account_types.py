from abc import ABC, abstractmethod
from customers import *

class Account_Type(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def saving_account(self, name):
        pass

    @abstractmethod
    def checking_account(self, name):
        pass


class Saving_Account(Account_Type):

    def saving_account(self, name):
        if name in Customer.BankAccountData:
            Customer.BankAccountData[name]["Account Type"] = {}
            Customer.BankAccountData[name]["Account Type"].update({'Saving Account':self.amount})
            return "Added"

    def checking_account(self, name):
        pass



class Checking_Account(Account_Type):

    def saving_account(self, name):
        pass

    def checking_account(self, name):
        if name in Customer.BankAccountData:
            amount = Customer.BankAccountData[name]["Balance"]
            Customer.BankAccountData[name]["Account Type"] = {}
            Customer.BankAccountData[name]["Account Type"].update({'Checking Account':amount})
            return "Added"

