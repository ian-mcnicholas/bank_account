


class BankAccount:
    
   
    # don't forget to add some default values for these parameters!
    def __init__(self, balance = 0, int_rate = 0.05, name =""): 
        self.balance = balance
        self.int_rate = int_rate
        self.name = name
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
        print(f'Your balance is: {self.balance} , Your interest rate is {self.int_rate}')
        return self
        # your code here
    def yield_interest(self):
        self.balance *= (1+ self.int_rate)
        return self

        # Create 2 accounts
    # accounts = [BankAccount(name = "John Account"), BankAccount(name = "Stacy Account")]

account1 = BankAccount(name = "John Account")
account2= BankAccount(name = "Stacy Account")
    # To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
account1.deposit(500).deposit(200).deposit(100).withdraw(65).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

account2.deposit(70000).deposit(1200000).withdraw(100000).withdraw(65000).withdraw(75000).withdraw(10000).yield_interest().display_account_info()



        # your code here

