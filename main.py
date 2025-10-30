from turtle import Screen, Turtle
from snake import Snake, Treat
import random
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("#594f4f")
screen.title("My Snake Game")
screen.tracer(0)
turtle = Turtle()
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
treat = Treat()
score = 0
scoreboard = f"Score: {score}"

while game_is_on:
    turtle.write(scoreboard)
    screen.update()
    time.sleep(0.15)
    snake.move()
    if abs(snake.head.xcor()) > 295 or abs(snake.head.ycor()) > 295:
        game_is_on = False
    if abs(treat.treat.xcor() - snake.head.xcor()) <20 and abs(treat.treat.ycor() - snake.head.ycor()) <20:
        score += 1
        treat.new_treat()



#treat color = "#ff4e50"












screen.exitonclick()
