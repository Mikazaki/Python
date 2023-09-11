from turtle import Turtle
import csv
FONT = ("PIXY", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.color('black')
        self.goto(-200, 260)
        self.level = 1
        self.update()

    def update(self):

        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def game_over(self):

        self.color('black')
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("PIXY", 30, "normal"))

    def increase(self):

        self.level += 1
        self.update()

    def save_score_to_csv(self):

        with open('scores.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.level])

    def display_leaderboard(self):

        self.penup()
        self.clear()

        ranked_scores = self.display_ranked_scores()

        self.goto(0, 260)
        self.color('black')
        self.write("Ranked Scores:", align="center", font=("PIXY", 30, "bold"))

        y_position = 230

        for rank, (name, score) in enumerate(ranked_scores[:10], start=1):

            self.goto(0, y_position)
            self.color('black')
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
