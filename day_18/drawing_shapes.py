import turtle as t
from turtle import Turtle


def draw_shape(size: int, sides: int, angle: float):
    for i in range(sides):
        tim.backward(size)
        tim.left(angle)


tim = Turtle()

tim.shape("turtle")
tim.color("coral2")

for j in range(3, 10):
    draw_shape(100, j, 360 / j)

screen = t.Screen()
screen.exitonclick()
