import getpass 

def withdraw(checking):
    withdrawal=int(input("How much do you want to withdraw:"))
    newbal=checking-withdrawal
    return newbal

def deposit(checking):
    deposit=int(input("How much do you want to add:"))
    newbal=checking+deposit
    return newbal

def balance(checking):
    newbal=checking
    return newbal



def main():
    print("Welcome to the ATM")
    userName=input("What is your username?")
    password=getpass.getpass()
    print(password)
    print("Welcome!" ,userName)
    checking=600
    choice=int(input("1. withdraw, 2. deposit, 3. balance"))
    if(choice==1):
        print("You now have: " ,withdraw(checking))

    elif(choice==2):
        print("You now have: " ,deposit(checking))

    elif(chocie==3):
        print("Your balance is: ")

    else:
        print("Try Again")

    print("Goodbye")


if __name__=="__main__":
    main()