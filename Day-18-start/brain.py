from turtle import Turtle
import random




timmy = Turtle()
timmy.shape("turtle")

# Hides timmy
timmy.hideturtle()
class Brain:


    def __init__(self):
        self.degrees = 360




    def shape_calculate_run(self, number_of_corners):
        corners = self.degrees / number_of_corners
        print(corners)

        colorlist = ['red', 'orange', 'yellow', 'green', 'blue',
                     'purple', 'pink', 'brown', 'chocolate', 'gold', 'AliceBlue', 'cyan', 'DarkViolet',
                     'azure', 'brown4', 'beige', 'DarkOrchid', 'DarkGray']
        randomnr = random.randint(0, len(colorlist) - 1)
        randomcolor = colorlist[randomnr]

        timmy.color(randomcolor)

        for x in range(number_of_corners):
            timmy.fd(100)
            timmy.right(corners)