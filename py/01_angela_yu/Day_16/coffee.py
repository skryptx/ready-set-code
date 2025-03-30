from decimal import Decimal


class Coffee:
    def __init__(self, type: str, water: int, milk: int, coffee: int, money: Decimal):
        self.type = type
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
