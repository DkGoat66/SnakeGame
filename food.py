from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()

        # Set up the food appearance and position
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

        # Initialize the food's position by calling the refresh method
        self.refresh()

    def refresh(self):
        # Generate random coordinates within the screen boundaries
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # Move the food to the randomly generated position
        self.goto(random_x, random_y)
