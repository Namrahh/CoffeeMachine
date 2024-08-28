from turtle import Turtle
import ingredients


class Money(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.transaction = False
        self.goto(0, -20)

    def user_transaction(self, drink_type, user_money):
        self.clear()
        if user_money < ingredients.MENU[drink_type]['cost']:
            self.write(f"Sorry that is not enough money. Money refunded", False, align="center",
                       font=("Courier", 20, "bold"))
            self.transaction = False
        else:
            ingredients.profit += ingredients.MENU[drink_type]['cost']
            if user_money > ingredients.MENU[drink_type]['cost']:
                change = round(user_money - ingredients.MENU[drink_type]['cost'], 2)
                self.write(f"Here is ${change} dollars in change", False, align="center",
                           font=("Courier", 15, "bold"))
                self.transaction = True


