from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"{self.left_score} : {self.right_score}", align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.clear()
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.clear()
        self.update_score()
