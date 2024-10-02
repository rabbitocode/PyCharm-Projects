from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20







class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        self.color("green")
        self.FINISH_LINE_Y = 280
        self.move_speed = 0.1

    def MoveUP(self):
        self.forward(MOVE_DISTANCE)


    def LevelUp(self):
        self.goto(STARTING_POSITION)
        self.move_speed *= 0.8

