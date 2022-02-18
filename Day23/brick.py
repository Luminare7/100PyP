from turtle import Turtle
import random

COLORS = ["green", "blue", "gold", "red", "orange", "brown"]


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_x = random.randint(-300, 300)
        self.initial_y = random.randint(-240, 260)
        self.brick_speed = random.randint(2, 8)
        self.create_brick()

    def create_brick(self):
        self.hideturtle()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(self.initial_x, self.initial_y)
        self.showturtle()

    def move_left(self):
        new_x = self.xcor() - self.brick_speed
        if new_x <= -300:
            new_x += 600
        self.goto(new_x, self.ycor())

