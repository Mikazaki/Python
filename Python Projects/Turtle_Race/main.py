from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(width=700, height=400)
bots = False
bet = None
player_list = {}
color = ['red', 'blue', 'cyan', 'purple', 'green', 'yellow']

number_of_players = screen.textinput(title="Number of Players", prompt="How Many Player(s): "
                                                                       "\n(Max 6 Players)")

if number_of_players == "1":

    bots = True
    player_list = screen.textinput(title="Player Name", prompt="Enter Your Name(s): ")
    bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a Color:\n" + "\n".join(color))

else:

    remaining_colors = color.copy()

    for players in range(int(number_of_players)):
        player = screen.textinput(title="Player Name", prompt="Enter Your Name(s): ")
        bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a Color:\n" + "\n".join(remaining_colors))
        remaining_colors.remove(bet.lower())
        player_list[player] = bet.lower()

screen.colormode(255)
turtles = []


flag = Turtle("square")
flag.penup()
flag.speed("fastest")
x = 310
y = 180

for i in range(9):
    flag.goto(x, y)
    flag.stamp()
    x += 20
    y -= 20
    flag.goto(x, y)
    flag.stamp()
    x -= 20
    y -= 20
    flag.goto(x, y)
    flag.stamp()

if bots:

    for number_turtle in range(6):
        turt = Turtle(shape='turtle')
        turt.color(color[number_turtle])
        turt.penup()
        turt.goto(x=-340, y=-125 + 50 * number_turtle)
        turtles.append(turt)

else:

    for player, bet in player_list.items():
        turt = Turtle(shape='turtle')

        if bet in color:
            turt.color(bet)
            color.remove(bet)

        else:
            turt.color(random.choice(list(color)))
        turt.penup()
        turt.goto(x=-340, y=-125 + 50 * len(turtles))
        turtles.append(turt)

if bet:
    race = True

while race:

    for turtle in turtles:

        if turtle.xcor() > 285:
            race = False
            winner = turtle.pencolor()

            if bots:

                if winner == bet.lower():
                    screen.textinput(title="Race Result", prompt=f"You have won. The {winner} turtle is the winner.")
                else:
                    screen.textinput(title="Race Result", prompt=f"You have lost. The winner is {winner} turtle.")

            for player in player_list.keys():
                if winner == player_list[player]:
                    screen.textinput(title="Race Result",
                                     prompt=f"Player {player}'s turtle has won. The {winner} turtle is the winner.")

        distance = random.randint(0, 12)
        turtle.forward(distance)

screen.exitonclick()
