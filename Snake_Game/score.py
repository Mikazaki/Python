from turtle import Turtle
import csv


class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.score = 0
        self.update()
        self.name = ""

    def update(self):

        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("bit5x3", 30, "bold"))

    def game_over(self):

        self.color('red')
        self.goto(0, -80)
        self.write("Game Over", False, align="center", font=("PIXY", 30, "bold"))
        self.goto(0, -210)
        self.color('red')
        self.write("Important Note:", align="center", font=("PIXY", 15, "bold"))
        self.goto(0, -225)
        self.write("Please Do NOT edit your scores in the csv!", align="center", font=("PIXY", 15, "bold"))
        self.goto(0, -240)
        self.write("that is very ungamer like,", align="center", font=("PIXY", 15, "bold"))
        self.goto(0, -255)
        self.write("and a breach to the sacred gamers code!", align="center", font=("PIXY", 15, "bold"))

    def increase(self):

        self.score += 1
        self.update()

    def save_score_to_csv(self):
        with open('scores.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.score])

    def display_leaderboard(self):
        self.penup()
        self.clear()

        ranked_scores = self.display_ranked_scores()

        self.goto(0, 260)
        self.color('white')
        self.write("Ranked Scores:", align="center", font=("PIXY", 30, "bold"))

        y_position = 230

        for rank, (name, score) in enumerate(ranked_scores[:10], start=1):
            self.goto(0, y_position)
            self.color('white')
            self.write(f"Rank {rank}: {name} - {score}", align="center", font=("PIXY", 15, "bold"))
            y_position -= 30

    def get_score(self, item):

        return item[1]

    def display_ranked_scores(self):
        scores_names = []

        with open('scores.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name, score = row
                scores_names.append((name, int(score)))

        ranked_scores = sorted(scores_names, key=self.get_score, reverse=True)
        return ranked_scores
