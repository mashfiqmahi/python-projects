x = 1
class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.q_list):
            return True
        else:
            print("No more questions left!")
            return False

    def next_question(self):
        if x == 0:
            self.current_question = self.q_list[self.question_number - 1]
        elif x == 1:
            self.current_question = self.q_list[self.question_number]
            self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def answer_check(self,guess):
        correct_answer = self.current_question.answer
        if guess == correct_answer:
            print("You got it right")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}\n")
            return True
        else:
            print("That's wrong")
            print(f"The correct answer was {correct_answer}.")
            print(f"Your current score is {self.score}/{self.question_number}\n")
            return False

