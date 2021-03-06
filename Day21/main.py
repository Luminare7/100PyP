# Welcome to Day21!
# Let's finish the snake game:

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()  # The screen refreshes every 0.1 seconds
    time.sleep(0.1)
    snake.move()

    # Check collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for part in snake.body_parts[1:]:
        if snake.head.distance(part) < 10:
            game_is_on: False
            score.game_over()
    # if the head collides with any segment in the tail we lose


screen.exitonclick()
