import random
from turtle import Turtle, Screen
from typing import List

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Turtle Race", prompt="Bet on a turtle. Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def check_winner(turtle: Turtle):
    return turtle.xcor() >= 125


def create_turtles():
    y_pos = -100
    turtles: List[Turtle] = []
    for color in colors:
        turtle = Turtle("turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-230, y=y_pos)
        y_pos = y_pos + 50
        turtles.append(turtle)

    return turtles


def race(turtles: List[Turtle]):
    has_winner = False

    while not has_winner:
        for turtle in turtles:
            if check_winner(turtle):
                has_winner = True
                if user_bet == turtle.pencolor():
                    print(f"You won with the color of {turtle.pencolor()}!")
                else:
                    print(f"You lost against the color of {turtle.pencolor()}!")

                screen.bye()
                break
            turtle.forward(random.randint(5, 10))


turtle_list = create_turtles()

race(turtle_list)
