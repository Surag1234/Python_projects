from turtle import Screen
import time
from player import Player
from car import Car
from score import Score

S = Screen()
S.bgcolor("white")
S.screensize(600, 600)
S.tracer(0)
S.title("Car Crossing")

game_is_on = True

player = Player()
car = Car()
score = Score()

S.listen()
S.onkey(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    S.update()

    car.create_cars()
    car.move_car()

    # detect collision with car

    for i in car.all_cars:
        if i.distance(player) < 25:
            score.game_over()
            game_is_on = False

    # detect the end

    if player.is_at_finish_line():
        player.restart()
        car.level_up()
        score.update_level()

S.exitonclick()
