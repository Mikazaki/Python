from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.penup()
        self.car_list = []
        self.car()
        self.move()

    def car(self):

        if random.randint(1, 2) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))

            y = random.choice([-245, -215, -155, -125, -95, -35, -5, 25, 85, 115, 145, 205, 235])
            new_car.goto(280, y)
            self.car_list.append(new_car)

    def move(self):

        for car in self.car_list:

            car.forward(STARTING_MOVE_DISTANCE)

            if car.xcor() < -300:
                car.hideturtle()
                self.car_list.remove(car)

    def increase(self):

        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
