from domainModel.interface.abstractRepositoryAccount import AbstractRepositoryAccount

class TransferMoneyService:
    def __init__(self, repository):
        self.repository = repository

    def transfer(self, numberFrom: str, numberTo: str, balance):
        accountFrom = self.repository.get(numberFrom)
        accountTo = self.repository.get(numberTo)
        accountFrom.withdraw(balance)
        accountTo.deposit(balance)
        self.repository.add(accountFrom)
        self.repository.add(accountTo)