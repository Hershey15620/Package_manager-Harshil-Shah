class atm:
    def __init__(self, number, pin): 
        self.number= number
        self.pin=pin

    def checkbalance(self):
        print("$50000")
    def depositmoney(self,amount):
        new_amount=50000+amount
        print("currentbalance=", new_amount)
    def withdrawmoney(self,amount):
        new_amount=50000-amount
        print("currentbalance", new_amount)        
        
        
def main():
    card_number=input("give your card number")
    pin_number=input("give your pin number")

    new_user= atm(card_number,pin_number)     
    print("choose your activity")
    print("1.check balance,2.withdraw,3.deposit") 
    activity=int(input("Enter your choice:"))  
    if(activity == 1):
        new_user.checkbalance()
    elif(activity == 2):
        amount= int(input("Enter the amount you want to withdraw"))    
        new_user.withdrawmoney(amount)
    elif(activity == 3):
        amount= int(input("Enter the amount you want to deposit")) 
        new_user.depositmoney(amount)
    else: print("enter a valid number")

if __name__ == "__main__":
    main()   