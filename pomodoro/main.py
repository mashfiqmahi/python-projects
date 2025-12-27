import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    start_button.config(state=NORMAL)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    start_button.config(state=DISABLED)
    reps += 1

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    102, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

timer_label = Label(
    text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN
)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)

window.mainloop()
