"""Bank Account

Create a BankAccount with owner and balance (default 0), plus deposit(amount),
withdraw(amount), and show_balance() methods. Test several deposits and
withdrawals, including one that should fail for insufficient funds.
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Withdrawal refused: insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}.")

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance:.2f}")


account = BankAccount("Jordan")
account.show_balance()
account.deposit(100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)  # This withdrawal should fail.
account.withdraw(20)
account.show_balance()
