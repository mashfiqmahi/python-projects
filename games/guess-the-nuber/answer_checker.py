def check_answer(chosen_number, final_number, turn):
    if chosen_number > final_number:
        print("Too high")
        return turn - 1
    elif chosen_number < final_number:
        print("Too low")
        return turn - 1
    else:
        print(f"You got it. The number was {final_number}")
