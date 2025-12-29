# gui_ceaser.py
import tkinter as tk
from tkinter import messagebox
from alphabet_list import alphabet


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    return end_text


def submit_action():
    text = text_entry.get().lower()
    if not text:
        messagebox.showwarning("Warning", "Please enter a message!")
        return

    try:
        shift = int(shift_entry.get()) % 26
    except ValueError:
        messagebox.showwarning("Warning", "Shift must be a number!")
        return

    direction = direction_var.get()
    if not direction:
        messagebox.showwarning("Warning", "Please select encode or decode!")
        return

    result = ceaser(text, shift, direction)
    result_label.config(text=f"Result: {result}")


def check_input(*args):
    if text_entry.get() and shift_entry.get().isdigit() and direction_var.get():
        submit_btn.config(state="normal")
    else:
        submit_btn.config(state="disabled")


# GUI setup
root = tk.Tk()
root.title("Caesar Cipher")

tk.Label(root, text="Enter your message:").grid(row=0, column=0, padx=10, pady=10)
text_entry = tk.Entry(root, width=30)
text_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Shift number:").grid(row=1, column=0, padx=10, pady=10)
shift_entry = tk.Entry(root, width=5)
shift_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

direction_var = tk.StringVar(value="")
tk.Label(root, text="Choose action:").grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Encode", variable=direction_var, value="encode", command=check_input).grid(row=2, column=1,
                                                                                                      sticky="w")
tk.Radiobutton(root, text="Decode", variable=direction_var, value="decode", command=check_input).grid(row=2, column=1)

submit_btn = tk.Button(root, text="Submit", state="disabled", command=submit_action)
submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Track input changes to enable button
text_entry.bind("<KeyRelease>", lambda e: check_input())
shift_entry.bind("<KeyRelease>", lambda e: check_input())

root.mainloop()
