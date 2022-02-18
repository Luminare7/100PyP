from turtle import Turtle

TEXT_OVER = "GAME OVER"
TEXT_WIN = "YOU WON"
TEXT_X = 0
TEXT_Y = 0
ALIGNMENT = "center"
FONT = ('Courier', 50, 'italic')


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=TEXT_X, y=TEXT_Y)
        self.speed("fastest")

    def write_gameover(self):
        self.write(arg=TEXT_OVER, align=ALIGNMENT, font=FONT)

    def write_win(self):
        self.write(arg=TEXT_WIN, align=ALIGNMENT, font=FONT)
