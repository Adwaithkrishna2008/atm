from hashlib import new


class Atm:
    def __init__(self,pin,card_no):
        self.pin=pin
        self.card_no=card_no
    def balance_check(self):
        print("Your balance is 1,000,100")
    
    def cash_withdrawal(self,amount):
        new=1000100-amount
        print('You have withdrawn: '+str(amount)+' Your remaining balance is: '+str(new))
    
def main():
    card_no=input('Insert your card no:')
    pin=input('Enter your pin:')
    new_customer=Atm(pin,card_no)
    print("Choose your activity")
    print("1.BalanceEnquiry 2.Withdrawal")
    activity=int(input("Enter activity no: "))
    
    if activity==1 :
        new_customer.balance_check()
    elif activity==2:
        amount=int(input("please enter the required amount: "))
        new_customer.cash_withdrawal(amount)
    else:
        print("entered an Invalid no!")
        

if __name__=="__main__":
    main()




