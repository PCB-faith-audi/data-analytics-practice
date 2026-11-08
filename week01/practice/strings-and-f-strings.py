region = "Asia"
large = region.strip().title()

print(large)

print(large.upper(),len(large))

print("Asi" in large)

gross_profit = 50000
expenses = 20000
name = "Kilonzo"
net_income = gross_profit - expenses
print(f"{name} made KES {net_income:,.2f} today")