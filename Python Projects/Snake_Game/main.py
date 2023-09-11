from turtle import Screen
from snake import Snake
from banana import Banana
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
player_name = screen.textinput(title="Player Name", prompt="Enter your name to display your scores in "
                                                           "leaderboard: ")

snake = Snake()
food = Banana()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game = True

while game:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Collision

    if snake.head.distance(food) < 14:

        food.relocate()
        snake.grow()
        score.increase()

    # Wall collision
    if snake.head.xcor() > 293 or snake.head.xcor() < -293 or snake.head.ycor() > 293 or snake.head.ycor() < -293:

        game = False
        score.name = player_name
        score.save_score_to_csv()
        score.display_leaderboard()
        score.game_over()

    # Tail Collision
    for segments in snake.segment[1:]:

        if snake.head.distance(segments) < 14:
            game = False
            score.name = player_name
            score.save_score_to_csv()
            score.display_leaderboard()
            score.game_over()

screen.exitonclick()
