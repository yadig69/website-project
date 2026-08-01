from utils.bank import BankAccount


# todo-> Write test code (either within a main section in bank.py or in a separate test file) to:

if __name__ == "__main__":
    print("-- initialize Account --")
# * 1. Create an instance of BankAccount.
    users_account = BankAccount (account_number = "12345", owner = "Alice", balance = 500)
    print(users_account)
    print()
# ~ Demonstrate a successful deposit and withdrawal.
    users_account.deposit(amount = 300.00)
    print(f"Balance after deposit: -> ${users_account.balance:.2f} ")
    print(f"Balance after deposit: -> New balance: ${users_account.balance:.2f} ")
    users_account.withdrawal(amount = 100.00)
    print(f"Balance after withdrawal: -> ${users_account.balance:.2f} ")

# //// Attempt a withdrawal that exceeds the balance to trigger and catch the exception, printing an error message.
    try:
        users_account.withdrawal(amount = 1000.00)
    except ValueError as e:
        print(f"Error: {e}")