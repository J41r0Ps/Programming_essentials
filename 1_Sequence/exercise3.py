import math

three_digit_number = int(input("Enter a three-digit number: "))

print(f"Half = {three_digit_number/ 2}")
print(f"Double = {three_digit_number * 2}")
print(f"Third power = {round(math.pow(three_digit_number,3))}")
print(f"Tenfold = {three_digit_number * 10}")
print("The digits are:")
print(f"{three_digit_number // 100 % 10}")
print(f"{three_digit_number // 10 % 10}")
print(f"{three_digit_number % 10}")