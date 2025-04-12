import tkinter as tk
from tkinter import ttk
import random

# Main window setup
mg = tk.Tk()
mg.title("Multiplication Quiz")
mg.geometry("800x600")
mg.configure(bg="#6d9ac7")

# Make the root window scalable
mg.grid_rowconfigure(0, weight=1)
mg.grid_columnconfigure(0, weight=1)

# window size stuff
main_frame = tk.Frame(mg, bg="#6d9ac7")
main_frame.grid(row=0, column=0, sticky="nsew")

for i in range(10):
    main_frame.grid_rowconfigure(i, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# initial question variables!!!
x = random.randint(1, 9)
y = random.randint(1, 9)
correct = x * y

# my global variables here (mostly for functions to mess around with)
message_question = tk.Label(main_frame, text=f"{x} x {y}", bg="#1269cc", fg="white", font=("Arial", 20))
entry_label = tk.Label(main_frame, text="Answer:", bg="#6d9ac7", font=("Arial", 12))
entry = tk.Entry(main_frame, font=("Arial", 12))

hint_label = tk.Label(main_frame, text="", bg="#6d9ac7", font=("Arial", 12))
tip_label = tk.Label(main_frame, text="Tip: press enter to enter", bg="#6d9ac7", font=("Arial", 10))
feedback_label = tk.Label(main_frame, text="", bg="#6d9ac7", font=("Arial", 12))

retry_button = tk.Button(main_frame, text="Try again?", command=lambda: next_question())


# functions here
def open_secondary_window():
    secondary = tk.Toplevel()
    secondary.title("Secondary Window")
    secondary.geometry("400x200")
    tk.Button(secondary, text="Close window", command=secondary.destroy).pack(pady=50)

def check_answer(event=None):
    global correct
    user_input = entry.get()
    try:
        user_answer = int(user_input)
    except ValueError:
        feedback_label.config(text="Please enter a number", bg="orange")
        entry.delete(0, tk.END)
        return

    if user_answer == correct:
        feedback_label.config(text="Good job!", bg="lightgreen")
        retry_button.grid(row=7, column=0, columnspan=2)
    else:
        feedback_label.config(text=f"Unlucky, the answer was {correct}", bg="lightcoral")
        retry_button.grid(row=7, column=0, columnspan=2)

def show_hint():
    hint_label.config(text=f"Hint: The answer is {correct}")

def next_question():
    global x, y, correct
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    correct = x * y

    message_question.config(text=f"{x} x {y}")
    entry.delete(0, tk.END)
    feedback_label.config(text="", bg="#6d9ac7")
    hint_label.config(text="")

    retry_button.grid_remove()

# actual code for the ui here
message_question.grid(row=1, column=0, columnspan=2)
entry_label.grid(row=2, column=0, sticky="e")
entry.grid(row=2, column=1, sticky="w")
entry.bind("<Return>", check_answer)

tk.Button(main_frame, text="Press for hint", command=show_hint).grid(row=3, column=1, sticky="w")
hint_label.grid(row=4, column=0, columnspan=2)
tip_label.grid(row=5, column=0, columnspan=2)
feedback_label.grid(row=6, column=0, columnspan=2)

tk.Button(main_frame, text="Open a window", command=open_secondary_window).grid(row=8, column=0, columnspan=2)

mg.mainloop()


