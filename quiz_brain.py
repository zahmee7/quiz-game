class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_runiing(self):
        return self.question_number<len(self.questions_list)



    def user_answer(self):
        current_questions= self.questions_list[self.question_number]
        self.question_number+=1
        user_an = input(f"Q.{self.question_number}: {current_questions.text} (True/False): ")
        self.chake_answer(user_an,current_questions.answer)

    def chake_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower() or len(user_answer.lower())==len(correct_answer.lower()):
            print("You got it right!")
            self.score +=1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n")



