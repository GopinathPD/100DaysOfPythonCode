from turtle_practice import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
screen.colormode(255)


# turtle.shape("classic")


# # Draw a dashed line
# for i in range(10):
#     turtle.forward(5)
#     turtle.penup()
#     turtle.forward(5)
#     turtle.pendown()

# # Draw a triangle
# full_circle_angle = 360
# sides = 3
# side_size = 100
# for _ in range(sides):
#     turtle.forward(side_size)
#     turtle.right(full_circle_angle / sides)
#
# # Draw a square
# sides = 4
# for _ in range(sides):
#     turtle.forward(side_size)
#     turtle.right(full_circle_angle / sides)

# Draw any shape based on size and number of sides
def draw_shape(side):
    full_circle_angle = 360
    move_pixels = 100
    angle = full_circle_angle / side
    for _ in range(side):
        turtle.forward(move_pixels)
        turtle.right(angle)


# Change the color of turtle object
def change_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    turtle.pencolor((R, G, B))


# Choose random direction
def change_direction():
    angles = [90, 180, 270, 360]
    random_direction = random.choice(angles)
    turtle.setheading(random_direction)


# # Draw the Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon
# for sides in range(3, 10):
#     change_color()
#     draw_shape(sides)

# # Draw a Random Walk
# '''The arrow marker moves in random direction for few pixels
# and turn the direction, then moves for few pixels, then turn
# the direction and moves on. This will continue until the user
# breaks the operation. For every new direction movement, it chooses
# random color. Also, the marker should be thicker with faster movement'''
#
# # Increase the turtle speed - fast (0 to 10 --> 6 is normal and 10 is fast)
# turtle.speed(8)
#
# # Increase the thickness of the marker line
# turtle.pensize(15)
#
#
# for _ in range(100):
#     turtle.forward(30)
#     change_color()
#     change_direction()

# # Draw a spirograph
# turtle.speed(0)
# draw_circle = True
# size = 0
#
# while draw_circle:
#     turtle.circle(100)
#     size += 5
#     turtle.setheading(size)
#     change_color()
#     print(turtle.heading())
#     if turtle.heading() == 0.0:
#         draw_circle = False

# move the cursor/marker
def move_forwards():
    turtle.forward(10)


# Screen Listen Methods
screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()

