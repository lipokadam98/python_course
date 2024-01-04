import random
import turtle as t
from turtle import Turtle

tim = Turtle()

tim.shape("turtle")

tim.width(10)
tim.speed("fastest")
for i in range(1000):
    rand_int = random.randint(1, 4)

    match rand_int:
        case 1:
            tim.color("gold")
            tim.forward(20)
        case 2:
            tim.color("aqua")
            tim.backward(20)
        case 4:
            tim.color("coral2")
            tim.left(90)
            tim.forward(20)
        case 4:
            tim.color("yellow")
            tim.right(90)
            tim.forward(20)

screen = t.Screen()
screen.exitonclick()
