import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
game_paused = False

# -------- Controls --------
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

def toggle_pause():
    global game_paused
    game_paused = not game_paused

screen.onkeypress(toggle_pause, "p")

# -------- Game Loop --------
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    if game_paused:
        continue

    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Paddle collision (right)
    if (
        ball.xcor() > 320
        and ball.distance(r_paddle) < 50
        and ball.x_move > 0
    ):
        ball.x_bounce()
        ball.goto(320, ball.ycor())

    # Paddle collision (left)
    if (
        ball.xcor() < -320
        and ball.distance(l_paddle) < 50
        and ball.x_move < 0
    ):
        ball.x_bounce()
        ball.goto(-320, ball.ycor())

    # Right miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_ball()

    # Left miss
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_ball()

screen.exitonclick()
