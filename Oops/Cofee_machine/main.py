from asyncio.windows_events import NULL
from random import choice

from fontTools.misc.cython import returns

from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_working = True

money = MoneyMachine()
cofee = CoffeeMaker()

menu = Menu()
# choice = "cappuccino"
# menu_item = menu.find_drink(choice)
# print(menu_item.name)
def generate_report():
    print(cofee.report())
    print(money.report())



while is_working:

    choice = input(f"Enter you choice {menu.get_items()} ")
    if choice == "report":
        generate_report()

    elif choice == "off":
        is_working = False
    else:
        menu_item = menu.find_drink(choice)
        if menu_item == NULL:
            print("Entered item is not available...!")
            is_working = False
        else:
            if cofee.is_resource_sufficient(menu_item) and money.make_payment(menu_item.cost):
                cofee.make_coffee(menu_item)







