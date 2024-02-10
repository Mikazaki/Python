from question_model import Question
from data import question_data
from quiz_brain import QuizBrain




question_bank = []

for question in question_data:
    q = question['question']
    a = question['correct_answer']
    qb = Question(q, a)
    question_bank.append(qb)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")