class BankAccount:
    def __init__(self):
        self.balance = 0
        owner_name = str(input("Insert your name: "))
        
        print(f"Hello {owner_name}, welcome to your bank account!")

    def deposit(self):
        amount = float(input("Enter the amount deposited: "))
        self.balance += amount
        print("\n Amount deposited: ", amount)
        print("\n Current account balance: ", self.balance)

    def withdrawal(self):
        amount = float(input("Enter the amount to withdrawn: "))
        if self.balance >= 0:   
            self.balance += amount
            print("\n Amount withdrawn: ", amount)
        else:
            print("\n Insuficient balance ")
    
    def display(self):
        print("\n Current account balance: ", self.balance)
            
bank_account = BankAccount()

menu = int(input("Select a bank menu option (1 -d, 2 - w, 3 - display): "))

if menu == 1:
     bank_account.deposit()
elif menu == 2:
    bank_account.withdrawal()
elif menu == 3:
    bank_account.display()
else:
    None