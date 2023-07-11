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
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
    	# your code here
        self.account.deposit(amount)
        return self
    def make_withdrawal (self,amount):
        self.account.withdraw(amount)
        return self.account
    def display_user_balance(self):
        self.account.display_account_info()
        return self

first_user=User("achref","jachref@gamil.com")
first_user.make_deposit(100).make_deposit(100).make_deposit(100).display_user_balance()
print(f"user:{first_user.name} ; checking balance :{first_user.display_user_balance}")  
  

