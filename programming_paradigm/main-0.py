# Title: Create a Simple Bank Account Class
# Author: Archie Prince
# Filename: main-0.py
# Date: 19.01.2025
# Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations.
# Use command line arguments to interact with instances of this class.

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Withdrawal failed.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or syntax. Use one of the following:")
        print("  deposit:<amount>")
        print("  withdraw:<amount>")
        print("  display")

if __name__ == "__main__":
    main()
