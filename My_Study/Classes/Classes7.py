# Копилка
class BankAccount:
    def __init__(self,balance = 0):
        self._balance = balance
    def get_balance(self):
        return self._balance
    def deposit(self,amount):
        self._balance += amount
    def withdraw(self,amount):
       if (self._balance - amount) < 0:
           raise ValueError('На счете недостаточно средств')
       else:
           self._balance -= amount
    def transfer(self,account,amount):
        if (self._balance - amount) >= 0:
            self.withdraw(amount)
            account.deposit(amount)
        else:
            raise ValueError('На счете недостаточно средств')

account1 = BankAccount(balance=100)
print(account1.get_balance())
account2 = BankAccount()
print(account2.get_balance())
account1.transfer(account2, 100)
print(account1.get_balance())
print(account2.get_balance())