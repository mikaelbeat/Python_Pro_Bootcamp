
from Question_model import Question
from Data import question_data
from Quiz_brain import QuizBrain
from replit import clear

question_bank = []

for data in question_data:
   question_text = data["text"]
   question_answer = data["answer"]
   question = Question(question_text, question_answer)
   question_bank.append(question)
   
quiz = QuizBrain(question_bank)



clear()
while quiz.still_has_questions():
   quiz.next_question()

print("You have completed the quiz.")
print(f"You final score was: {quiz.score}/{quiz.question_number}.")

   


