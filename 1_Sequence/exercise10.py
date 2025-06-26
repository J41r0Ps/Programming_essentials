fixed_annual_amount = 83.6
amount_night = 0.073
amount_day = 0.146
vat = 0.06

power_consumption_day = int(input("Power consumption during the day (kilowatt per hour): "))
power_consumption_night = int(input("Power consumption at night (kilowatt per hour): "))

print(f"Invoice")
print("*" * len("Invoice"))
print(f"Fixed costs: €{fixed_annual_amount}")
print(f"Daily consumption: €{power_consumption_day * amount_day}")
print(f"Night consumption: €{power_consumption_night * amount_night}")
print(f"Total excluding VAT: €{(power_consumption_day * amount_day) + (power_consumption_night * amount_night)}")
print(f"Total including VAT: €{((power_consumption_day * amount_day) + (power_consumption_night * amount_night))* vat}")