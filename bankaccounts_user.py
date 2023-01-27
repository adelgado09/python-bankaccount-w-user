class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        self.balance
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

    def display_user_balance(self):
        self.balance
        print(f"Balance: ${self.balance}")
        return self

# Account1=BankAccount()
# Account2=BankAccount()
# Account1.deposit (500).deposit(100).deposit(100).withdrawl(300).yield_interest().display_account_info()
# Account2.deposit(100).deposit(400).withdrawl(200).withdrawl(100).withdrawl(50).withdrawl(100).yield_interest().display_account_info()

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawl(amount)
        return self

    def display_user_balance(self):
        self.account.display_user_balance()
        return self

user1 = User("Sadie")
user1.make_deposit(100).make_deposit(250).display_user_balance()

user2 = User("William")
user2.make_deposit(1000).display_user_balance().make_withdrawal(450).display_user_balance()
