
from utils.savings import SavingsAccount
# Write test code that:


#? Creates an instance of SavingsAccount.
if __name__ == "__main__":
    savings_account = SavingsAccount(account_number = "54321", owner = "Alice", balance = 1000.0, interest_rate = 5.0)
    print(savings_account)
#? Demonstrates the inherited deposit and withdraw functionalities.
    savings_account.deposit(1500)
    print(f"Deposit: 1500  Your savings Balance: -> ${savings_account.balance:.2f} ")
    print()
    savings_account.withdrawal(200)
    print(f"Your savings Balance: -> ${savings_account.balance:.2f} ")
#? Calls apply_interest() and prints the account to verify that the balance updates correctly and the interest rate is displayed.
    savings_account.apply_interest()
    print(f"Your savings Balance after interest: -> ${savings_account.balance:.2f} ")