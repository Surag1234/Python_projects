from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.65, stretch_len=.65)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        r_x = random.randint(-280, 280)
        r_y = random.randint(-280, 280)
        self.goto(r_x, r_y)
