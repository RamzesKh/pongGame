import turtle
from turtle import Turtle



class Paddle:
    def __init__(self, position_X,position_Y):
        self.paddle = Turtle("square")
        self.paddle.goto(position_X, position_Y)
        self.paddle.setheading(90)
        self.paddle.penup()
        self.paddle.shapesize(stretch_len=5, stretch_wid=1)
        self.paddle.color("white")

    def moveUp(self):
        self.paddle.forward(50)

    def moveDown(self):
        self.paddle.backward(50)


