from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for text in question_data:
    q = text["text"]
    a = text["answer"]
    question = Question(text=q, answer=a)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_runiing() == True:
    quiz.user_answer()
print("You've completed the quiz")
print(f"Your current score is: {quiz.score}/{quiz.question_number}")




