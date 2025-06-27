number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))

smallest_number = number1
if smallest_number > number2:
    smallest_number = number2
elif smallest_number > number3:
    smallest_number = number3

# print(f"The smallest number is {smallest_number}")
print(f"The smallest number is {min(number1,number2,number3)}")