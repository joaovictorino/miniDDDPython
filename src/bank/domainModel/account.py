from domainModel.accountNumber import AccountNumber

class Account:
    def __init__(self, number: AccountNumber, balance):
        self.number = number
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value