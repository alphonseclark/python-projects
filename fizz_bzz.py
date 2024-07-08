def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif (num % 3 == 0):
        print("Fizz")
    elif (num % 5 == 0):
        print("Buzz")
    else:
        print("Not Fizz or Buzz")

fizz_buzz(12)
fizz_buzz(10)
fizz_buzz(9)
fizz_buzz(15)