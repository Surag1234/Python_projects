from turtle import Turtle
import random

START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car:

    def __init__(self):
        self.all_cars = []
        self.car_speed = START_MOVE_DISTANCE

    def create_cars(self):
        random_time = random.randint(1, 6)
        if random_time == 1:
            new_car = Turtle("square")
            new_car.clear()
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-220, 220)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
