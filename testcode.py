import customtkinter as ctk
import random

# ======== Setup ========
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Multiplication Quiz Game")
app.geometry("800x600")
app.configure(fg_color="#1A1A2E")

# ======== Fonts & Colors ========
title_font = ctk.CTkFont(family="Segoe UI", size=32, weight="bold")
button_font = ctk.CTkFont(family="Segoe UI", size=16)
label_font = ctk.CTkFont(family="Segoe UI", size=20)
small_font = ctk.CTkFont(family="Segoe UI", size=12)
accent_color = "#1E90FF"
entry_bg = "#2C3E50"

# ======== Variables ========
x = y = correct = 0
score = 0
question_num = 0
max_questions = 10
total_time = 5.0  # Total time in seconds for timed quiz
remaining_time = total_time
timer_running = False

# ======== Title Menu ========
title_menu = ctk.CTkFrame(app, corner_radius=20)
title_menu.pack(expand=True, fill="both")

title_label = ctk.CTkLabel(title_menu, text="Multiplication Quiz", font=title_font, text_color="white")
title_label.pack(pady=(60, 40))

play_button = ctk.CTkButton(title_menu, text="Play", font=button_font, width=220, height=45,
                            fg_color=accent_color, hover_color="#4682B4",
                            corner_radius=10, command=lambda: goto_main_menu())
play_button.pack(pady=10)

quit_button = ctk.CTkButton(title_menu, text="Quit", font=button_font, width=220, height=45,
                            fg_color="gray", hover_color="#555555",
                            corner_radius=10, command=app.destroy)
quit_button.pack(pady=10)

# ======== Main Menu ========
main_menu = ctk.CTkFrame(app, corner_radius=20)

main_label = ctk.CTkLabel(main_menu, text="Main Menu", font=title_font, text_color="white")
main_label.pack(pady=(60, 40))

practice_button = ctk.CTkButton(main_menu, text="Practice Questions", font=button_font, width=220, height=45,
                                fg_color=accent_color, hover_color="#4682B4", corner_radius=10,
                                command=lambda: show_quiz())
practice_button.pack(pady=10)

timed_button = ctk.CTkButton(main_menu, text="Timed Questions", font=button_font, width=220, height=45,
                             fg_color=accent_color, hover_color="#4682B4", corner_radius=10,
                             command=lambda: show_timed_quiz())
timed_button.pack(pady=10)

menu_button = ctk.CTkButton(main_menu, text="Go Back", font=button_font, width=220, height=45,
                            fg_color="gray", hover_color="#555555",
                            corner_radius=10, command=lambda: back_to_title())
menu_button.pack(pady=(30, 10))

# ======== Countdown Overlay ========
countdown_overlay = ctk.CTkFrame(app, fg_color="#000000", corner_radius=0)
countdown_label = ctk.CTkLabel(countdown_overlay, text="", font=ctk.CTkFont(size=72, weight="bold"), text_color="white")
countdown_label.pack(expand=True)

# ======== Quiz Frame (Practice) ========
quiz_frame = ctk.CTkFrame(app, corner_radius=20)
message_question = ctk.CTkLabel(quiz_frame, text="", font=label_font, text_color="white")
entry_label = ctk.CTkLabel(quiz_frame, text="Answer:", font=button_font, text_color="white")
entry = ctk.CTkEntry(quiz_frame, font=button_font, text_color="white", fg_color=entry_bg,
                     border_color=accent_color, border_width=2, corner_radius=8)
hint_label = ctk.CTkLabel(quiz_frame, text="", text_color="gray")
tip_label = ctk.CTkLabel(quiz_frame, text="Tip: Press Enter to submit", font=small_font, text_color="gray")
feedback_label = ctk.CTkLabel(quiz_frame, text="", font=button_font, text_color="white")
retry_button = ctk.CTkButton(quiz_frame, text="Try Again?", font=button_font,
                             fg_color=accent_color, hover_color="#4682B4", corner_radius=10,
                             command=lambda: next_question())
hint_button = ctk.CTkButton(quiz_frame, text="Hint", font=button_font,
                            fg_color="#444", hover_color="#666",
                            corner_radius=10, command=lambda: show_hint())
back_button = ctk.CTkButton(quiz_frame, text="Back to Menu", font=button_font,
                            fg_color="gray", hover_color="#555555",
                            corner_radius=10, command=lambda: back_to_menu())

message_question.pack(pady=30)
entry_label.pack()
entry.pack(pady=(5, 15))
entry.bind("<Return>", lambda event: check_answer())
hint_button.pack(pady=5)
hint_label.pack()
tip_label.pack(pady=5)
feedback_label.pack(pady=10)
retry_button.pack_forget()
back_button.pack(pady=(20, 10))

