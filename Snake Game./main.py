from turtle import Screen
import time
from snakes import Snake
from food import Food
from Score import Scoreboard

food = Food()
scoreboard = Scoreboard()

game_is_on = True
S = Screen()
S.tracer(0)
seg = []
snake = Snake()
S.update()

S.setup(width=600, height=600)
S.title("Snakes")
S.bgcolor("black")
S.listen()
S.onkey(snake.up, "Up")
S.onkey(snake.down, "Down")
S.onkey(snake.right, "Right")
S.onkey(snake.left, "Left")

while game_is_on:
    S.update()
    time.sleep(.1)
    snake.move()

    # detect Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with body
    for i in snake.seg:
        if i == snake.head:
            pass

        elif snake.head.distance(i) < 10:
            game_is_on = False
            scoreboard.game_over()

S.exitonclick()
