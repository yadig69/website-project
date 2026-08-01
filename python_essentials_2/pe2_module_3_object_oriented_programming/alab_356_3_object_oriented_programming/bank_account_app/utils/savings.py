# Task 2: Subclassing and Inheritance (SavingsAccount)
print("\n-- Task 2: Subclassing and Inheritance --")

from utils.bank import BankAccount
# In the same file or a new file (e.g., savings.py), create a subclass SavingsAccount that inherits from BankAccount:
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance: float = 0.0, interest_rate: float = 0.0):
        # Call the parent class initializer
        super().__init__(account_number, owner, balance)
        # Initialize the additional attribute
        self.interest_rate = interest_rate
    
    def apply_interest(self) -> float:
        # Calculate interest and add it to the balance
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return self.balance

    def __str__(self):
        # Return a string representation including the interest rate
        return f"Account {self.account_number} - Owner: {self.owner}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%"
# ^ Additional Attribute:
# //// interest_rate (representing the annual interest rate as a percentage).
# //// Initializer:
# //// Modify the initializer to accept interest_rate along with other parameters and call the base class initializer using super().__init__().
# ^ Additional Method:
# //// apply_interest(self): Calculate the interest based on the current balance and interest_rate, and add it to the balance. For example, if the interest rate is 5%, add balance * 0.05 to the balance.
# ^ Method Overriding:
# //// Override the __str__ method to include the interest rate in the account’s string representation.

