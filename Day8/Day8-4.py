#Implement a BankAccount base class and inherit SavingsAccount and CurrentAccount.
class BankAccount:
    def __init__(self, balance=0):
        self.balance=balance

    def check_balance(self):
        print("Balance:", self.balance)

class SavingAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__(balance)
    
    def Rate(self):
        print("intrest Rate:0.5%")

class CurrentAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__(balance)
    
    def limit(self):
        print("Overdraft Limit:1000")

s = SavingAccount(10000)
s.Rate()
s.check_balance()

c = CurrentAccount(20000)
c.limit()
c.check_balance()