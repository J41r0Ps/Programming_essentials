number1 = int(input("number 1 (0, 1 or 2): "))
number2 = int(input("number 1 (0, 1 or 2): "))
number3 = int(input("number 1 (0, 1 or 2): "))

if (number2 == number3) != number1:
    print(1)
elif number1 == number2 == number3 and 4 not in [number1, number2, number3]:
    print(5)
elif number1 == 2 and number2 == 2 and number3 == 2:
    print(10)
else:
    print(0)