from turtle import Turtle
from random import randint, choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.setheading(choice([choice([randint(0, 45), randint(315,360)]), randint(135, 225)]))
        self.move_speed = 20

    def move(self):
        self.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += 2

    def reset_speed(self):
        self.move_speed = 20

    def change_direction(self):
        current_heading = self.heading()
        if 180 > current_heading >= 0:
            self.setheading(270+(90-current_heading))
            self.forward(self.move_speed)
        else:
            self.setheading(90+(270-current_heading))
            self.forward(self.move_speed)

    def bounce_paddle(self):
        current_heading = self.heading()
        if 90 > current_heading >= 270:
            self.setheading(180 + (360 - current_heading))
            self.forward(self.move_speed)
        else:
            self.setheading(180 - (360 + current_heading))
            self.forward(self.move_speed)

    def reset_position(self):
        self.goto(0, 0)
        self.setheading(choice([choice([randint(0, 45), randint(315,360)]), randint(135, 225)]))
