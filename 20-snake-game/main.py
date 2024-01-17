from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Initialize screen with basic properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initializing the snake
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Listening to the keyboard strokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detection collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail - if head collides any segment with the tail
    for segment in snake.segments[1:]:  # run through all the segments except head (index 0)
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Close the screen on the click
screen.exitonclick()
