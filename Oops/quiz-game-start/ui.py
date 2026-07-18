from textwrap import fill
from tkinter import  *
from data import question_data
from question_model import Question,QuestionBank
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain : QuizBrain):
        self.response = False
        self.window = Tk()
        self.quiz_brain = quiz_brain
        self.window.title("Truth or Dare")
        self.window.config(height=500,width=350,padx=20, pady=20,bg=THEME_COLOR)
        self.label = Label(text= f"Score: {quiz_brain.score}")
        self.label.config(pady=25,padx=14,bg=THEME_COLOR,fg="white")
        self.label.grid(row=0,column=1)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_test = self.canvas.create_text(150, 120, text="Some Questions", fill=THEME_COLOR,width=280)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50,padx=20)


        true_img = PhotoImage(file = 'images/true.png')
        self.true = Button(image=true_img,padx=20,pady=20,bg=THEME_COLOR,command=self.true_check)
        self.true.grid(row=2, column=0)

        false_img = PhotoImage(file='images/false.png')
        self.false = Button(image=false_img,bg=THEME_COLOR,command=self.false_check)
        self.false.grid(row=2,column=1)


        self.next_question()
        print("hello1")
        if self.quiz_brain.is_over:
            print("hello")
            self.canvas.itemconfig(self.question_test,text=f"Congragulations successfully completed the Quiz"
                                                           f" Program!!\n Your Score is {self.quiz_brain.score}")


        self.window.mainloop()

    def feedback(self, right):
        pass
        if right:
            self.canvas.config(bg = "green")
            self.quiz_brain.score += 1
            self.label.config(text=f"Score: {self.quiz_brain.score}")
            self.window.after(1000, self.next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.next_question)

    def false_check(self):
        self.feedback(self.quiz_brain.check_ans("false"))

    def true_check(self):
        self.feedback(self.quiz_brain.check_ans("true"))



    def next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_test, text=self.quiz_brain.next_question(), fill=THEME_COLOR)
