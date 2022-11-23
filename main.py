from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
# from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Karlijn's Pong Game")
screen.tracer(0)  # turns off automatic screen updating

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)  # updates the screen every 0.1 seconds
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.change_direction()

#     # Detect collision with paddle
    if ball.xcor() < -335 and ball.distance(l_paddle) < 50:
        ball.bounce_paddle()
        ball.increase_speed()
        scoreboard.increase_score_left()

    if ball.xcor() > 335 and ball.distance(r_paddle) < 50:
        ball.bounce_paddle()
        ball.increase_speed()
        scoreboard.increase_score_right()

    # detect missing the ball
    if ball.xcor() < -400 or ball.xcor() > 400:
        ball.reset_position()
        ball.reset_speed()


screen.exitonclick()
