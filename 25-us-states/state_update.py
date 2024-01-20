from turtle import Turtle

FONT = ("Courier", 20, "normal")


class UpdateState(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def update_state(self, x, y, text):
        self.goto(x, y)
        self.write(text, align="center", font=FONT)
