from turtle import Screen
from paddle import Paddle
from balls import Balls
from scores import Score, PongLine

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.delay(0)
screen.tracer(0)

paddle_1 = Paddle(x=370)
paddle_2 = Paddle(x=-370)
balls = Balls()
score = Score()
line = PongLine()

screen.listen()
screen.onkeypress(paddle_1.start_moving_up, "Up")
screen.onkeyrelease(paddle_1.stop_moving_up, "Up")
screen.onkeypress(paddle_1.start_moving_down, "Down")
screen.onkeyrelease(paddle_1.stop_moving_down, "Down")
screen.onkeypress(paddle_2.start_moving_up, "w")
screen.onkeyrelease(paddle_2.stop_moving_up, "w")
screen.onkeypress(paddle_2.start_moving_down, "s")
screen.onkeyrelease(paddle_2.stop_moving_down, "s")

is_game = True


def game():
    global is_game
    screen.update()
    balls.move()
    balls.check_paddle_collision(paddle_1)
    balls.check_paddle_collision(paddle_2)

    # Wall Collision

    if balls.ycor() > 288 or balls.ycor() < -279:
        balls.dy *= -1

    # Paddle Collision

    if (300 < balls.xcor() < paddle_1.xcor() + 10 and
            abs(balls.ycor() - paddle_1.ycor()) < 30):
        balls.bounce('right')
        balls.dx *= 1.1

    if (-300 > balls.xcor() > paddle_2.xcor() - 10 and
            abs(balls.ycor() - paddle_2.ycor()) < 30):
        balls.bounce('left')
        balls.dx *= 1.1

    # reset
    if balls.xcor() > 400:
        score.increase_l()
        balls.respawn()
    elif balls.xcor() < -400:
        score.increase_r()
        balls.respawn()

    if score.score_l == 10:
        is_game = False
        score.win_l()

    elif score.score_r == 10:
        is_game = False
        score.win_r()

    else:
        screen.ontimer(game, 16)


game()

paddle_1.update_position()
paddle_2.update_position()

screen.exitonclick()
