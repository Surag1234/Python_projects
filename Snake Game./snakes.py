from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]

    def create_snake(self):
        for i in range(3):
            s1 = Turtle(shape="square")
            s1.color("white")
            s1.penup()
            s1.goto(-20 * i, 0)
            self.seg.append(s1)

    def add_segment(self, position):
        s1 = Turtle(shape="square")
        s1.color("white")
        s1.penup()
        s1.goto(position)
        self.seg.append(s1)

    def extend_segment(self):
        self.add_segment(self.seg[-1].position())

    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[i - 1].xcor()
            new_y = self.seg[i - 1].ycor()
            self.seg[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
