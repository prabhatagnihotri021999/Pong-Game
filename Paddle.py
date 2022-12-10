from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.shapesize(3, 1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_x = self.ycor() + 20
        self.goto(self.xcor(), new_x)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
