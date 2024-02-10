import turtle

import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
turt = Turtle()
turt.hideturtle()
turt.penup()
img = "blank_states_img.gif"
screen.bgpic(img)

data = pandas.read_csv("50_states.csv")
states = data.state.str.lower().to_list()
score = 0
guessed_states = []

while score < 50:
    turtle.update()
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="Guess a State")
    if answer.lower() in states:
        if answer.title() not in guessed_states:
            guessed_states.append(answer.title())
            print(guessed_states)
            score += 1
            coord = data[data.state == answer.title()]
            x = coord.x.values[0]
            y = coord.y.values[0]
            turt.goto(x, y)
            turt.write(answer.title(), align='center', font=('Arial', 8, 'bold'))

    if answer.lower() == "exit":
        missing_states = [state for state in states if state.title() not in guessed_states]
        new = pandas.DataFrame(missing_states)
        new.to_csv("missing_states.csv")
        break

turtle.mainloop()
