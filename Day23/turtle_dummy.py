from turtle import Turtle

STEP_SIZE = 20


class Dummy(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(0, -280)

    def step_up(self):
        self.forward(STEP_SIZE)
