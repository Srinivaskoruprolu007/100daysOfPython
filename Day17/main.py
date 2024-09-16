from question_model import Question
from Question_Data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects from the question data
question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the quiz with the question bank
quiz = QuizBrain(question_bank)
quiz.next_question()

# Continue asking questions while there are more questions in the quiz
while quiz.still_has_a_question():
    quiz.next_question()

# Print the final results after the quiz is completed
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")
