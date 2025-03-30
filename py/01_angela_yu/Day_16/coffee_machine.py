from decimal import Decimal
from operator import attrgetter
from typing import Tuple
from coffee import Coffee
from coins import Coins


class CoffeeMachine:
    def __init__(self, coffee_req: list[Coffee], water: int, milk: int, coffee: int, money: Decimal):
        self.coffee_req = self.create_dict(coffee_req)
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def create_dict(self, coffee_req: list[Coffee]) -> dict[str, Coffee]:
        coffee_dict = {}
        for coffee in coffee_req:
            coffee_dict[coffee.type] = coffee

        return coffee_dict

    def check_resources(self, coffee_type: str) -> bool:
        if not coffee_type in self.coffee_req:
            return False

        milk, water, coffee = attrgetter(
            'milk', 'water', 'coffee')(self.coffee_req[coffee_type])
        return self.milk >= milk and self.water >= water and self.coffee >= coffee

    def consume_resources(self, total: Decimal, coffee_type: str) -> bool:

        coffee_req = self.coffee_req[coffee_type]

        if coffee_req.money > total:
            return False

        self.water -= coffee_req.water
        self.milk -= coffee_req.milk
        self.coffee -= coffee_req.coffee
        self.money += coffee_req.money

        return True

    def dispense_coffee_and_return_change(self, coins: dict[str, int], coffee_type: str) -> Tuple[bool, Decimal]:
        quarter = coins[Coins.Quarter.name]*Coins.Quarter.value
        dime = coins[Coins.Dime.name]*Coins.Dime.value
        nickel = coins[Coins.Nickel.name]*Coins.Nickel.value
        penny = coins[Coins.Penny.name]*Coins.Penny.value
        total = Decimal(quarter + dime + nickel + penny)

        is_money_enough = self.consume_resources(total, coffee_type)

        if not is_money_enough:
            return (False, total)
        return (True, total - self.coffee_req[coffee_type].money)

    def print_report(self) -> None:
        print(self)

    def __str__(self) -> str:
        return (f'''
            Water: {self.water}ml
            Milk: {self.milk}ml
            Coffee: {self.coffee}g
            Money: ${self.money}
        ''')
