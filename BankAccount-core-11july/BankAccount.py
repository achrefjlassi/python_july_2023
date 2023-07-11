class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        self.balance -= amount
        return self
        # your code here
    def display_account_info(self):
        print(f"the balance : {self.balance}")
        # your code here
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
        # your code here
john_account=BankAccount(0.01,1000)
jane_account=BankAccount(0.01,1500)
john_account.deposit(100).deposit(150).deposit(250).withdraw(70).yield_interest().display_account_info()
jane_account.deposit(100).deposit(150).withdraw(280).withdraw(120).withdraw(100).withdraw(500).yield_interest().display_account_info()