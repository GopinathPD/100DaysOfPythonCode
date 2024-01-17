from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race> Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_y_axis = -100
all_turtles = []

for item in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[item])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=turtle_y_axis)
    turtle_y_axis += 30
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
