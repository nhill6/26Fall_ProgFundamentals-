class Bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Added {amount} to the balance")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Not enough funds")
        else:
            self.balance -= amount
            print("Withdrawal accepted")
    def get_balance(self):
        return self.balance

account1 = Bankaccount("John",1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1000)
print(account1.get_balance())