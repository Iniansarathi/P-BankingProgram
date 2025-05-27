def userchoice():
    print()
    print("1. Show Balance")
    print("2. Withdraw")
    print("3. Deposite")
    print("4. Quit")
    print()
    uchoice = input("Enter your Choice [1-4]: ")
    if uchoice.isdigit():
        uchoice = int(uchoice)
        if uchoice > 0 and uchoice <5:
            if uchoice == 1:
                showbalance()
            elif uchoice == 2:
                withdraw()
            elif uchoice == 3:
                deposite()
            else:
                quit()
        else:
            print("Invalid input")
            userchoice()

def showbalance():
    global balance
    print()
    print(f"Available Balance : {balance:.2f}")
    continuebanking()


def withdraw():
    global balance
    print()
    withdraw_amt= input("Enter the amount you want to withdraw :")
    if withdraw_amt.isdigit():
        withdraw_amt = int(withdraw_amt)
        if withdraw_amt <= balance :
            print(f"₹{withdraw_amt:.2f} successfully withdrawn. ")
            balance -=withdraw_amt
            print(f"Available Balance : {balance:.2f}")
            continuebanking()
        elif withdraw_amt > balance:
            print("Insufficient Balance !!!")
            continuebanking()
    else:
        print("Invalid Input.Enter the amount you like to withdraw in numbers")
        continuebanking()

def deposite():
    pass
def quit():
    print()
    print("*****************")
    print("*  Thankyou 🙏  *")
    print("*****************")
def continuebanking():
    print()
    sb_uchoice = input("Would you like to continue banking [y/n]").lower()
    if sb_uchoice.isalpha():
        if sb_uchoice == "y":
            userchoice()
        elif sb_uchoice == "n":
            quit()
        else:
            print("Invalid input")
            continuebanking()
    else:
        print("Invalid input")
        continuebanking()
def main():
    global balance

    balance = 83068.65

    userchoice()






if __name__ == '__main__':
    print()
    print("*********************************")
    print("   Welcome To Banking Program")
    print("*********************************")
    print()
    main()