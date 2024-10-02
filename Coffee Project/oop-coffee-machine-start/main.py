from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine








def main():
    menu = Menu()
    coffee = CoffeeMaker()
    money = MoneyMachine()
    is_on = True




    while is_on:
        customer = input(f"What would you like? ({menu.get_items()}): ")
        if customer == "report":
            coffee.report()
            money.report()
        elif customer == "off":
            print("Shutting off")
            is_on = False
        else:
            drink = menu.find_drink(customer)
            if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee.make_coffee(drink)














main()