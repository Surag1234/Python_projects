from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score


S = Screen()
S.setup(800, 600)
S.bgcolor("black")
S.title("Pong")
S.tracer(0)
score = Score()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

S.listen()
S.onkey(r_paddle.go_up, "Up")
S.onkey(r_paddle.go_down, "Down")
S.onkey(l_paddle.go_up, "w")
S.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    S.update()
    ball.move()

    # detect collision on upper wall and lower wall

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with r_paddle

    if ball.distance(r_paddle) < 50 and 320 < ball.xcor() or ball.distance(l_paddle) < 50 and -320 > ball.xcor():
        ball.bounce_x()

    # detect r_paddle miss

    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    # detect l_paddle miss

    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()


S.exitonclick()
