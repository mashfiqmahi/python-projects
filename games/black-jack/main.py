import tkinter as tk
from tkinter import messagebox
import random

# --- Game Logic ---
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        return sum(hand)
    return score


# --- GUI Class ---
class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Blackjack")
        self.root.geometry("400x500")
        self.root.configure(bg="#2d5a27")  # Casino Green

        self.user_cards = []
        self.computer_cards = []

        # UI Elements
        self.label_dealer = tk.Label(root, text="Dealer's Hand", bg="#2d5a27", fg="white", font=("Arial", 12, "bold"))
        self.label_dealer.pack(pady=10)

        self.dealer_display = tk.Label(root, text="", bg="#1e3d1a", fg="white", font=("Arial", 14), width=20, height=2)
        self.dealer_display.pack()

        self.label_player = tk.Label(root, text="Your Hand", bg="#2d5a27", fg="white", font=("Arial", 12, "bold"))
        self.label_player.pack(pady=10)

        self.player_display = tk.Label(root, text="", bg="#1e3d1a", fg="white", font=("Arial", 14), width=20, height=2)
        self.player_display.pack()

        self.score_label = tk.Label(root, text="Score: 0", bg="#2d5a27", fg="yellow", font=("Arial", 10))
        self.score_label.pack()

        # Buttons
        self.btn_frame = tk.Frame(root, bg="#2d5a27")
        self.btn_frame.pack(pady=30)

        self.hit_btn = tk.Button(self.btn_frame, text="Hit", command=self.hit, width=10, state="disabled")
        self.hit_btn.grid(row=0, column=0, padx=5)

        self.stand_btn = tk.Button(self.btn_frame, text="Stand", command=self.stand, width=10, state="disabled")
        self.stand_btn.grid(row=0, column=1, padx=5)

        self.start_btn = tk.Button(root, text="New Game", command=self.start_game, bg="gold",
                                   font=("Arial", 10, "bold"))
        self.start_btn.pack(pady=10)

    def start_game(self):
        self.user_cards = [deal_card(), deal_card()]
        self.computer_cards = [deal_card(), deal_card()]
        self.hit_btn.config(state="normal")
        self.stand_btn.config(state="normal")
        self.update_ui(reveal_dealer=False)
        self.check_instant_win()

    def update_ui(self, reveal_dealer=False):
        # Update Player
        self.player_display.config(text=f"{self.user_cards}")
        u_score = calculate_score(self.user_cards)
        self.score_label.config(text=f"Score: {u_score if u_score != 0 else 21}")

        # Update Dealer
        if reveal_dealer:
            self.dealer_display.config(text=f"{self.computer_cards}")
        else:
            self.dealer_display.config(text=f"[{self.computer_cards[0]}, ?]")

    def check_instant_win(self):
        u_score = calculate_score(self.user_cards)
        if u_score == 0 or u_score > 21:
            self.stand()

    def hit(self):
        self.user_cards.append(deal_card())
        self.update_ui()
        if calculate_score(self.user_cards) > 21:
            self.stand()

    def stand(self):
        self.hit_btn.config(state="disabled")
        self.stand_btn.config(state="disabled")

        u_score = calculate_score(self.user_cards)
        c_score = calculate_score(self.computer_cards)

        # Dealer's turn
        while c_score != 0 and c_score < 17 and u_score <= 21:
            self.computer_cards.append(deal_card())
            c_score = calculate_score(self.computer_cards)

        self.update_ui(reveal_dealer=True)
        self.show_result(u_score, c_score)

    def show_result(self, u_score, c_score):
        # Using your compare logic
        if u_score == c_score:
            res = "It's a Draw! 🙃"
        elif c_score == 0:
            res = "Dealer has Blackjack! 😔"
        elif u_score == 0:
            res = "You have Blackjack! 😀"
        elif u_score > 21:
            res = "Bust! You lose. 😔"
        elif c_score > 21:
            res = "Dealer bust! You win! 😀"
        elif u_score > c_score:
            res = "You win! 😀"
        else:
            res = "You lose. 😔"

        messagebox.showinfo("Result", res)


# --- Run Application ---
root = tk.Tk()
game = BlackjackGUI(root)
root.mainloop()