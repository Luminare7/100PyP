from turtle import Turtle

SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed_x = SPEED
        self.speed_y = SPEED
        self.move_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.speed_x
        new_y = self.ycor() + self.speed_y # * 3 / 4
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.speed_y *= -1

    def bounce_x(self):
        self.speed_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

