import abc
from bank.domainModel.accountNumber import AccountNumber
from bank.domainModel.account import Account

class AbstractRepositoryAccount(abc.ABC):

    @abc.abstractmethod
    def get(self, accountNumber: AccountNumber) -> Account:
        pass

    @abc.abstractmethod
    def add(self, model: Account):
        pass