from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

SCREEN_COLOR = 'black'

# Not adjustable yet
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

"""
---------------- Setup Game ----------------
"""

# Setup screen

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.bgcolor(SCREEN_COLOR)
screen.title('The Snake Game')

snake = Snake(screen)  # Setup snake
food = Food()  # Setup food
scoreboard = Scoreboard()  # Setup scoreboard

"""
---------------- Run Game ----------------
"""

game_is_on = True


def game_over():
    global game_is_on

    game_is_on = False
    scoreboard.game_over()


while game_is_on:

    time.sleep(0.1)  # control snake move speed
    screen.update()  # refresh the screen
    snake.move()

    # Detect if snake eats a food

    if snake.head.distance(food) < 15:
        # Place another food
        food.refresh()
        # Increase the scoreboard
        scoreboard.increase_score()
        # Increase snake length
        snake.extend()

    # Detect if snake hits walls

    if snake.is_hit_wall():
        game_over()

    # Detect if snake hits its tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # This number is acquired by testing
            game_over()

screen.exitonclick()  # Show screen
