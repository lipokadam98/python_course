from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_left():
    tim.forward(10)


screen.listen()

# If a function is a parameter we call it a higher order function
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
