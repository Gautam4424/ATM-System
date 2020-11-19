print("Welcome to The Atm System \n Created by Gautam Sachdeva")
contine=int(input("press 1 to continue"))
if contine==1:
    print("Press 1 to withdrwal money from bank")
    print("press 2 to change the atm pin")
    print("press 3 to see the mini statement")
    print("press 4 for to check balance")
    option=int(input("Enter your choise"))
    if option==1:
        import withdral
        withdral.withdrawl()
    elif option==2:
        import change_pin
        change_pin.change_pin()
    elif option==3:
        import mini_statement
        mini_statement.mini_statement()
    elif option==4:
        import get_balance

        get_balance.get_balance()
    else:
        print("please enter valid option")



