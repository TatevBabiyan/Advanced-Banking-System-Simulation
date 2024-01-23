from descriptor import Descriptor

class Customer:
    name = Descriptor()
    contact_information = Descriptor()

    BankAccountData = {}

    def __init__(self, name, contact_information):
        self._name = name
        self._contact_information = contact_information


    def register_as_customer(self):
        if len(self._name) >= 5 and self._name.isalpha() and len(self._contact_information) == 9 and self._contact_information[0] == '0' and self._contact_information.isdigit():
            if self._name not in Customer.BankAccountData:
                Customer.BankAccountData[self._name] = {}
                Customer.BankAccountData[self._name].update({'Contact Information':self._contact_information})
            return "added"
        else:
            raise ValueError("Enter Valid Data")

    def view_transaction_history(self, name):
        if name in Customer.BankAccountData:
            return Customer.BankAccountData[name]["Transactions"]


