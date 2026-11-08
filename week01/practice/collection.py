# Lists
daily_sales = [1200, 950, 1800, 1430, 2100, 3000, 2750]

print(len(daily_sales))
print(sum(daily_sales))
print(max(daily_sales), min(daily_sales))
print(daily_sales[0], daily_sales[-1])
print(daily_sales[1:4])

daily_sales.append(1650) #add an item to the end
print(len(daily_sales))

# Dictionary
product = {"name": "Juice","price": 120, "stock": 30}
print(product["name"])
product["states"] = product["stock"] - 4 #4 bottles sold
print(product)

coordinates = (-1.2921, 39.897) # tuple:fixed
states = ["USA", "Los_Angels", "USA", "Washington_D.C","La_Vegas"]
print(len(states), len(set(states))) # total vs unique