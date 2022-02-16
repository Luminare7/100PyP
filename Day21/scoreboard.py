from turtle import Turtle

SCORE_X = 5
SCORE_Y = 270
ALIGNMENT = "center"
FONT = ('Courier', 30, 'italic')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=SCORE_X, y=SCORE_Y)
        self.speed("fastest")
        self.score = 0
        # self.increase_score()
        self.refresh_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()

    def refresh_score(self):
        self.goto(x=SCORE_X, y=SCORE_Y)
        self.pendown()
        self.pencolor("white")
        self.write(arg=f"Total Points: {self.score}", align=ALIGNMENT, font=FONT)
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
