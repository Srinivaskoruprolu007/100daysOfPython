class QuizBrain:
    # Initialize the QuizBrain class with the list of questions
    def __init__(self, q_list):
        self.question_no = 0  # Keeps track of the current question number
        self.question_list = q_list  # List of all the questions
        self.score = 0  # Keeps track of the player's score

    # Method to get the next question from the list and ask the user for their answer
    def next_question(self):
        current_question = self.question_list[self.question_no]  # Get the current question
        self.question_no += 1  # Increment the question number
        user_answer = input(f"q.{self.question_no} : {current_question.text} (True/False): ?")  # Prompt the user for their answer
        self.check_answer(user_answer, current_question.answer)  # Check if the user's answer is correct

    # Method to check if there are still questions left in the quiz
    def still_has_a_question(self):
        if self.question_no < len(self.question_list):  # Compare current question number with the total number of questions
            return True  # Return True if there are more questions
        else:
            return False  # Return False if there are no more questions

    # Method to check the user's answer and update the score accordingly
    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():  # Check if the user's answer matches the correct answer (case insensitive)
            self.score += 1  # Increment the score if the answer is correct
            print("You got it right!")  # Notify the user of their correct answer
        else:
            print("That's wrong.")  # Notify the user if the answer is wrong
        print(f"The correct answer was: {answer}")  # Display the correct answer
        print(f"Your current score is {self.score}/{self.question_no}")  # Display the current score
        print("\n")  # Add a line break for better readability
