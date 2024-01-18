import time
import turtle
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle(350,0)
paddle_l = Paddle(-350,0)


ball = Ball()
screen.listen()
screen.onkey(paddle_r.moveUp,"Up")
screen.onkey(paddle_r.moveDown,"Down")

screen.onkey(paddle_l.moveUp,"w")
screen.onkey(paddle_l.moveDown,"s")

scoreBoard_left = ScoreBoard(-100,200)
scoreBoard_right = ScoreBoard(100,200)
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    print(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle_r.paddle) < 50 and ball.xcor() > 320 or  ball.distance(paddle_l.paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360 :
        scoreBoard_left.update()
        ball.reset()
    elif ball.xcor() < -380:
        scoreBoard_right.update()
        ball.reset()





screen.exitonclick()