first_name = input("Enter the first name: ")
second_name = input("Enter the second name: ")

print(f"Before changing: {first_name} {second_name}")

temp = first_name
first_name = second_name
second_name = temp

print(f"After changing : {first_name} {second_name}")