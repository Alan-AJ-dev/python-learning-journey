class Question():
    def __init__(self,question,ans):
        self.text = question
        self.ans = ans
    
   

class QuestionBank():
     def create_question_bank(self,question_data):
        question_bank = []
        for i in range(len(question_data)):
            text = question_data[i]["text"]
            ans = question_data[i]["answer"]
            new_question = Question(text,ans)
            question_bank.append(new_question)
        return question_bank



