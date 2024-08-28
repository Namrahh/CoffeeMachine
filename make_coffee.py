from turtle import Turtle, Screen
import ingredients
import time


class MakeCoffee(Turtle):
    def __init__(self):
        super().__init__()
        self.resources = False
        self.hideturtle()
        self.penup()

    def gen_report(self):
        Water = ingredients.resources['water']
        Milk = ingredients.resources['milk']
        Coffee = ingredients.resources['coffee']
        self.write(f"Water = {Water} ml\nMilk = {Milk} ml\nCoffee = {Coffee} g", False, align="center",
                   font=("Courier", 20, "bold"))

    def check_resources(self, user_drink):
        self.clear()
        drink_ingredients = ingredients.MENU[user_drink]['ingredients']
        for key in drink_ingredients:
            if ingredients.resources[key] < drink_ingredients[key]:
                self.write(f"sorry there is not enough {key}", False, align="center",
                           font=("Courier", 20, "bold"))
                self.resources = False
            else:
                self.write(f"Getting your coffee ready..", False, align="center",
                           font=("Courier", 15, "bold"))
                self.resources = True

    def make_coffee(self, user_drink):
        self.clear()
        drink_resources = ingredients.MENU[user_drink]['ingredients']
        for key in drink_resources:
            ingredients.resources[key] -= drink_resources[key]
        self.write(f"Here is your {user_drink}. Enjoy!", False, align="center",
                   font=("Courier", 15, "bold"))