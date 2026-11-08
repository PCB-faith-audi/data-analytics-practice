daily_sales = [1200, 950, 1800, 1430, 2100, 3000, 2750]
avg = sum(daily_sales)/ len(daily_sales)
print(f"Average;KES{avg:,.0f}")

for day,sale in enumerate(daily_sales, start=1):
    if sale > avg:
        label = "Above average"
    elif sale == avg:
        label = "Average"
    else:
        label = "Below average"

print(f"Day [day]: Kes{sale:,} -> {label}")

# while loop
balance = 20000
month = 0
while balance < 25000:
    balance = balance * 1.05 # 5% growth per month
    month += 1
print(f"Target reached in {month} months: KES{balance:,.2f}")