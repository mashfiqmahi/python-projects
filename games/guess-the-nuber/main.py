import random
from tkinter import *
from tkinter import messagebox

# -------------------- GAME STATE -------------------- #
level = 1
score = 0
attempts = 0
answer = 0
MAX_RANGE = 100

# -------------------- GAME LOGIC -------------------- #
def start_game():
    global level, score
    level = 1
    score = 0
    next_level()
    play_again_btn.config(state=DISABLED)

def next_level():
    global answer, attempts, MAX_RANGE

    MAX_RANGE = level * 100
    answer = random.randint(1, MAX_RANGE)
    attempts = 10 if level <= 3 else 7

    update_ui()
    guess_entry.delete(0, END)

def check_guess(event=None):
    global attempts, level, score

    guess = guess_entry.get()
    if not guess.isdigit():
        feedback_label.config(text="Enter a number!", fg="orange")
        return

    guess = int(guess)
    attempts -= 1

    if guess > answer:
        feedback_label.config(text="Too High ⬆️", fg="red")
    elif guess < answer:
        feedback_label.config(text="Too Low ⬇️", fg="blue")
    else:
        score += 1
        level += 1
        messagebox.showinfo("Correct!", "Level Up! 🎉")
        next_level()
        return

    if attempts == 0:
        game_over()

    update_ui()

def game_over():
    play_again_btn.config(state=NORMAL)
    messagebox.showinfo(
        "Game Over",
        f"Final Score: {score}\nLevel Reached: {level}"
    )

def quit_game():
    messagebox.showinfo(
        "Quit Game",
        f"Final Score: {score}\nLevel Reached: {level}"
    )
    window.destroy()

# -------------------- UI UPDATE -------------------- #
def update_ui():
    level_label.config(text=f"Level: {level}")
    score_label.config(text=f"Score: {score}")
    attempts_label.config(text=f"Attempts Left: {attempts}")
    range_label.config(text=f"Guess between 1 and {MAX_RANGE}")

# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Number Guessing Game")
window.config(padx=40, pady=30, bg="#f0f8ff")

title = Label(
    text="🎯 Number Guessing Game 🎯",
    font=("Arial", 22, "bold"),
    bg="#f0f8ff",
    fg="#333"
)
title.pack(pady=10)

level_label = Label(font=("Arial", 14), bg="#f0f8ff")
level_label.pack()

score_label = Label(font=("Arial", 14), bg="#f0f8ff")
score_label.pack()

attempts_label = Label(font=("Arial", 14), bg="#f0f8ff")
attempts_label.pack()

range_label = Label(font=("Arial", 12), bg="#f0f8ff")
range_label.pack(pady=5)

guess_entry = Entry(font=("Arial", 14), justify="center")
guess_entry.pack(pady=10)
guess_entry.bind("<Return>", check_guess)

guess_btn = Button(
    text="Guess",
    font=("Arial", 12),
    bg="#4caf50",
    fg="white",
    command=check_guess
)
guess_btn.pack()

feedback_label = Label(font=("Arial", 14), bg="#f0f8ff")
feedback_label.pack(pady=10)

play_again_btn = Button(
    text="Play Again",
    font=("Arial", 12),
    state=DISABLED,
    command=start_game
)
play_again_btn.pack(pady=5)

quit_btn = Button(
    text="Quit",
    font=("Arial", 12),
    bg="#e53935",
    fg="white",
    command=quit_game
)
quit_btn.pack()

start_game()
window.mainloop()
