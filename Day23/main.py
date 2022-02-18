# Welcome to Day23!
# Cross, Turtle, Cross! 🐢
import time
from turtle import Screen
from turtle_dummy import Dummy
from brick import Brick
from gameover import GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

brick_list = []

gameover = GameOver()
turtle = Dummy()
for _ in range(0, 15):
    brick_list.append(Brick())

screen.listen()
screen.onkey(fun=turtle.step_up, key="space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for brick in brick_list:
        brick.move_left()
        if brick.ycor() + 10 >= turtle.ycor() >= brick.ycor() - 10 and brick.distance(turtle) < 50:
            game_is_on = False
            gameover.write_gameover()
    if turtle.ycor() >= 300:
        game_is_on = False
        gameover.write_win()

screen.exitonclick()
