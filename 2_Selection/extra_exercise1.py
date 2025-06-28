year = int(input("Enter a year: "))

if year < 1582 and year % 4 == 0:
    print("This is a leap year")
elif year > 1582 and (year % 400 == 0 or year % 4 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")