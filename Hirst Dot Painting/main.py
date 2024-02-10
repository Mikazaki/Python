from turtle import Turtle, Screen
import random

color = [(211, 154, 97), (52, 108, 132), (177, 78, 33), (201, 142, 33), (116, 155, 171), (123, 80, 98), (123, 175, 157),
         (233, 239, 243), (228, 197, 128), (192, 87, 107), (54, 38, 19), (11, 50, 64), (47, 168, 124), (193, 123, 143),
         (52, 122, 117), (166, 22, 30), (224, 93, 79), (7, 31, 29), (37, 32, 34), (243, 164, 160), (80, 148, 169),
         (163, 26, 22), (240, 164, 167), (174, 207, 187), (105, 124, 159), (21, 79, 90), (162, 204, 212)]

turt = Turtle()
screen = Screen()
turt.hideturtle()
turt.penup()
turt.setposition(-200, -200)
turt.speed(8)
screen.colormode(255)


def random_color():
    return random.choice(color)


for j in range(10):
    for i in range(10):
        turt.dot(20, random_color())
        turt.forward(50)
    turt.backward(500)
    turt.left(90)
    turt.forward(50)
    turt.right(90)

screen.exitonclick()
