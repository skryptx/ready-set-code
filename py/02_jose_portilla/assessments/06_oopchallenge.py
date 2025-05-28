"""
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""


class Account:
    """
    Bank Account class capable of depositing and withdrawing balance
    during Withdraw, the amount should not go in negative
    """

    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> None:
        if self.balance <= 0:
            print("Invalid Amount!")
            return

        print("Deposit Accepted")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if self.balance < amount or self.balance <= 0:
            print("Funds Unavailable!")
            return

        print("Withdrawal Accepted")
        self.balance -= amount

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"


# 1. Instantiate the class
acct1 = Account("Jose", 100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