# ======== Timed Quiz Frame ========
timed_quiz_frame = ctk.CTkFrame(app, corner_radius=20)

ready_button = ctk.CTkButton(timed_quiz_frame, text="Ready?", font=button_font, width=220, height=45,
                             fg_color=accent_color, hover_color="#4682B4", corner_radius=10,
                             command=lambda: start_countdown())
ready_button.pack(pady=100)

timed_question = ctk.CTkLabel(timed_quiz_frame, text="", font=label_font, text_color="white")
timed_entry_label = ctk.CTkLabel(timed_quiz_frame, text="Answer:", font=button_font, text_color="white")
timed_entry = ctk.CTkEntry(timed_quiz_frame, font=button_font, text_color="white", fg_color=entry_bg,
                           border_color=accent_color, border_width=2, corner_radius=8)
time_label = ctk.CTkLabel(timed_quiz_frame, text="Time:", font=button_font, text_color="white")
time_progress = ctk.CTkProgressBar(timed_quiz_frame, width=400, progress_color=accent_color, mode="determinate")
score_label = ctk.CTkLabel(timed_quiz_frame, text="Score: 0", font=button_font, text_color="white")
timed_feedback = ctk.CTkLabel(timed_quiz_frame, text="", font=button_font, text_color="white")
timed_tip_label = ctk.CTkLabel(timed_quiz_frame, text="Tip: Press Enter to submit", font=small_font, text_color="gray")
timed_hint_button = ctk.CTkButton(timed_quiz_frame, text="Hint", font=button_font,
                                  fg_color="#444", hover_color="#666", corner_radius=10,
                                  command=lambda: show_timed_hint())
timed_hint_label = ctk.CTkLabel(timed_quiz_frame, text="", text_color="gray")
retry_button_timed = ctk.CTkButton(timed_quiz_frame, text="Next Question", font=button_font,
                                   fg_color=accent_color, hover_color="#4682B4", corner_radius=10,
                                   command=lambda: next_timed_question())
timed_back_button = ctk.CTkButton(timed_quiz_frame, text="Back to Menu", font=button_font,
                                  fg_color="gray", hover_color="#555555", corner_radius=10,
                                  command=lambda: back_to_menu())

# Hide timed quiz widgets initially
timed_question.pack_forget()
timed_entry_label.pack_forget()
timed_entry.pack_forget()
time_label.pack_forget()
time_progress.pack_forget()
score_label.pack_forget()
timed_feedback.pack_forget()
timed_tip_label.pack_forget()
timed_hint_button.pack_forget()
timed_hint_label.pack_forget()
retry_button_timed.pack_forget()
timed_back_button.pack_forget()

# ======== Navigation ========
def goto_main_menu():
    title_menu.pack_forget()
    main_menu.pack(expand=True, fill="both")

def back_to_title():
    main_menu.pack_forget()
    title_menu.pack(expand=True, fill="both")

def back_to_menu():
    global timer_running
    timer_running = False
    quiz_frame.pack_forget()
    timed_quiz_frame.pack_forget()
    timed_entry.unbind("<Return>")
    main_menu.pack(expand=True, fill="both")

# ======== Countdown Logic ========
def start_countdown():
    main_menu.pack_forget()
    ready_button.pack_forget()
    timed_back_button.pack_forget()  # Hide(back) button during countdown
    timed_quiz_frame.pack_forget()
    countdown_overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
    countdown_label.configure(text="3")
    app.after(1000, lambda: update_countdown(2))

def update_countdown(count):
    if count > 0:
        countdown_label.configure(text=str(count))
        app.after(1000, lambda: update_countdown(count - 1))
    else:
        countdown_label.configure(text="GO!")
        app.after(1000, start_timed_quiz)

def start_timed_quiz():
    countdown_overlay.place_forget()
    timed_quiz_frame.pack(expand=True, fill="both")
    timed_question.pack(pady=30)
    time_label.pack(pady=5)
    time_progress.pack(pady=5)
    score_label.pack(pady=10)
    timed_entry_label.pack()
    timed_entry.pack(pady=10)
    timed_entry.bind("<Return>", lambda event: check_timed_answer())
    timed_tip_label.pack(pady=5)
    timed_hint_button.pack(pady=5)
    timed_hint_label.pack()
    timed_feedback.pack(pady=10)
    retry_button_timed.pack_forget()
    timed_back_button.pack(pady=20)
    next_timed_question()

# ======== Practice Mode Logic ========
def show_quiz():
    main_menu.pack_forget()
    quiz_frame.pack(expand=True, fill="both")
    next_question()

