# import SavingsAccount class from the utils/savings module
from utils.savings import SavingsAccount

if __name__ == "__main__":
    # create a SavingsAccount instance with an account number, owner, starting balance, and interest rate
    savings_account = SavingsAccount(account_number="54321", owner="Alice", balance=1000.0, interest_rate=5.0)
    # print the account details using the __str__ method
    print(savings_account)

    # demonstrate inherited deposit functionality from BankAccount
    savings_account.deposit(1500)
    print(f"Deposit: 1500  Your savings Balance: -> ${savings_account.balance:.2f} ")
    print()

    # demonstrate inherited withdrawal functionality from BankAccount
    savings_account.withdrawal(200)
    print(f"Your savings Balance: -> ${savings_account.balance:.2f} ")

    # apply interest to the current balance and print the updated balance
    # interest is calculated as: balance += balance * (interest_rate / 100)
    savings_account.apply_interest()
    print(f"Your savings Balance after interest: -> ${savings_account.balance:.2f} ")
