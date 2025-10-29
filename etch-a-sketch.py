from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.color("cyan4")
tim.width(10)
# Create etch-a-sketch app: screen listening
def move_up():
    tim.setheading(90)
    tim.forward(10)

def move_down():
    tim.setheading(270)
    tim.forward(10)

def move_left():
    tim.setheading(180)
    tim.forward(10)

def move_right():
    tim.setheading(0)
    tim.forward(10)

def clear_screen():
    tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()

#functions as inputs in other functions, just the name, not the parentheses at the end
# Higher order functions -- functions that can work within other functions. Very useful.
screen.listen()
screen.onkey(key = "Up", fun = move_up)
screen.onkey(key = "Down", fun = move_down)
screen.onkey(key = "Left", fun = move_left)
screen.onkey(key = "Right", fun = move_right)
screen.onkey(key = "c", fun = clear_screen)

screen.exitonclick()