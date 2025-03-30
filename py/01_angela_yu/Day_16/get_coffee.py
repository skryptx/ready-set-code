from decimal import Decimal
from coffee_machine import CoffeeMachine
from coffee import Coffee
from coins import Coins


def get_coffee(coffee_machine: CoffeeMachine) -> None:
    machine_off = False

    while not machine_off:
        user_input = str.capitalize(input(
            "What would you like? ((espresso/latte/cappuccino): "))

        if user_input == "Report":
            coffee_machine.print_report()
            continue

        if user_input == "Off":
            machine_off = True
            continue

        is_resources_available = coffee_machine.check_resources(user_input)

        if not is_resources_available:
            print("Sorry there is not enough resources")
            break

        print("Please insert coins:")
        coins: dict[str, int] = {}
        coins[Coins.Quarter.name] = int(input("quarter: "))
        coins[Coins.Dime.name] = int(input("dime: "))
        coins[Coins.Nickel.name] = int(input("nickel: "))
        coins[Coins.Penny.name] = int(input("penny: "))

        is_dispensed, change = coffee_machine.dispense_coffee_and_return_change(
            coins, user_input)
        if not is_dispensed:
            print("Sorry that's not enough money. Money refunded.")
            return

        print(f"Here is ${round(change, 2)} in change")


def prepare_machine() -> CoffeeMachine:
    return CoffeeMachine([
        Coffee("Espresso", 50, 5, 25, Decimal(5)),
        Coffee("Cappuccino", 40, 15, 15, Decimal(4)),
        Coffee("Latte", 50, 60, 5, Decimal(7))], 100, 100, 100, Decimal(5)
    )


coffee_machine = prepare_machine()
get_coffee(coffee_machine)
