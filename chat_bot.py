def chat_bot():
    print("Welcome traveler")
    response = input("What do you need?\n")
    if (response == "calculate"):

        func = input("what do you wannt to calculate?\n")
        num1 = int(input("what's your first number?\n"))
        num2 = int(input("what's your second number?\n"))

        result = 0

        if (func == "add"):
            result = num1 + num2
        elif (func == "sub"):
             result = num1 - num2
        elif (func == "mult"):
             result = num1 * num2
        elif (func == "div"):
             result = num1 / num2
        elif (func == "pow"):
             result = num1 ** num2

        print("Your result is ", result)

chat_bot()