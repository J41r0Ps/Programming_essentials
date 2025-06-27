from datetime import datetime

year_of_birth = int(input("Enter your year of birth: "))
age = datetime.now().year - year_of_birth

print(f"Your age = {age}")
print("So you're an adult") if age >= 18 else print("You're not an adult yet")