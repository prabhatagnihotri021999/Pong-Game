from turtle import Turtle, Screen
from Ball import Ball
from Paddle import Paddle
from Paddle_Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

l_paddle = Paddle((-280, 0))
r_paddle = Paddle((280, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.move_up, 'Up')
screen.onkey(l_paddle.move_down, 'Down')
screen.onkey(r_paddle.move_up, 'w')
screen.onkey(r_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 285:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -285:
        ball.reset_position()
        scoreboard.r_point()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 265 or ball.distance(l_paddle) < 50 and ball.xcor() < -265:
        ball.bounce_x()

screen.exitonclick()
