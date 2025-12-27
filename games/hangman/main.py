import random
from tkinter import *
from tkinter import messagebox
from stages import stages, logo
from Hangman_wordlist import word_list

# -------------------- GAME STATE -------------------- #
chosen_word = ""
display_word = []
lives = 6
score = 0
level = 1
used_letters = set()

# -------------------- GAME LOGIC -------------------- #
def start_game():
    global chosen_word, display_word, lives, used_letters
    lives = 6
    used_letters.clear()

    chosen_word = random.choice(word_list)
    display_word = ["_"] * len(chosen_word)

    update_ui()
    play_again_btn.config(state=DISABLED)

    for btn in letter_buttons:
        btn.config(state=NORMAL)

def next_level():
    global chosen_word, display_word, lives, used_letters, level

    level += 1
    lives = 6
    used_letters.clear()

    chosen_word = random.choice(word_list)
    display_word = ["_"] * len(chosen_word)

    update_ui()

    for btn in letter_buttons:
        btn.config(state=NORMAL)


def guess_letter(letter):
    global lives, score

    if letter in used_letters:
        return

    used_letters.add(letter)

    for btn in letter_buttons:
        if btn["text"].lower() == letter:
            btn.config(state=DISABLED)

    if letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                display_word[i] = letter
    else:
        lives -= 1

    word_label.config(text=" ".join(display_word))
    stage_label.config(text=stages[lives])
    lives_label.config(text=f"Lives: {lives}")

    if "_" not in display_word:
        global score
        score += 1
        messagebox.showinfo(
            "Level Complete!",
            f"Great job!\nMoving to Level {level + 1}"
        )
        next_level()

    elif lives == 0:
        game_over(False)

def game_over(win):
    for btn in letter_buttons:
        btn.config(state=DISABLED)

    play_again_btn.config(state=NORMAL)

    if win:
        messagebox.showinfo("You Win!", f"You guessed the word!\nScore: {score}")
    else:
        messagebox.showinfo("Game Over", f"The word was: {chosen_word}\nScore: {score}")

def quit_game():
    if score == 0:
        window.destroy()
    else:
        messagebox.showinfo("Quit Game", f"Final Score: {score}")
        window.destroy()

def update_ui():
    word_label.config(text=" ".join(display_word))
    stage_label.config(text=stages[lives])
    lives_label.config(text=f"Lives: {lives}")
    level_label.config(text=f"Level: {level}")
    score_label.config(text=f"Score: {score}")


def key_pressed(event):
    letter = event.char.lower()
    if letter.isalpha() and letter in "abcdefghijklmnopqrstuvwxyz":
        guess_letter(letter)

# -------------------- UI -------------------- #
window = Tk()
window.bind("<Key>", key_pressed)
window.title("Hangman")
window.config(padx=30, pady=20)

title_label = Label(text="HANGMAN", font=("Arial", 24, "bold"))
title_label.pack()

lives_label = Label(text="Lives: 6", font=("Arial", 14))
lives_label.pack()

level_label = Label(text="Level: 1", font=("Arial", 14))
level_label.pack()

score_label = Label(text="Score: 0", font=("Arial", 14))
score_label.pack()


stage_label = Label(text=stages[6], font=("Courier", 10))
stage_label.pack()

word_label = Label(text="", font=("Arial", 18))
word_label.pack(pady=10)

# -------------------- LETTER BUTTONS -------------------- #
letters_frame = Frame()
letters_frame.pack()

letter_buttons = []

for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    btn = Button(
        letters_frame,
        text=letter.upper(),
        width=4,
        command=lambda l=letter: guess_letter(l)
    )
    btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)
    letter_buttons.append(btn)

# -------------------- CONTROL BUTTONS -------------------- #
play_again_btn = Button(text="Play Again", state=DISABLED, command=start_game)
play_again_btn.pack(pady=5)

quit_btn = Button(text="Quit", command=quit_game)
quit_btn.pack()

start_game()
window.mainloop()
