def userchoice ():
    print()
    uchoice = input("Enter your Choice [1-4]: ")
    if uchoice.isdigit() :
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
    pass
def withdraw():
    pass
def deposite():
    pass
def quit():
    pass
def main():

    print("1. Show Balance")
    print("2. Withdraw")
    print("3. Deposite")
    print("4. Quit")

    userchoice()

    global balance
    balance = 83068.65




if __name__ == '__main__':
    print()
    print("*********************************")
    print("   Welcome To Banking Program")
    print("*********************************")
    print()
    main()