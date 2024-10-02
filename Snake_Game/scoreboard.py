from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")



class Scoreboard(Turtle):



    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0


    def scores(self):
        self.clear()
        self.pendown()
        self.write(f"Score: {self.score} High Score: {self.highscore}", font=FONT, align=ALIGNMENT)
