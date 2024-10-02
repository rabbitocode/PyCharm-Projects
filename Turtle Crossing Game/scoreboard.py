FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.score = 0
        self.pencolor("black")
        self.penup()
        self.goto(-230, 250)

    def GameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def UpdateScore(self):
        self.score += 1

    def Scores(self):
        self.clear()
        self.write(f"Level:{self.score}", font=FONT, align=ALIGNMENT)