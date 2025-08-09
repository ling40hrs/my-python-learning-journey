
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def name(self):
        return self.name
    
    def check_balance(self):
        print(f"Account Owner: {self.name} | Balance: ${self.balance}")
    
    def deposit(self, deposit_ammount):
        self.balance += deposit_ammount
        print(f"{self.name} deposits ${deposit_ammount}...")
        print(f"Deposited {deposit_ammount}. New balance is ${self.balance}.")

    def silent_deposit(self, deposit_ammount):
        self.balance += deposit_ammount    

    def withdraw(self, withdraw_ammount):
        self.withdraw_amount = withdraw_ammount
        if self.balance >= self.withdraw_amount:
            self.balance -= self.withdraw_amount
            print(f"{self.name} withdraws ${self.withdraw_amount}...")
            print(f"Withdrew ${self.withdraw_amount}. New balance is ${self.balance}.")
        else:
            print("Can't withdraw, no balance.")

    def transfer(self,  recipient, transfer_ammount):
        self.recipient = recipient
        self.transfer_ammount = transfer_ammount

        for x, y  in bank_accounts.items():
            if y == self.recipient and not self.recipient == self.name:                
                print(f"""{self.name} transfers ${self.transfer_ammount} to {self.recipient}...
Transferred ${self.transfer_ammount} to {self.recipient}.""")
                x.silent_deposit(self.transfer_ammount)
                self.balance -= self.transfer_ammount

            elif self.recipient == self.name:
                print("Can't transfer to own account. Use deposit method instead.")
                break

account1 =  BankAccount("Alice", 500)
account2 = BankAccount("Bob", 100)

bank_accounts = {
    account1: account1.name,
    account2: account2.name
}

print("--- Initial Balances ---" )
account1.check_balance()
account2.check_balance()

print("--- Performing Transactions ---")

account1.deposit(50)

account2.withdraw(20)

account1.transfer("Bob", 100)

print("--- Final Balances ---")
account1.check_balance()
account2.check_balance()