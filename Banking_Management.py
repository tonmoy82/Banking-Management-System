class Banking:
     def __init__(self, user_name, initial_balance):
          self.name  = user_name
          self.balance = initial_balance
          
     def deposit(self, amount):
         if amount>0:
             self.balance += amount
         return amount
     
     def get_balance(self):
         return self.balance
     
     def withdraw(self, amount):
          if amount < self.balance:
              self.balance -= amount
              return amount
          else:
              return f"Insufficient Balance"
         
          
account = Banking("Tonmoy", 50000)
print(f"Account Name: {account.name}")
print(f"Initial Balance is: {account.balance}")
print(f"Deposit Balance: {account.deposit(20000)}")
print(f"After deposit, Your Balance is: {account.get_balance()}")
print(f"Withdraw Balance: {account.withdraw(10000)}")
print(f"After withdraw, Your Balance is: {account.get_balance()}")