import time
from turtle import Turtle,Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
snake.move()
screen.listen()
screen.onkey(key="Up",fun=snake.snake_up)
screen.onkey(key="Left",fun=snake.snake_left)
screen.onkey(key="Right",fun=snake.snake_right)
screen.onkey(key="Down",fun=snake.snake_down)
food = Food()
score = Scoreboard()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #### Collison with food
    if snake.head.distance(food) < 15:
        score.increment_score()
        snake.increase_size()
        food.refresh()


    ### Colison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    ### Collison with tail
    for segment in snake.snake[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 5:
            score.reset()
            snake.reset()

screen.exitonclick()