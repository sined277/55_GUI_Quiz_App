import html

# Create a QuizBrain class to manage quiz-related functions
class QuizBrain:

    # Initialize the class with a question number, score, question list, and current question
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # Check if there are still questions remaining in the quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Move to the next question in the quiz and return the question text
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Unescape HTML entities in the question text
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")

    # Check the user's answer against the correct answer and update the score accordingly
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
