# Task 1: Defining a Base Class (BankAccount)
print("-- Task 1: Defining a Base Class --")
# Create a class BankAccount in a file (e.g., bank.py) that includes:
# ^ Attributes:
# account_number
# owner
# balance
# Initializer:
# //// __init__(self, account_number, owner, balance=0) that sets the initial values.
class BankAccount:
    def __init__(self, account_number, owner, balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

# ^ Methods:
# //// deposit(self, amount): Adds the given amount to balance. Allow only positive amounts; if a non-positive amount is passed, raise a ValueError with an appropriate message.

    def deposit(self, amount: float) -> float:
        # Check if the deposit amount is valid
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        return self.balance

# //// withdraw(self, amount): Subtracts the given amount from balance if sufficient funds exist. If the withdrawal amount is greater than the current balance, raise a ValueError (or your custom exception, if you choose to implement Task 3) indicating insufficient funds. Otherwise, deduct the amount and return the new balance.

    def withdrawal(self, amount: float) -> float:
        # Check if the withdrawal amount is valid and sufficient
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Trying to withdraw ${amount} with a balance of ${self.balance}")

        self.balance -= amount
        return self.balance
# //// __str__(self): Returns a string representation of the account (e.g., "Account 12345 – Owner: Alice, Balance: $500").

    def __str__(self):
        # Return a formatted string representation of the bank account
        return f"Account {self.account_number} - Owner: {self.owner}, Balance: ${self.balance}"



