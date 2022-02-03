class Bank:
    def __init__(self,name,accountNo,password):
        self.owner = name
        self.balance = 0.0
        self.accountNo = accountNo
        self.password = password
        self.log = True

    def getBalance(self):
        return self.balance
        
    def control(self,a_no,p):
        if len(p) == 9:
            if a_no == self.accountNo and p == self.password:
                print("Your login has occurred. Welcome...")
                return self.log
            else:
                print("You entered your user name or password incorrectly. Try again...")
                self.log = False
                return self.log
        
        else:
            print("You entered a missing password...")

    def deposit(self,amount):
        self.balance+= amount
    
    def withdraw(self,amount):
        if (self.balance < amount ):
            print("\n Insufficient balance!....")
        else:
            self.balance -=amount

    
   
class App :
    def __init__(self):
        self.bank_acc = Bank("Öykü Sıla Şahin","BA12345","123456789")

    def check(self,acc_No,psw):
        return self.bank_acc.control(acc_No,psw)
   
    def login(self):
        dongu_girdi = False
        hak = 3
        while dongu_girdi == False or hak != 0:
            acc_No = input("Please enter your account number: ")
            psw = input("Enter your password: ")
            dongu_girdi = self.check(acc_No, psw)
            if dongu_girdi == False:
                if hak == 0:
                    print("You entered the wrong password 3 times. Your card is blocked...")
                hak -= 1
            else:
                dongu_girdi = True
                self.run()
    
    def run(self):
        print("Please select the defined process...")
        print("1-)Withdrawal\n","2-)Deposit\n","3-)Balance Inquiry\n","4-)Exit")
        dongu = True
        while dongu == True:
            op = int(input("Select and enter the action you want to do from the menu: "))
            if op == 1:
                print("You have selected the Withdrawal Process..")
                wAmount = float(input("Enter amount to be Withdrawn: "))
                self.bank_acc.withdraw(wAmount)
                dongu = False
            elif op == 2:
                print("You have selected the Deposit...")
                dAmount = float(input("Enter amount to be Deposited: "))
                self.bank_acc.deposit(dAmount)
                dongu = False
            elif op == 3:
                print("You have selected Balance Inquiry..")
                print("\n Net Available Balance=",self.bank_acc.getBalance())
                dongu = False
            elif op == 4:
                print("You have selected the Output Process...")
                print ("Thankyou for using the bank!")
                dongu = False
                exit()

            else:
                print("You made an incorrect transaction selection. Please select a valid transaction!!!") 



def main():
    print("Enter your account number and password to log into your bank account...")
    bank = App()
    bank.login()

main()
