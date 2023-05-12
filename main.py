# Import necessary modules
from question_model import Question  # Import the Question class from question_model.py
from data import question_data  # Import the question data from data.py
from quiz_brain import QuizBrain  # Import the QuizBrain class from quiz_brain.py
from ui import QuizInterface  # Import the QuizInterface class from ui.py

# Create an empty list to hold the Question objects
question_bank = []

# Loop through the question data and create Question objects
for question in question_data:
    question_text = question["question"]  # Get the question text from the question data
    question_answer = question["correct_answer"]  # Get the answer to the question from the question data
    new_question = Question(question_text, question_answer)  # Create a new Question object with the question text and answer
    question_bank.append(new_question)  # Add the new Question object to the question bank list

# Create a new QuizBrain object with the question bank list
quiz = QuizBrain(question_bank)

# Create a new QuizInterface object with the QuizBrain object
quiz_ui = QuizInterface(quiz)

# Run the quiz
# while quiz.still_has_questions():
#     quiz.next_question()

# Print the final score once the quiz is complete
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
