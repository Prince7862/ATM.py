
class ATM:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceInquiry(self):
        print("Your Balance is: $100")

    def cashWithDrawls(self, principal):
        new_principal = 100-principal
        print("You withdrawed: " + str(principal) + " Your remaining balance is: " + str(new_principal))

def main():
    name = input("Hello, what is your name: ")
    print("Hello " + name)
    cardNumber = input("What is the card number: ")
    pin = input("What is your pin number: ")
    new_user = ATM(cardNumber, pin)

    print("Choose your activity")
    print("1. Balance Inquiry")
    print("2. Cash WithDrawl")
    activity = int(input("Enter activity choice: "))

    if(activity == 1):
        new_user.balanceInquiry()
    elif(activity == 2):
      principal = int(input("Enter the amount: "))
      new_user.cashWithDrawls(principal)
    else:
        print("Enter a valid number: ")

main()
