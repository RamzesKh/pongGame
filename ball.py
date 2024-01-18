from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.05
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.goto(0,0)
        self.y_move = 10
        self.x_move = 10

    def move(self):
        self.goto(self.xcor()+self.x_move, self.y_move + self.ycor())

    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.05

