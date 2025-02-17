total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? $"))
people_count = float(input("How many people to split the bill? "))

result = round((total_bill+tip*total_bill/100)/people_count, 2)
print("Each person should pay: " + str(result))
