import pytest
from src.application.transferMoneyService import TransferMoneyService
from src.adapter.repositoryAccount import RepositoryAccount
from src.domainModel.account import Account
from src.domainModel.accountNumber import AccountNumber

def test_transferMoney():
    repository = RepositoryAccount()
    accountFrom = Account(AccountNumber("123456"), 1200)
    accountTo = Account(AccountNumber("654321"), 500)
    repository.add(accountFrom)
    repository.add(accountTo)

    transferService = TransferMoneyService(repository)
    transferService.transfer(accountFrom.number.value, accountTo.number.value, 200)

    assert repository.get("123456").balance == 1000
    assert repository.get("654321").balance == 700