from bank.domainModel.interface.abstractRepositoryAccount import AbstractRepositoryAccount
from bank.domainModel.accountNumber import AccountNumber
from bank.domainModel.account import Account

class RepositoryAccount(AbstractRepositoryAccount):

    def __init__(self):
        self.items = dict([])

    def get(self, number) -> Account:
        return self.items[number]

    def add(self, model: Account):
        self.items[model.number.value] = model
             
