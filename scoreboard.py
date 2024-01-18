
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, x,y):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x,y)
        self.write(self.score,align="center", font=("Courier", 80, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(self.score,align="center", font=("Courier", 80, "normal"))