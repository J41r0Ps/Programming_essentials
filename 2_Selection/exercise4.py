number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))

if (number1 + number2 == number3) or (number2 + number3 == number1) or (number3 + number1 == number2):
    print("This works")
else:
    print("This won't work")