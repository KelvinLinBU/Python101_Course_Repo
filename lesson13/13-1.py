class BankAccount:
    def __init__(self, owner,balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if isinstance(amount, int): 
            if amount > 0:
                self._balance += amount

    def withdraw(self, amount):
        if isinstance(amount, int): 
            if amount > 0 and amount <= self._balance:
                self._balance -= amount

    def get_balance(self):
        return self._balance
    
account1 = BankAccount("Kelvin", 1000)
print(account1.get_balance())