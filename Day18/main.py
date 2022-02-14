# Welcome to day 18!!

from turtle import Turtle, Screen
import random
import colorgram

Width, Height = 650, 650
Screen().setworldcoordinates(-20, -20,  Width, Height )

colors = colorgram.extract('hirst_spots.jpg', 30)
colors_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = (r, g, b)
    colors_list.append(color_tuple)

used_colors = colors_list[4:]

tim = Turtle()
Screen().colormode(255)

tim.hideturtle()
tim.penup()


def draw_dot_line():
    dot_color = random.choice(used_colors)
    tim.dot(20, dot_color)
    tim.forward(70)
    x_pos = tim.pos()[0]


def move_up():
    step = 70
    y_pos = (tim.pos()[1] + step)
    tim.goto(0, y_pos)


while tim.pos()[1] <= 630:
    while tim.pos()[0] <= 630:
        draw_dot_line()
    move_up()

print(tim.position()[0])
print(tim.position()[1])

Screen().exitonclick()
