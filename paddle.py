from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 40
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.seth(UP)
        self.goto(position)

    def up(self):
        self.seth(UP)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.seth(DOWN)
        self.forward(MOVE_DISTANCE)



