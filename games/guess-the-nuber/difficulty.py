EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def set_difficulty():
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose == 'hard':
        return HARD_LEVEL_TURN
    else:
        return EASY_LEVEL_TURN