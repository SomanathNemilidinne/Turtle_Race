from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -100, -50, 0, 50, 100]
all_turtles = []
for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[index])
    tim.penup()
    tim.goto(x=-280, y=y_positions[index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
