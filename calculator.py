def Calculate(num1, num2, func):
    if func == "add":
        print(num1 + num2)
    elif func == "sub":
        print(num1 - num2)
    elif func == "mult":
        print(num1 * num2)
    elif func == "div":
        print(num1 / num2)
    elif func == "pow":
        print(num1 ** num2)
    else:
        print("Error")


Calculate(2, 3, "add")
Calculate(6, 7, "mult")
Calculate(72, 8, "sub")
Calculate(2, 7, "div")
Calculate(3, 9, "pow")