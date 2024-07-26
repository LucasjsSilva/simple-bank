class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Cannot withdraw negative amount or zero")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Cannot deposit negative amount or zero")
        self.balance += amount
    
    def transfer(self, amount, destiny):
        if amount <= 0:
            raise ValueError("Cannot transfer negative amount or zero")        
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        destiny.balance += amount
        