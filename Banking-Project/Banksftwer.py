# Importing Libraries
import numpy as np # Importing Numpy as np
# Class ATM
class Atm():
      #Constructor for initializing variable
    def __init__(self, name, account_no , balance=0):  
        self.name = name
        self.account_no = account_no
        self.balance = balance
      #Method for printing account inforamtion/credential
    def account_credential(self):
        print("\n------------ACCOUNT CREDENTIALS------------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_no}")
        print(f"Account Balance: ₹{self.balance}\n")
      #Method for depositing money  
    def deposite(self, amount) :
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Deposit successful")
        print("₹{} Deposited Successfully...".format(amount))
        print("Current Balance: ₹",self.balance, '\n')
       #Method for withdraw money   
    def withdraw(self, amount) :
        self.amount = amount
        if self.amount <= self.balance:
            self.balance = self.balance - self.amount
            print("Withdraw Successful")
            print("₹{} Withdraw Successfully...".format(amount))
            print("Current Balance: ₹",self.balance, '\n')
        else:
            print("Insufficient Funds\n")
      #Method for checking balance
    def check_balance(self) :
        print("Available Balance: ₹",self.balance, '\n')
        print()
      #Method for printing menu  
    def menu(self) :
        print( '''
        ************** MENU **************
                1> Account Detail.
                2> Check Balance.
                3> Deposit.                 
                4> Withdraw.
                5> Exit.                    
        ***********************************
            '''
        )
        
        while True:
            try:
                user_input = int(input("Enter 1, 2, 3, 4 or 5: "))
            except:
                print("Error: Only Enter 1, 2, 3, 4 or 5 \n")
                continue
            else: 
                if user_input == 1:
                    atm.account_credential()
                elif user_input == 2:
                    atm.check_balance()
                elif user_input == 3:
                    amount = int(input("How Much You Want To Deposite: "))
                    atm.deposite(amount)
                elif user_input == 4:
                    amount = int(input("How Much You Want To Withdraw: "))
                    atm.withdraw(amount)
                elif user_input == 5:
                    # Generating random integer for tansaction ID using numpy
                    print(f'''
                    -------Transaction Summary-------
                    *********************************
                    Transaction ID: {np.random.randint(100000000, 1000000000)} 
                    Name: {self.name.upper()}
                    Account Number: {self.account_no}
                    Avalabel Balance: ₹{self.balance}
                    *********************************
                    Thank you for using our services
                    ''')
                    
                    exit()
                    
  
print("_______________________________________________________\n")
print("*********** WELCOME TO STATE BANK OF INDIA *************")
print("_______________________________________________________\n")
print("-----------------ACCOUNT CREATION---------------------")
name = input("Enter Your Name: ")
account_no = input("Enter your account number: ")
print("Congratulations! Account Created Successfully..........\n")

atm = Atm(name, account_no)

while True :
    trans = input("Do you want to do any transaction?(y/n): ")
    if trans == "y":
        atm.menu()
    elif trans == "n":
        print('''
         ------------------------------------------
        |   Thanks for choosing us as your bank    |
        |          Visit us again!                 |
         ------------------------------------------
        ''')
        break
    else:
        print("Wrong command! Enter 'y' for Yes and 'n' for No: \n")
