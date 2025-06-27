first_number = int(input("Fist number: "))
second_number = int(input("Second number: "))

if (30 <= first_number <= 40) and (30 <= second_number <= 40) or (first_number or second_number) in [65, 72, 83, 90]:
    print("Both numbers are ok")
else:
    print("They are NOT ok")