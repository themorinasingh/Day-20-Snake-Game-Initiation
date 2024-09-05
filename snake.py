from turtle import Turtle, Screen

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in positions:
            new_segment = Turtle("circle")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake_body.append(new_segment)

    def move(self):
        for i in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[i -1].xcor()
            new_y = self.snake_body[i -1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(move_distance)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


