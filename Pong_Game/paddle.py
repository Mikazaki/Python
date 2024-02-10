from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):

        super().__init__()
        self.paddle(x)
        self.move_speed = 10
        self.move_interval = 16
        self.moving_up = False
        self.moving_down = False

    def paddle(self, x):

        self.penup()
        self.shape('square')
        self.goto(x, 0)
        self.shapesize(stretch_len=0.9, stretch_wid=5)
        self.color('white')

    def start_moving_up(self):

        self.moving_up = True

    def start_moving_down(self):

        self.moving_down = True

    def stop_moving_up(self):

        self.moving_up = False

    def stop_moving_down(self):

        self.moving_down = False

    def update_position(self):

        if self.moving_up:

            y = self.ycor() + self.move_speed

            if y < 255:

                self.goto(self.xcor(), y)

        if self.moving_down:

            y = self.ycor() - self.move_speed

            if y > -245:

                self.goto(self.xcor(), y)

        self.screen.ontimer(self.update_position, self.move_interval)


