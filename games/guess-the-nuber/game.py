import random
from difficulty import set_difficulty
from answer_checker import check_answer


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turn = set_difficulty()
    chosen_number = 0
    while chosen_number != answer:
        print(f"You have {turn} attempts remaining to guess the number")
        chosen_number = int(input("Guess a number : "))
        turn = check_answer(chosen_number,answer,turn)
        if turn == 0:
            print("You've run out of guesses, you lose.")
            return
        elif chosen_number != answer:
            print("Try again")