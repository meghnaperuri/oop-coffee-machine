from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
# espresso = MenuItem("e",50,100,25,3)
# latte = MenuItem("l",55,110,20,2)
# cappuccino = MenuItem("c",60,120,15,4)
# print(cappuccino.cost)
# print(latte.name)
# print(espresso.ingredients["water"])

choice=input("welcome! what do you want to have? "+menu.get_items())
selectedItem=menu.find_drink(choice)
print(selectedItem.name)
coffee_maker.report()
# coffee_maker.is_resource_sufficient(choice)
# print(coffee_maker.make_coffee(choice))
money_machine.report()
money_machine.make_payment(10)