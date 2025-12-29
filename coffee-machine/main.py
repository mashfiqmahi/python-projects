from tkinter import *
from tkinter import messagebox
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

window = Tk()
window.title("☕ Coffee Machine")
window.config(padx=30, pady=30, bg="#fef6e4")

selected_drink = None

# -------------------- FUNCTIONS -------------------- #
def order_coffee(drink_name):
    global selected_drink
    drink = menu.find_drink(drink_name)

    if not drink:
        return

    if not coffee_maker.is_resource_sufficient(drink):
        messagebox.showerror("Error", "Not enough resources!")
        return

    selected_drink = drink
    open_payment_window()

def open_payment_window():
    pay = Toplevel(window)
    pay.title("Insert Coins")
    pay.config(padx=20, pady=20)

    Label(pay, text=f"Cost: ${selected_drink.cost}", font=("Arial", 12)).pack(pady=5)

    entries = {}

    for coin in ["quarters", "dimes", "nickles", "pennies"]:
        frame = Frame(pay)
        frame.pack(pady=3)
        Label(frame, text=coin.capitalize(), width=10).pack(side=LEFT)
        entry = Entry(frame, width=5)
        entry.insert(0, "0")
        entry.pack(side=LEFT)
        entries[coin] = entry

    def pay_now():
        coins = {}
        try:
            for coin, entry in entries.items():
                coins[coin] = int(entry.get())
                if coins[coin] < 0:
                    raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers only.")
            return

        success, amount = money_machine.make_payment(selected_drink.cost, coins)

        if success:
            coffee_maker.make_coffee(selected_drink)
            update_report()
            messagebox.showinfo(
                "Success",
                f"Enjoy your {selected_drink.name} ☕"
            )
            pay.destroy()
        else:
            messagebox.showwarning(
                "Payment Failed",
                f"Not enough money. Inserted: ${amount}"
            )

    Button(pay, text="Pay", width=10, command=pay_now).pack(pady=10)

def update_report():
    water_label.config(text=f"Water: {coffee_maker.resources['water']} ml")
    milk_label.config(text=f"Milk: {coffee_maker.resources['milk']} ml")
    coffee_label.config(text=f"Coffee: {coffee_maker.resources['coffee']} g")
    money_label.config(text=f"Money: ${money_machine.profit}")

def quit_machine():
    messagebox.showinfo(
        "Machine Off",
        f"Total Money Earned: ${money_machine.profit}"
    )
    window.destroy()

# -------------------- UI -------------------- #
Label(
    text="☕ Coffee Machine ☕",
    font=("Arial", 22, "bold"),
    bg="#fef6e4"
).pack(pady=10)

btn_frame = Frame(bg="#fef6e4")
btn_frame.pack(pady=10)

Button(btn_frame, text="Espresso ($1.5)", width=18,
       command=lambda: order_coffee("espresso")).grid(row=0, column=0, padx=5)

Button(btn_frame, text="Latte ($2.5)", width=18,
       command=lambda: order_coffee("latte")).grid(row=0, column=1, padx=5)

Button(btn_frame, text="Cappuccino ($3.0)", width=18,
       command=lambda: order_coffee("cappuccino")).grid(row=1, column=0, columnspan=2, pady=5)

report_frame = Frame(bg="#fef6e4")
report_frame.pack(pady=10)

water_label = Label(report_frame, bg="#fef6e4")
milk_label = Label(report_frame, bg="#fef6e4")
coffee_label = Label(report_frame, bg="#fef6e4")
money_label = Label(report_frame, bg="#fef6e4")

water_label.pack()
milk_label.pack()
coffee_label.pack()
money_label.pack()

update_report()

Button(text="Quit", bg="#ef476f", fg="white", width=15,
       command=quit_machine).pack(pady=10)

window.mainloop()
