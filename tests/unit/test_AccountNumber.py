import pytest
from bank.domainModel.accountNumber import AccountNumber

def test_NumberAccount():
    number = AccountNumber("123456")

def test_NumberAccount():
    with pytest.raises(ValueError):
        number = AccountNumber("12345")