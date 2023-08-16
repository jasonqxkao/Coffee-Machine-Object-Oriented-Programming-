from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
should_continue = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while should_continue:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ").lower()
    if user_input == "off":
        should_continue = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_name = menu.find_drink(user_input)
        resource_sufficiency = coffee_maker.is_resource_sufficient(drink_name)
        if resource_sufficiency:
            if money_machine.make_payment(drink_name.cost):
                coffee_maker.make_coffee(drink_name)







