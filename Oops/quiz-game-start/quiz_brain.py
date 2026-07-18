from data import question_data
from question_model import Question
import  html

class QuizBrain():
    def __init__(self,ques_list):
        self.question_number = 0
        self.score = 0
        self.is_over = False
        self.question_list = ques_list
        self.current_question = None

    def next_question(self):
        try:

            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
        except IndexError:
            self.is_over = True


        return f"{self.question_number} {html.unescape(self.current_question.text)}"



    

    def check_ans(self,in_ans):
        return self.current_question.ans.lower() == in_ans.lower()
    

