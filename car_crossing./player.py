from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POS = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POS)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
