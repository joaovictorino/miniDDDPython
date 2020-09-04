import pytest
from src.domainModel.account import Account

def test_deposit():
    account = Account("123456", 100)
    account.deposit(50)
    assert account.balance == 150

def test_withdraw():
    account = Account("123456", 200)
    account.withdraw(100)
    assert account.balance == 100