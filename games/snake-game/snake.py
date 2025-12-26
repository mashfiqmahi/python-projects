from turtle import Turtle



UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
starting_position = [(0,0), (-20,0), (-40,0)]
class Snake:
    def __init__(self):
        self.snake = []
        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.speed("fastest")
            self.snake.append(new_segment)
        self.head = self.snake[0]

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(10)


    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
        for segment in self.snake:
            segment.goto(1000,1000)
        self.snake.clear()
        self.__init__()
    def increase_size(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.snake[-1].position())
        self.snake.append(new_segment)