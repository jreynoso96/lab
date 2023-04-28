import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')
        self.a2 = Account('Daisy')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a2.get_name() == 'Daisy'
        assert self.a1.get_balance() == 0
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(0.0) == False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(-50.0) == False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(50.0) == True
        assert self.a1.get_balance() == 50.0

        assert self.a2.deposit(0.0) == False
        assert self.a2.get_balance() == 0
        assert self.a2.deposit(-5.0) == False
        assert self.a2.get_balance() == 0
        assert self.a2.deposit(100.0) == True
        assert self.a2.get_balance() == 100.0

    def test_withdraw(self):
        assert self.a1.withdraw(-50.0) == False
        assert self.a1.get_balance() == 0
        assert self.a1.withdraw(0.0) == False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(50.0) == True
        assert self.a1.get_balance() == 50.0
        assert self.a1.withdraw(100.0) == False
        assert self.a1.get_balance() == 50.0
        assert self.a1.withdraw(-50.0) == False
        assert self.a1.get_balance() == 50.0
        assert self.a1.withdraw(20.0) == True
        assert self.a1.get_balance() == 30.0

        assert self.a2.withdraw(-50.0) == False
        assert self.a2.get_balance() == 0.0
        assert self.a2.withdraw(0.0) == False
        assert self.a2.get_balance() == 0.0
        assert self.a2.deposit(100.0) == True
        assert self.a2.get_balance() == 100.0
        assert self.a2.withdraw(-100.0) == False
        assert self.a2.get_balance() == 100.0
        assert self.a2.withdraw(2000.0) == False
        assert self.a2.get_balance() == 100.0
        assert self.a2.withdraw(50.0) == True
        assert self.a2.get_balance() == 50.0
