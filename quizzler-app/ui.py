from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
class QuizInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score board
        self.score_label = Label(text="Score : 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text =  self.canvas.create_text(150, 125, width=280, text="some question", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")
        self.right_button = Button(image=right_image, command=self.right )
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=wrong_image, command=self.wrong)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reach end of the game")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right(self):
        #is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))


    def wrong(self):
        #is_right = self.quiz.check_answer("False")
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)