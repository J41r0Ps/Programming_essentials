"""
age = int(input("How old are you: "))
father_age = int(input("How old is your father: "))
years = 0

if father_age / 2 < age:
    print("The situation is no longer possible for your ages")
else:
    while father_age / 2 > age:
        years += 1
        age += 1
        father_age += 1
    print(f"Your father will be {father_age} and you will be {age}")
"""

# Advanced mode

def years_until_double_age(child_age: int, father_age: int) -> int | None:
    years = 0
    while father_age > 2 * child_age:
        years += 1
        child_age += 1
        father_age += 1
    if father_age == 2 * child_age:
        return years
    else:
        return None

def main():
    try:
        age = int(input("How old are you: "))
        father_age = int(input("How old is your father: "))
        if age < 0 or father_age < 0 or father_age <= age:
            print("Please enter valid ages (father must be older).")
            return
        years = years_until_double_age(age, father_age)
        if years is None:
            print("The situation is no longer possible for your ages")
        elif years == 0:
            print("Your father is already twice your age!")
        else:
            print(f"Within {years} years your father will have twice your age")
            print(f"Your father will be {father_age + years} and you will be {age + years}")
    except ValueError:
        print("Please enter valid integer ages.")

if __name__ == "__main__":
    main()