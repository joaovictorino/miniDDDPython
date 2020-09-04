from src.domainModel.interface.abstractRepositoryAccount import AbstractRepositoryAccount
from src.domainModel.accountNumber import AccountNumber
from src.domainModel.account import Account

class RepositoryAccount(AbstractRepositoryAccount):

    def __init__(self):
        self.items = dict([])

    def get(self, number) -> Account:
        return self.items[number]

    def add(self, model: Account):
        self.items[model.number.value] = model
             
