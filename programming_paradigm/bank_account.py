# Title: Create a Simple Bank Account Class
# Author: Archie Prince
# Filename: bank_account.py
# Date: 19.01.2025
# Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations.
# Use command line arguments to interact with instances of this class.

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional initial balance.
        :param initial_balance: Initial balance for the account, defaults to 0.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        :param amount: The amount to deposit (must be positive).
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds exist.
        :param amount: The amount to withdraw (must be positive).
        :return: True if the withdrawal is successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
