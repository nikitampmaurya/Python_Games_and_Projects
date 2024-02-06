class Atm: #name of class should always be in PascalCase
    def __init__(self): #Constructor - assign value to data
        self.__pin = ""
        self.__balance = 0
        self.__menu() #call a method to do something
        
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if type(new_pin) == int:
            self.__pin = new_pin
            print("Pin has changed")
        else:
            print("not allowed")
            
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,new_balance):
        if type(new_balance) == int:
            self.__balance = new_balance
            print("Balance has changed")
        else:
            print("not allowed")

    def __menu(self): #method
        #taking input from users
        user_input = input(""" 
                           Hello, How would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw 
                           4. Enter 4 to check balance
                           5. Enter 5 to exit

""") 
        #assign input with work
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("exit")

    def create_pin(self): #defining work in the same class
        while True:
            temp=input("Enter your pin: ")
            if temp.isdigit():
                self.__pin = temp
                print("Pin is set successfully")
                break
            elif not temp.isdigit():
                print("Invalid pin, please enter only integers")

    def deposit(self):
        temp=input("Enter your pin to deposit amount: ")
        if temp==self.__pin:
            amount = int(input("Enter the amount to deposit: "))
            self.__balance+=amount #updating initial value of balance from the constructor
            print("Deposit is successful")
        else:
            print("pin is wrong")
    def withdraw(self):
        temp=input("Enter your pin to withdraw amount: ")
        if temp==self.__pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.__balance:
                self.__balance-=amount
                print("Transaction was successful")
            else:
                print("Insufficient Fund")
        else:
            print("pin is wrong")

    def check_balance(self):
        temp=input("Enter your pin to check balance: ")
        if temp==self.__pin:
            print(self.__balance)
        else:
            print("pin is wrong")

sbi = Atm()

