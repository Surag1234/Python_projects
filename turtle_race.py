import turtle
from turtle import Turtle, Screen
import random

is_bet_on = False


colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

S = Screen()
S.setup(width=500, height=400)
user_bet = S.textinput(title="Make your bet", prompt="Which Turtle will win the race?? Enter a color : ")
print(user_bet)

All_turtles = []

for i in range(len(colors)):
    T = Turtle(shape="turtle")
    T.color(colors[i])
    T.penup()
    T.goto(-230, i*20)
    All_turtles.append(T)

if user_bet:
    is_bet_on = True

while is_bet_on:
    for i in All_turtles:
        if i.xcor() > 230:
            is_bet_on = False
            win_color = i.pencolor()
            if win_color == user_bet:
                print("Congo!!!!!!!! You won !!!!!!!!!!!")

            else:
                print(f"You Loose!!!! Winner is {i.pencolor()}")

        rd = random.randint(0,10)
        i.forward(rd)


S.exitonclick()
