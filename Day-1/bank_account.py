class BankAccount:
    def __init__(self, account_number, account_holder, account_type, routing_number = "29842900"):
        self.account_number = account_number
        self.balance = 0.0
        self.account_holder = account_holder
        self.account_type = account_type
        self.routing_number = routing_number

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance -=withdraw

    def transfer(self, total):
        if total <= self.balance:
            self.balance -=total

account = BankAccount("29382", "Jen Ine", "checking")
account.deposite(450)
account.withdraw(500)
print(f"Your {account.account_type} account balance:  {account.balance}")

account_savings = BankAccount("23983798", "Jen Ine", "savings" )
account_savings.deposite(4000)




        