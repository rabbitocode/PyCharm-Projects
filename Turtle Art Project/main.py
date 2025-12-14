import random

from turtle import *

from brain import Brain
from colorgram import colorgram



tim = Turtle()
tim.shape("turtle")
colormode(255)
tim.speed("fastest")
tim.pensize(2)

brain = Brain()



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def dashed_line():

    for x in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def turn_left():
    tim.left(90)
    tim.forward(60)

def turn_right():
    tim.right(90)
    tim.forward(60)



def draw_square():
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)



#for x in range(3,10):
    #brain.shape_calculate_run(x)



def random_walk(nr_lines):
    for x in range(0,nr_lines):

        tim.color(random_color())

        random_path = random.randrange(1,5)
        if random_path == 1:
            tim.forward(60)
        elif random_path == 2:
            tim.backward(60)
        elif random_path == 3:
            turn_left()
        else:
            turn_right()


def spirograph(gap):

    for x in range(int(360 / gap)):

        tim.color(random_color())

        tim.circle(90)
        tim.setheading(tim.heading() + gap)








# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#
#
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def hirst_row(length_of_row):
    for times in range(0,length_of_row):
        tim.pendown()
        color_choice = random.choice(color_list)
        tim.color(color_choice)
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()


# TODO tp_turtle still a bit broken, y variable not incrementing properly

y = 0
def tp_turtle(height):
    global y
    for x in range (height):
        tim.penup()
        tim.setpos(0,y)
        tim.position()
        y += 3




def hirst_dots(width,height):

    for x in range(width):
        hirst_row(width)
        tp_turtle(height)


hirst_dots(10,10)

tim.hideturtle()

screen = Screen()
screen.exitonclick()

