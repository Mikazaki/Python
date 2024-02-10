from turtle import Turtle
import random


class Balls(Turtle):
    def __init__(self):
        super().__init__()
        self.ball()
        self.is_touching_paddle = False

    def ball(self):
        self.penup()
        self.shape('square')
        self.goto(0, 0)
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color('white')
        self.dy = 4
        self.dx = 4

    def move(self):
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        self.goto(x, y)

    def check_paddle_collision(self, paddle):
        if self.distance(paddle) < 30 and abs(self.xcor() - paddle.xcor()) < 30:
            self.is_touching_paddle = True

    def bounce(self, direction):
        if direction == "right":
            self.dx = -(abs(self.dx))
        elif direction == "left":
            self.dx = abs(self.dx)
        self.is_touching_paddle = False

    def respawn(self):
        y = random.randint(-230, 230)
        self.goto(0, y)
        self.dx *= -1
        self.dx = 4