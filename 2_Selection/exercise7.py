first_number = int(input("First number: "))
second_number = int(input("Second number: "))

if first_number == second_number:
    print(0)
elif first_number % 5 == 0 and second_number % 5 == 0:
    print(min(first_number,second_number))
else:
    print(f"The answer for the number {abs(first_number)} and {abs(second_number)} = {max(abs(first_number),abs(second_number))}")