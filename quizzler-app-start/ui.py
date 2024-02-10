from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Ui:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.q_canvas = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"), width=280)

        self.score = Label(text=f"Score: 0", font=("Arial", 10, "bold"), fg="white", background=THEME_COLOR)
        self.score.grid(column=1, row=0)

        right = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right, highlightthickness=0, borderwidth=0, command=self.check_right)
        self.right_button.grid(column=0, row=2)

        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0, borderwidth=0, command=self.check_wrong)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.q_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.q_canvas, text="You have reached the end of the quiz")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def check_right(self):
        self.outcome(self.quiz.check_answer("True"))

    def check_wrong(self):
        self.outcome(self.quiz.check_answer("False"))

    def outcome(self, is_right):
        self.window.after(1000, self.get_next_question)

        if is_right:
            self.canvas.configure(background="green")

        else:
            self.canvas.configure(background="red")
