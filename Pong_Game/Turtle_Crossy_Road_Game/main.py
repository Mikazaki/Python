import time
from turtle import Screen
from player import Player, Line
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.bgcolor('gray')
screen.tracer(0)
player_name = screen.textinput(title="Player Name", prompt="Enter your name to display your scores in "
                                                           "leaderboard: ")

player = Player()
line = Line()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()
    car.car()

    # next level

    if player.ycor() == 280:
        score.increase()
        player.goto(0, -280)
        car.increase()

    # game over

    for cars in car.car_list:
        if cars.distance(player) < 23:
            score.game_over()
            score.name = player_name
            score.save_score_to_csv()
            score.display_leaderboard()
            game_is_on = False

screen.exitonclick()
