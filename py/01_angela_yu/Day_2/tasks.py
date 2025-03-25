total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people_count = float(input("How many people to split the bill? "))

tip_amount = tip*total_bill/100
actual_total_amount = tip_amount
result = round(actual_total_amount/people_count, 2)
print(f"Each person should pay: ${result}")

