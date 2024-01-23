from descriptor import Descriptor
import random
from customers import *


class Account:
    balance = Descriptor()

    def __init__(self):
        self._account_number = ''.join(random.choice('0123456789') for _ in range(16))
        self._balance = 100000

    def accnumbercheck(self, name):
        if name in Customer.BankAccountData:
            Customer.BankAccountData[name].update({"Account Number":self._account_number,
                                                   "Balance":self._balance})
            return "added"





