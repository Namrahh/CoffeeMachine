from turtle import Screen
from make_coffee import MakeCoffee
from money import Money
import time

screen = Screen()
screen.setup(700, 700)
# screen.bgpic("coffee-bg.png")
screen.title("Coffe Wending Machine")
screen.tracer(0)

coffee = MakeCoffee()
money = Money()

user_coffee = screen.textinput("Coffee Type", "What would you like to have (Espresso/Latte/Cappucino)? ").lower()

while user_coffee != "off":
    screen.update()
    if user_coffee == "report":
        coffee.gen_report()

    # Check resources for user coffee
    else:
        coffee.check_resources(user_coffee)
        if coffee.resources:  # if we have enough resources, ask the user for money
            quarters = int(screen.textinput("Quarters: ", "Please enter your quarters"))
            dimes = int(screen.textinput("Dimes: ", "Please enter your dimes"))
            nickles = int(screen.textinput("Nickles: ", "Please enter your nickles"))
            pennies = int(screen.textinput("Pennies: ", "Please enter your pennies"))
            total_money = (round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2))
            money.user_transaction(user_coffee, total_money)
            if money.transaction:
                coffee.make_coffee(user_coffee)

    user_coffee = screen.textinput("Coffee Type", "What would you like to have (Espresso/Latte/Cappucino)? ").lower()

screen.exitonclick()
