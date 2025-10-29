from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

x_start = 0
segments = []

for i in range(3):
    new_segment = Turtle(shape = "square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(x_start, 0)
    x_start -= 20
    segments.append(new_segment)
screen.update()

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)










screen.exitonclick()