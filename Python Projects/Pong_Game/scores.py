from turtle import Turtle
import csv


class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score_l = 0
        self.score_r = 0
        self.update()



    def update(self):

        self.clear()
        self.goto(100, 200)
        self.write(f"{self.score_r}", False, align="center", font=("bit5x3", 90, "bold"))
        self.goto(-80, 200)
        self.write(f"{self.score_l}", False, align="center", font=("bit5x3", 90, "bold"))

    def increase_l(self):

        self.score_l += 1
        self.update()

    def increase_r(self):

        self.score_r += 1
        self.update()

    def win_l(self):
        self.goto(-200, 100)
        self.write("Win", False, align="center", font=("PIXY", 90, "normal"))

    def win_r(self):
        self.goto(200, 100)
        self.write("Win", False, align="center", font=("PIXY", 90, "normal"))


class PongLine(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, -290)
        self.pendown()
        self.color('white')
        self.setheading(90)
        self.draw_line()

    def draw_line(self):

        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)

        for _ in range(24):

            self.stamp()
            self.forward(30)
