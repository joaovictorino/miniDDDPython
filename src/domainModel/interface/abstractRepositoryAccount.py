import abc
from src.domainModel.accountNumber import AccountNumber
from src.domainModel.account import Account

class AbstractRepositoryAccount(abc.ABC):

    @abc.abstractmethod
    def get(self, accountNumber: AccountNumber) -> Account:
        pass

    @abc.abstractmethod
    def add(self, model: Account):
        pass