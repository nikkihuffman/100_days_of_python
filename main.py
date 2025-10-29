# Day 19 - Instances, State and Higher Order Functions

# Turtle Race

from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

is_race_on = False
screen.setup(width =500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_start = -230
y_start = -75
all_turtles = []

#Create different instances of the Turtle class that act and behave differently.
for i in range(6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.speed(0)
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x_start, y_start)
    y_start += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The {winning_color} turtle won! You win!")
            else:
                print(f"The {winning_color} turtle won, but you bet on {user_bet}. Sorry, you lose.")
        else:
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)




screen.exitonclick()