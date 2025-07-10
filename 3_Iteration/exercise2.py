"""
num = int(input("Enter a number: "))
zeros = sixes = 0

for i in range(len(str(num))):
    if num % 10 == 6:
        sixes += 1
    elif num % 10 == 0:
        zeros += 1
    num //= 10

print(f"The number consists of {zeros} zeros and {sixes} sixes")
"""

# Advanced mode

def count_zeros_and_sixes(number):
    zeros = sixes = 0
    for digit in str(number):
        if digit == '0':
            zeros += 1
        elif digit == '6':
            sixes += 1
    return zeros, sixes

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        zeros, sixes = count_zeros_and_sixes(num)
        print(f"The number consists of {zeros} zeros and {sixes} sixes")
    except ValueError:
        print("Please enter a valid integer.")