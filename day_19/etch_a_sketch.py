from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()


screen.listen()

screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
