# Write a class that meets these requirements.
#
# Name:       BankAccount
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.amount = []



# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
    def get_balance(self):
        return self.balance

    def deposit(self, amoount):
        self.balance += amoount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

# Example:
account001 = BankAccount(100)

print(account001.get_balance())  # prints 100
account001.withdraw(50)
print(account001.get_balance())  # prints 50
account001.deposit(120)
print(account001.get_balance())  # prints 170
#
# There is pseudocode for you to guide you.

# class BankAccount
    # method initializer(self, balance)
        # self.balance = balance

    # method get_balance(self)
        # returns the balance

    # method withdraw(self, amount)
        # reduces the balance by the amount

    # method deposit(self, amount)
        # increases the balance by the amount
