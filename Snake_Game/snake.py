from turtle import Turtle, Screen

MOVE_DISTANCE = 20
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
screen = Screen()

color = screen.textinput(title='Color of Snake', prompt="What color of snake do you want:"
                                                        "\nBlue"
                                                        "\nRed"
                                                        "\nWhite"
                                                        "\nPurple"
                                                        "\nCyan"
                                                        "\nGold"
                                                        "\nGreen"
                                                        "\nYellow")


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.current_direction = 0

    def create_snake(self):

        for snake in START_POSITION:

            self.add_parts(snake)

    def add_parts(self, snake):

        turt = Turtle(shape="square")
        turt.penup()
        turt.color(color)
        turt.setposition(snake)
        self.segment.append(turt)

    def grow(self):

        last_segment = self.segment[-1]
        self.add_parts((last_segment.xcor(), last_segment.ycor()))

    def move(self):

        for parts in range(len(self.segment) - 1, 0, -1):

            new_x = self.segment[parts - 1].xcor()
            new_y = self.segment[parts - 1].ycor()
            self.segment[parts].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):

        if self.current_direction != 270:

            self.current_direction = 90
            self.head.setheading(self.current_direction)

    def down(self):

        if self.current_direction != 90:

            self.current_direction = 270
            self.head.setheading(self.current_direction)

    def right(self):

        if self.current_direction != 180:

            self.current_direction = 0
            self.head.setheading(self.current_direction)

    def left(self):

        if self.current_direction != 0:

            self.current_direction = 180
            self.head.setheading(self.current_direction)
