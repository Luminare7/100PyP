# Welcome to Day22! 💪

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.ball_move()

    # Wall collision:
    if pong_ball.ycor() >= 280 or pong_ball.ycor() <= -280:
        pong_ball.bounce_y()

    # Collision with right paddle:
    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    # Detect right paddle miss:
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss:
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
