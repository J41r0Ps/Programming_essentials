amount_wine = int(input("How many bottles of wine are there: "))
amount_pizzas = int(input("How many pizzas are there: "))

if amount_wine >= amount_pizzas * 2 or amount_pizzas >= amount_wine * 2:
    print("This is a fantastic party")
elif amount_pizzas >= 5 and amount_wine >= 5:
    print("This is a good party")
else:
    print("This is just a stupid party")