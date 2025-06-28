import math

weight = float(input("Your weight in kilograms: "))
length = int(input("Your length in centimetres: "))

bmi = (weight / math.pow(length,2)) * 10000
print(f"A person of {weight} kg with a length of {length} cm has as BMI {bmi}")

if bmi < 18:
    print("This is underweight")
elif 18 <= bmi < 25:
    print("This is a normal weight")
elif 25 <= bmi < 27:
    print("This is slightly overweight")
elif 27 <= bmi < 30:
    print("This is moderate overweight")
elif 30 <= bmi < 40:
    print("This is obese")
elif 40 >= bmi:
    print("sickly obese")