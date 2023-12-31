#!/usr/bin/python3
"""class with hidden data fields"""


class BankAccount:
    """constructor or initializer"""
    def __init__(self, name, money):
        self.__name = name
        """__balance is private now,
        so it is only accessible inside the
        class
        """
        self.__balance = money

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return (money)
        else:
            return ("Insufficient funds")

    def checkbalance(self):
        return (self.__balance)

b1 = BankAccount('tim', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbalance())
print(b1.withdraw(800))
print(b1.checkbalance())
