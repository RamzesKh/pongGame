from turtle import Turtle


class Wall(Turtle):
    def __init__(self, x, y):
        super().__init__(visible=False)
        self.shape("square")
        self.shapesize(stretch_len=40, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(x, y)