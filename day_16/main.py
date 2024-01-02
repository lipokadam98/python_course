import turtle
from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("chartreuse")
timmy.forward(100)
timmy.tilt(90)
timmy.forward(100)
my_screen = Screen()
my_screen.setup(width=600, height=600)
print(my_screen.canvheight)
my_screen.exitonclick()

turtle.forward(100)
