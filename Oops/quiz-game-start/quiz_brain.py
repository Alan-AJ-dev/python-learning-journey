from data import question_data
from question_model import Question

class QuizBrain():
    def __init__(self,ques_list):
        self.question_number = 0
        self.score = 0
        self.question_list = ques_list
        

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        in_ans =  input(f"Q: {self.question_number}: {current_question.text} (True/False): ")
        if self.check_ans(current_question.ans,in_ans):
            self.score +=1
            print(f"Your answer is correct" )
        elif in_ans == "exit":
            print("Exiting as your wish")
            return True
        else:
            print("Answer Was Wrong !!!")
            print(f"The correct ans was {current_question.ans}")
        print(f"Your score is ({self.score}")
        print(" "*2)
        return False

    def still_remain(self):
       
        if self.question_number < len(self.question_list):
            return True
        else:
            print("Questions Over")
            return False
    

    def check_ans(self,question_ans,in_ans):
        return question_ans.lower() == in_ans.lower()
    

