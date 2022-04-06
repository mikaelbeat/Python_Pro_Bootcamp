
class QuizBrain:
    
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question {self.question_number}: {current_question.text} (True / False)? ")
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1  
            print(f"Your score is {self.question_number}/{self.score}\n")
        else:
            print("That's wrong!")
            print(f"Your score was {self.score}.\n")
    
