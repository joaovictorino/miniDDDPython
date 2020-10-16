from bank.domainModel.service.transferMoneyService import TransferMoneyService
from bank.adapter.repositoryAccount import RepositoryAccount

class TransferApplicationService:

    def transfer(self, numberFrom: str, numberTo: str, balance):
        repository = RepositoryAccount()
        service = TransferMoneyService(repository)
        service.transfer(numberFrom, numberTo, balance)
