from turtle import Turtle
import random

FOOD_SHAPE = 'circle'
FOOD_COLOR = 'green'


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()  # Does not draw line
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Draw smaller, half the standard size
        self.color(FOOD_COLOR)
        self.speed('fastest')  # Shows no animation

        # Place the food randomly on the screen
        self.refresh()

    def refresh(self):
        """
        Place a food randomly on the screen
        """
        random_x = random.randint(-280, 280)  # Screen width / 2 - food width = 280
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
