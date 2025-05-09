print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ").upper()

price_mapping = {"L": 25, "M": 20, "S": 15}
pepperoni_price_mapping = {"L": 3, "M": 3, "S": 2}

price = price_mapping[size]

if pepperoni == "Y":
    price += pepperoni_price_mapping[size]

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}")
