import pytest
from bank.domainModel.service.transferMoneyService import TransferMoneyService
from bank.adapter.repositoryAccount import RepositoryAccount
from bank.domainModel.account import Account
from bank.domainModel.accountNumber import AccountNumber

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