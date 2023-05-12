import tkinter
from quiz_brain import QuizBrain

# Constants for the color theme and font
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Create the main window
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        # Create a canvas for the question text
        self.canvas = tkinter.Canvas(width=400, height=300, bg='White', highlightthickness=0)
        self.quote_text = self.canvas.create_text(200, 150, text="123", width=300, font=FONT, fill="Black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Create a label for the score
        self.score_label = tkinter.Label(text='Score: 0', bg=THEME_COLOR, fg="White", font=FONT)
        self.score_label.grid(row=0, column=1)

        # Create buttons for true and false answers
        true_image = tkinter.PhotoImage(file='images/true.png')
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.my_answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file='images/false.png')
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.my_answer_false)
        self.false_button.grid(row=2, column=1)

        # Start the quiz by showing the first question
        self.get_next_question()

        # Run the window and wait for user input
        self.window.mainloop()

    def get_next_question(self):
        # Reset the background color to white
        self.canvas.config(bg='White')

        # Check if there are more questions
        if self.quiz.still_has_questions():
            # Update the score label
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # Get the next question text from the quiz brain and update the canvas
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            # If there are no more questions, show the end of quiz message and disable answer buttons
            self.canvas.itemconfig(self.quote_text, text="You've reached the end of the quiz!!!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def my_answer_true(self):
        # Check if the answer is correct and get feedback
        is_right = self.quiz.check_answer('True')
        self.get_feedback(is_right)

    def my_answer_false(self):
        # Check if the answer is correct and get feedback
        is_right = self.quiz.check_answer('False')
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        # Update the background color based on the answer correctness
        if is_right:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')

        # Wait for 1 second before showing the next question
        self.window.after(1000, self.get_next_question)
