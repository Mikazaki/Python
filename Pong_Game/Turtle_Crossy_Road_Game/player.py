from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):

        super().__init__()
        self.penup()
        self.turt()

    def turt(self):

        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape('turtle')
        self.color('DarkGreen')

    def move(self):

        if self.ycor() < 280:
            self.forward(MOVE_DISTANCE)


class Line(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(280, -260)
        self.setheading(180)
        self.draw_line()
        self.grass()

    def draw_line(self):

        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=0.4, stretch_wid=0.1)

        for j in range(18):

            self.goto(280, -260 + j * (20 + 10))
            for i in range(20):

                self.stamp()
                self.forward(30)

    def grass(self):

        square_width = 21
        self.penup()
        self.shape('square')
        self.color('#59A608')
        self.setheading(180)
        self.shapesize(stretch_len=1.2, stretch_wid=1)

        y = [-185, -65, 55, 175]

        for j in y:

            self.goto(280, j)
            for i in range(28):

                self.stamp()
                self.forward(square_width)
