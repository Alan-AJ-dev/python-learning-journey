
from ui import *



question_set = QuestionBank()

question_bank_1 = question_set.create_question_bank(question_data)
# question_bank_2 = question_set.create_question_bank(question_data2)

quiz_brain = QuizBrain(question_bank_1)
# quiz_brain_2 = QuizBrain(question_bank_2)
exit = False

score = 0
ui = QuizInterface(quiz_brain)









   
    

    
