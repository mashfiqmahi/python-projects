from game_data import question_data
from question_model import Question
from question_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for i in range(len(question_data)):
    q = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(q)

print('Type "quit" to exit game')
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")