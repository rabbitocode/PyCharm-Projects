import time
from tkinter import *
from quiz_brain import QuizBrain


FONT_NAME = "Courier"

THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain


        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)



        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            fill=THEME_COLOR,
            text="Text goes here",
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Score Label
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=(FONT_NAME, 25, "bold"))
        self.score_label.grid(column=1, row=0)

        # True Button
        self.true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=0, row=3)

        # False Button
        self.false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
       self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)