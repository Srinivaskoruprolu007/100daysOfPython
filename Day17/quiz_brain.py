class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"q.{self.question_no} : {current_question.text} (True/False): ?")
        self.check_answer(user_answer, current_question.answer)

    def sill_has_a_question(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print("You got it right !")

        else:
            print("That's wrong. ")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is {self.score}/{self.question_no}")
        print("\n")


