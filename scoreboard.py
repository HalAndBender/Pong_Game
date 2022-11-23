from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'{self.left_score}                         {self.right_score}', align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_right(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()
