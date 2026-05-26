from data import question_data,question_data2
from question_model import Question,QuestionBank
from quiz_brain import QuizBrain


question_set = QuestionBank()

question_bank_1 = question_set.create_question_bank(question_data)
question_bank_2 = question_set.create_question_bank(question_data2)

quiz_brain = QuizBrain(question_bank_1)
quiz_brain_2 = QuizBrain(question_bank_2)
exit = False

score = 0

while not exit and quiz_brain.still_remain():
    exit = quiz_brain.next_question()



while not exit and quiz_brain_2.still_remain():
    exit = quiz_brain_2.next_question()
   
    

    