def next_question():
    global x, y, correct
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    correct = x * y
    message_question.configure(text=f"{x} x {y}")
    entry.delete(0, ctk.END)
    feedback_label.configure(text="")
    hint_label.configure(text="")
    retry_button.pack_forget()

def show_hint():
    hint_label.configure(text=f"Hint: The answer is {correct}")

def check_answer():
    global correct
    user_input = entry.get()
    if user_input == "":
        feedback_label.configure(text="Please enter a number", text_color="orange")
        return
    if user_input.startswith("0") and len(user_input) > 1:
        user_input = user_input.lstrip("0")
        if user_input == "":
            user_input = "0"
    try:
        user_answer = int(user_input)
    except ValueError:
        feedback_label.configure(text="Please enter a number", text_color="orange")
        entry.delete(0, ctk.END)
        return

    if user_answer == correct:
        feedback_label.configure(text="Good job!", text_color="green")
    else:
        feedback_label.configure(text=f"Unlucky, the answer was {correct}", text_color="red")
    retry_button.pack(pady=10, before=back_button)

# ======== Timed Mode Logic ========
def show_timed_quiz():
    global score, question_num, remaining_time, timer_running
    score = 0
    question_num = 0
    remaining_time = total_time
    timer_running = False
    score_label.configure(text="Score: 0")
    time_progress.set(1.0)
    main_menu.pack_forget()  # Hide the main menu frame
    timed_quiz_frame.pack(expand=True, fill="both")
    # Unpack both buttons to reset packing order
    ready_button.pack_forget()
    timed_back_button.pack_forget()
    # Pack buttons in correct order
    ready_button.pack(pady=100)
    timed_back_button.pack(pady=10)
    # Hide other widgets
    timed_question.pack_forget()
    timed_entry_label.pack_forget()
    timed_entry.pack_forget()
    time_label.pack_forget()
    time_progress.pack_forget()
    score_label.pack_forget()
    timed_feedback.pack_forget()
    timed_tip_label.pack_forget()
    timed_hint_button.pack_forget()
    timed_hint_label.pack_forget()
    retry_button_timed.pack_forget()

def next_timed_question():
    global x, y, correct, remaining_time, timer_running, question_num
    if question_num >= max_questions:
        timed_feedback.configure(text=f"Quiz Complete! Final Score: {score}", text_color="cyan")
        retry_button_timed.pack_forget()
        timed_entry.unbind("<Return>")
        return

    x = random.randint(2, 9)
    y = random.randint(2, 9)
    correct = x * y
    timed_question.configure(text=f"{x} x {y}")
    timed_entry.delete(0, ctk.END)
    timed_feedback.configure(text="")
    timed_hint_label.configure(text="")
    retry_button_timed.pack_forget()
    remaining_time = total_time
    time_progress.set(1.0)
    timer_running = True
    question_num += 1
    timed_entry.unbind("<Return>")
    timed_entry.bind("<Return>", lambda event: check_timed_answer())
    start_timer()

def check_timed_answer():
    global correct, timer_running, score
    user_input = timed_entry.get()
    if user_input == "":
        timed_feedback.configure(text="Please enter a number", text_color="orange")
        return
    if user_input.startswith("0") and len(user_input) > 1:
        user_input = user_input.lstrip("0")
        if user_input == "":
            user_input = "0"
    try:
        user_answer = int(user_input)
    except ValueError:
        timed_feedback.configure(text="Please enter a number", text_color="orange")
        timed_entry.delete(0, ctk.END)
        return

    timer_running = False
    if timed_feedback.cget("text") == "":
        if user_answer == correct:
            score += 1
            score_label.configure(text=f"Score: {score}")
            timed_feedback.configure(text="Good job!", text_color="green")
        else:
            timed_feedback.configure(text=f"Unlucky, the answer was {correct}", text_color="red")
            score = 0
            score_label.configure(text=f"Score: {score}")
        retry_button_timed.pack(pady=10, before=timed_back_button)
        timed_entry.unbind("<Return>")

def show_timed_hint():
    timed_hint_label.configure(text=f"Hint: The answer is {correct}")

def start_timer():
    global remaining_time, timer_running
    if timer_running and remaining_time > 0:
        remaining_time -= 0.1
        time_progress.set(remaining_time / total_time)
        app.after(100, start_timer)
    elif remaining_time <= 0:
        timer_running = False
        time_progress.set(0.0)
        if timed_feedback.cget("text") == "":
            timed_feedback.configure(text=f"Time's up! The answer was {correct}", text_color="red")
            retry_button_timed.pack(pady=10, before=timed_back_button)
            timed_entry.unbind("<Return>")

# ======== Run ========
app.mainloop()