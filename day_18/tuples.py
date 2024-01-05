import random
import turtle as t
from turtle import Turtle

# Tuples are fix length and fixed type arrays
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(example_tuple)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = Turtle()
t.colormode(255)
tim.shape("turtle")

tim.width(10)
tim.speed("fastest")
for i in range(1000):
    rand_int = random.randint(1, 4)

    match rand_int:
        case 1:
            tim.color(random_color())
            tim.forward(20)
        case 2:
            tim.color(random_color())
            tim.backward(20)
        case 4:
            tim.color(random_color())
            tim.left(90)
            tim.forward(20)
        case 4:
            tim.color(random_color())
            tim.right(90)
            tim.forward(20)

screen = t.Screen()
screen.exitonclick()
