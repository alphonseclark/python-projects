def Age_checker():
    user_age=int(input("What is your age"))
    yes or no=True

    while True:
    if(user_age<12):
        print("You are a child")
    elif(12<user_age<20):
        print("You are a teen")
    else(20<user_age):
        print("You are a adult")
    yes or no=input(Try again)


Age_checker()