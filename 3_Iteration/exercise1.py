"""
product_number = int(input("Enter a number, stop by entering a zero: "))
number = 1
counter = 0

while product_number != 0:
    number *= product_number
    counter += 1
    product_number = int(input("Enter a number, stop by entering a zero: "))

print(f"The product of the {counter} numbers is {number}")
"""

# Advanced mode

def calculate_product():
    product = 1
    count = 1

    try:
        num = int(input("Enter a number, stop by entering a zero: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    while num != 0:
        product *= num
        count += 1
        try:
            num = int(input("Enter a number, stop by entering a zero: "))
        except ValueError:
            print("Please enter a valid integer.")
            num = 0
    print(f"The product of the {count} numbers is {product}")

if __name__ == "__main__":
    calculate_product()