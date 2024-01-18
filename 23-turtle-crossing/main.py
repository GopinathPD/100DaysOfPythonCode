import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player
player = Player()

# Listen to the screen
screen.listen()
screen.onkey(player.move, "Up")

# Initialize the Car Manager
cars_manage = CarManager()

# Initialize the scoreboard
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_manage.create_cars()
    cars_manage.move_cars()

    # Detect when the player collides with a car
    for car in cars_manage.all_cars:  # run through all the segments except head (index 0)
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.stop_game()

    # Detect when the player touches the top wall
    if player.is_finish_line():
        cars_manage.increase_speed()
        scoreboard.level_up()
        player.reset_position()


screen.exitonclick()
