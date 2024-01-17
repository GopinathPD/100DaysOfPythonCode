from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def rotate_clockwise():
    turtle.setheading(turtle.heading() + 10)


def rotate_counter_clockwise():
    turtle.setheading(turtle.heading() - 10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()

# screen.onkey(key="w", fun=move_forwards)
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_clockwise, "a")
screen.onkey(rotate_counter_clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
