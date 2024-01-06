import random
import turtle as t
from turtle import Turtle


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spiral(gap: int):
    for i in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


tim = Turtle()
t.colormode(255)
tim.shape("turtle")

tim.width(2)
tim.speed("fastest")

draw_spiral(1)

screen = t.Screen()
screen.exitonclick()
