import pytest
from src.adapter.repositoryAccount import RepositoryAccount
from src.domainModel.account import Account
from src.domainModel.accountNumber import AccountNumber

def test_addAccount():
    number = AccountNumber("123456")
    account = Account(number, 100)
    repository = RepositoryAccount()
    repository.add(account)
    accountFromRepo = repository.get("123456")

    assert account.balance == accountFromRepo.balance

def test_updateAccount():
    number = AccountNumber("123456")
    account = Account(number, 100)
    repository = RepositoryAccount()
    repository.add(account)
    account.deposit(100)
    repository.add(account)
    assert account.balance == 200