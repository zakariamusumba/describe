class BankAccount:
    def __init__(self, owner, account_number, starting_balance):
        self.owner = owner
        self.account_number = account_number
        self.starting_balance = starting_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        if amount <= self._balance

        elif 

account1 = BankAccount("John", "1234", 4000)
print(account1.owner)
print(account1.account_number)
print(account1.starting_balance)