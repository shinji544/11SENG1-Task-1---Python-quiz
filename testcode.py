import customtkinter as ctk
import random

# Setup
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Multiplication Quiz Game")
app.geometry("800x600")


# === Title Menu Frame ===
title_menu = ctk.CTkFrame(app)
title_menu.pack(expand=True, fill="both")

title_label = ctk.CTkLabel(title_menu, text="Multiplication Quiz", font=ctk.CTkFont(size=32, weight="bold"))
title_label.pack(pady=40)

play_button = ctk.CTkButton(title_menu, text="Play", width=200, height=40, command=lambda: goto_main_menu())
play_button.pack(pady=10)

quit_button = ctk.CTkButton(title_menu, text="Quit", width=200, height=40, command=app.destroy)
quit_button.pack(pady=10)

# === Main Menu Frame ===
main_menu = ctk.CTkFrame(app)

main_label = ctk.CTkLabel(main_menu, text="Main menu", font=ctk.CTkFont(size=32, weight="bold"))
main_label.pack(pady=40)

practice_button = ctk.CTkButton(main_menu, text="Practice questions", width=200, height=40, command=lambda: show_quiz())
practice_button.pack(pady=10)

timed_button = ctk.CTkButton(main_menu, text="Timed questions", width=200, height=40)
timed_button.pack(pady=10)

menu_button = ctk.CTkButton(main_menu, text="Go back", width=200, height=40, command=lambda: back_to_title())
menu_button.pack(pady=10)

# === Quiz Frame ===
quiz_frame = ctk.CTkFrame(app)

x = random.randint(1, 9)
y = random.randint(1, 9)
correct = x * y

# Widgets
message_question = ctk.CTkLabel(
    quiz_frame, 
    text=f"{x} x {y}", 
    font=ctk.CTkFont(size=30, weight="bold")
)

entry_label = ctk.CTkLabel(
    quiz_frame, 
    text="Answer:", 
    font=ctk.CTkFont(size=16)
)

entry = ctk.CTkEntry(
    quiz_frame, 
    font=ctk.CTkFont(size=16)
)

hint_label = ctk.CTkLabel(
    quiz_frame, 
    text="", 
    text_color="gray"
)

tip_label = ctk.CTkLabel(
    quiz_frame, 
    text="Tip: press enter to submit", 
    font=ctk.CTkFont(size=12), 
    text_color="gray"
)

feedback_label = ctk.CTkLabel(
    quiz_frame, 
    text="", 
    font=ctk.CTkFont(size=16)
)

retry_button = ctk.CTkButton(
    quiz_frame, 
    text="Try Again?", 
    command=lambda: next_question()
)
retry_button.pack_forget()


# Functions
def show_quiz():
    main_menu.pack_forget()
    quiz_frame.pack(expand=True, fill="both")

def goto_main_menu():
    title_menu.pack_forget()
    main_menu.pack(expand=True, fill="both")

def check_answer(event=None):
    global correct
    user_input = entry.get()
    try:
        user_answer = int(user_input)
    except ValueError:
        feedback_label.configure(text="Please enter a number", text_color="orange")
        entry.delete(0, ctk.END)
        return

    if user_answer == correct:
        feedback_label.configure(text="Good job!", text_color="green")
        retry_button.pack(pady=10)
    else:
        feedback_label.configure(text=f"Unlucky, the answer was {correct}", text_color="red")
        retry_button.pack(pady=10)

def show_hint():
    hint_label.configure(text=f"Hint: The answer is {correct}")

def next_question():
    global x, y, correct
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    correct = x * y

    message_question.configure(text=f"{x} x {y}")
    entry.delete(0, ctk.END)
    feedback_label.configure(text="")
    hint_label.configure(text="")
    retry_button.pack_forget()

def back_to_menu():
    quiz_frame.pack_forget()
    main_menu.pack(expand=True, fill="both")

def back_to_title():
    main_menu.pack_forget()
    title_menu.pack(expand=True, fill="both")

# Layout of quiz
message_question.pack(pady=20)
entry_label.pack()
entry.pack()
entry.bind("<Return>", check_answer)

ctk.CTkButton(quiz_frame, text="Hint", command=show_hint).pack(pady=5)
hint_label.pack()
tip_label.pack()
feedback_label.pack()
ctk.CTkButton(quiz_frame, text="Back to Menu", command=lambda: back_to_menu()).pack(pady=100)

app.mainloop()
