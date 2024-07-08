def atm():
    deposit_cash = int(input("How much do you want to desposit?"))
    withdraw = int(input("How much do you want to withdraw"))
    if (deposit_cash > withdraw):
        print("Your withdraw balance is ", deposit_cash - withdraw)
    else:
        print("Withdraw not possible")

atm()