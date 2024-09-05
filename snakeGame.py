from turtle import Turtle, Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True

screen.listen()
screen.onkey(fun = snake.up, key="Up")
screen.onkey(fun = snake.down, key="Down")
screen.onkey(fun = snake.turn_right, key="Right")
screen.onkey(fun = snake.turn_left, key="Left")


while game_is_on:
    screen.update()
    sleep(.2) #stops execution for .2 seconds, and in other words it adds a gap of .2 in the loop
    snake.move()


screen.exitonclick()