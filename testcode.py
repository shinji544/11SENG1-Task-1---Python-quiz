import customtkinter as ctk
import random
from PIL import Image, ImageTk, ImageEnhance
import os
import tkinter as tk

# ======== Paths to PNG Icons ========
script_dir = os.path.dirname(os.path.abspath(__file__))
sun_path = os.path.join(script_dir, "sun.png")
moon_path = os.path.join(script_dir, "moon.png")
bg_path = os.path.join(script_dir, "background.png")
home_path = os.path.join(script_dir, "home.png")
play_path = os.path.join(script_dir, "play-button.png")
quit_path = os.path.join(script_dir, "door.png")
hint_path = os.path.join(script_dir, "hints.png")
play_arrow_path = os.path.join(script_dir, "play-button-arrowhead.png")
back_path = os.path.join(script_dir, "turn-back.png")
close_path = os.path.join(script_dir, "close.png")
settings_path = os.path.join(script_dir, "settings.png")
settings_tab_path = os.path.join(script_dir, "boxbox_settings.png")
tab_frame_path = os.path.join(script_dir, "boxbox_title.png")
practice_frame_path = os.path.join(script_dir, "boxbox_practice_test.png")
timed_frame_path = os.path.join(script_dir, "boxbox_timed_test.png")
tab_frame_fullscreen_path = os.path.join(script_dir, "boxbox_fullscreen.png")
dark_tab_frame_fullscreen_path = os.path.join(script_dir, "boxbox_fullscreen_darkmode.png")
dark_tab_frame_path = os.path.join(script_dir, "boxbox - dark mode.png")

sun_icon = ctk.CTkImage(light_image=Image.open(sun_path), size=(32, 32))
moon_icon = ctk.CTkImage(light_image=Image.open(moon_path), size=(32, 32))
play_arrow_icon = ctk.CTkImage(light_image=Image.open(play_arrow_path), size=(18, 18))
back_icon = ctk.CTkImage(light_image=Image.open(back_path), size=(18, 18))
close_icon = ctk.CTkImage(light_image=Image.open(close_path), size=(20, 20))
settings_icon = ctk.CTkImage(light_image=Image.open(settings_path), size=(36, 36))

# ======== App Setup ========
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Multiplication Quiz Game")
app.geometry("800x600")

# Set the window icon using home.png
icon1_tk = tk.PhotoImage(file=home_path)
app.iconphoto(False, icon1_tk)

# Load background images
bg_image = Image.open(bg_path)
brightness_factor = 0.7
contrast_factor = 1.5
enhancer_brightness = ImageEnhance.Brightness(bg_image)
brightened_image = enhancer_brightness.enhance(brightness_factor)
enhancer_contrast = ImageEnhance.Contrast(brightened_image)
adjusted_background = enhancer_contrast.enhance(contrast_factor)
bg_ctk_image = ctk.CTkImage(light_image=adjusted_background, size=(800, 600))
bg_label = ctk.CTkLabel(app, image=bg_ctk_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

quiz_bg_image = ctk.CTkImage(light_image=Image.open(tab_frame_fullscreen_path), size=(800, 600))
quiz_bg_label = ctk.CTkLabel(app, image=quiz_bg_image, text="")

practice_frame_image = ctk.CTkImage(light_image=Image.open(practice_frame_path), size=(350, 300))
timed_frame_image = ctk.CTkImage(light_image=Image.open(timed_frame_path), size=(350, 300))

# ======== Fonts & Colors ========
title_font = ctk.CTkFont(family="Segoe UI", size=32, weight="bold")
button_font = ctk.CTkFont(family="Segoe UI", size=16)
label_font = ctk.CTkFont(family="Segoe UI", size=20)
small_font = ctk.CTkFont(family="Segoe UI", size=12)
accent_color = "#1E90FF"
entry_bg = "#F0F0F0"

light_text = "black"
dark_text = "white"

# ======== All functions ========

# ======== Theme Toggle Function ========
def toggle_theme():
    global current_theme
    if current_theme == "dark":
        current_theme = "light"
        ctk.set_appearance_mode("light")
        #theme_button.configure(image=sun_icon)
        theme_button2.configure(image=moon_icon)
        update_text_colors(light_text)
        bg_label.configure(image=bg_ctk_image)
        quiz_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(tab_frame_fullscreen_path), size=(800, 600)))
        tab_frame.configure(image=ctk.CTkImage(light_image=Image.open(tab_frame_path), size=(450, 400)))
        practice_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(practice_frame_path), size=(350, 300)))
        timed_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(timed_frame_path), size=(350, 300)))
        print("Theme switched to: light")
    else:
        current_theme = "dark"
        ctk.set_appearance_mode("dark")
        #theme_button.configure(image=moon_icon)
        theme_button2.configure(image=sun_icon)
        update_text_colors(dark_text)
        bg_label.configure(image=bg_ctk_image)
        quiz_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(dark_tab_frame_fullscreen_path), size=(800, 600)))
        tab_frame.configure(image=ctk.CTkImage(light_image=Image.open(dark_tab_frame_path), size=(450, 400)))
        practice_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(dark_tab_frame_path), size=(350, 300)))
        timed_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(dark_tab_frame_path), size=(350, 300)))
        print("Theme switched to: dark")

def update_text_colors(color):
    message_question.configure(text_color=color)
    entry_label.configure(text_color=color)
    hint_label.configure(text_color="gray")
    tip_label.configure(text_color="gray")
    feedback_label.configure(text_color=color)
    timed_question.configure(text_color=color)
    timed_feedback.configure(text_color=color)
    score_label.configure(text_color=color)
    menu_button.configure(text_color=color)
    timed_back_button.configure(text_color=color)
    # quiz_close_button.configure(text_color=color)

# ======== Dragging Frames ========
def start_drag(event, widget):
    global drag_offset_x, drag_offset_y
    drag_offset_x = event.x_root - widget.winfo_x()
    drag_offset_y = event.y_root - widget.winfo_y()

def do_drag(event, widget):
    new_x = event.x_root - drag_offset_x
    new_y = event.y_root - drag_offset_y
    widget.place(x=new_x, y=new_y)

def unbind_drag(widget):
    widget.unbind("<Button-1>")
    widget.unbind("<B1-Motion>")

def bind_drag(widget):
    widget.bind("<Button-1>", lambda event: start_drag(event, widget))
    widget.bind("<B1-Motion>", lambda event: do_drag(event, widget))

# ======== Navigation ========

def show_settings():
    settings_frame.place(relx=0.5, rely=0.5, anchor="center")
    settings_close_button.place(x=140, y=13)
    bind_drag(settings_frame)

def close_settings():
    settings_frame.place_forget()
    unbind_drag(settings_frame)

def goto_main_menu():
    title_menu.place_forget()
    tab_frame.place_forget()
    quiz_bg_label.place_forget()
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    practice_tab_frame.place(relx=0.25, rely=0.5, anchor="center")
    timed_tab_frame.place(relx=0.75, rely=0.5, anchor="center")
    menu_button.place(relx=0.5, rely=0.75, anchor="center")
    theme_button2.place(relx=0.05, rely=0.05)
    unbind_drag(tab_frame)
    bind_drag(practice_tab_frame)
    bind_drag(timed_tab_frame)

def back_to_title():
    practice_tab_frame.place_forget()
    timed_tab_frame.place_forget()
    menu_button.place_forget()
    theme_button2.place_forget()
    quiz_bg_label.place_forget()
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    title_menu.place(relx=0.5, rely=0.55, anchor="center")
    tab_frame.place(relx=0.5, rely=0.5, anchor="center")
    bind_drag(tab_frame)
    unbind_drag(practice_tab_frame)
    unbind_drag(timed_tab_frame)

def back_to_menu():
    for f in [quiz_frame, timed_quiz_frame]:
        f.place_forget()
    quiz_bg_label.place_forget()
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    practice_tab_frame.place(relx=0.25, rely=0.5, anchor="center")
    timed_tab_frame.place(relx=0.75, rely=0.5, anchor="center")
    menu_button.place(relx=0.5, rely=0.75, anchor="center")
    theme_button2.place(relx=0.05, rely=0.05)
    practice_close_button.place_forget()
    bind_drag(practice_tab_frame)
    bind_drag(timed_tab_frame)

def show_quiz():
    practice_tab_frame.place_forget()
    timed_tab_frame.place_forget()
    menu_button.place_forget()
    theme_button2.place_forget()
    bg_label.place_forget()
    quiz_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    quiz_frame.place(relx=0.5, rely=0.55, anchor="center")
    practice_close_button.place(x=160, y=15)
    unbind_drag(practice_tab_frame)
    unbind_drag(timed_tab_frame)
    next_question()

def show_timed_quiz():
    global score, question_num
    score = 0
    question_num = 0
    practice_tab_frame.place_forget()
    timed_tab_frame.place_forget()
    menu_button.place_forget()
    theme_button2.place_forget()
    quiz_bg_label.place_forget()
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    timed_quiz_frame.place(relx=0.5, rely=0.55, anchor="center")
    unbind_drag(practice_tab_frame)
    unbind_drag(timed_tab_frame)
    next_timed_question()

# ======== Practice Mode ========
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
    retry_button.pack(pady=10)

# ======== Timed Mode ========
def next_timed_question():
    global x, y, correct, question_num
    if question_num >= max_questions:
        timed_feedback.configure(text="Quiz Complete!", text_color="cyan")
        return

    x = random.randint(2, 9)
    y = random.randint(2, 9)
    correct = x * y
    timed_question.configure(text=f"{x} x {y}")
    timed_entry.delete(0, ctk.END)
    question_num += 1

def check_timed_answer():
    global score, correct
    user_input = timed_entry.get()
    try:
        user_answer = int(user_input)
    except ValueError:
        timed_feedback.configure(text="Invalid input", text_color="orange")
        return

    if user_answer == correct:
        score += 1
        timed_feedback.configure(text="Correct!", text_color="green")
    else:
        timed_feedback.configure(text=f"Wrong. It was {correct}.", text_color="red")

    score_label.configure(text=f"Score: {score}")
    app.after(1000, next_timed_question)

# ======== Variables ========
x = y = correct = 0
score = 0
question_num = 0
max_questions = 10
current_theme = "light"

# ======== Draggable Frames (Using PNGs) ========
tab_frame_image = ctk.CTkImage(light_image=Image.open(tab_frame_path), size=(450, 400))
tab_frame = ctk.CTkLabel(app, image=tab_frame_image, text="", fg_color="#1e1e2f")
tab_frame.place(relx=0.5, rely=0.5, anchor="center")

# ======== Settings Frame  ========
settings_frame_image = ctk.CTkImage(light_image=Image.open(settings_tab_path), size=(450, 400))
settings_frame = ctk.CTkLabel(app, image=settings_frame_image, text="", fg_color="#1e1e2f")
settings_close_button = ctk.CTkButton(settings_frame, text="", image=close_icon, width=20, height=20,
                                      fg_color="#E8E8E8", hover_color="#D0D0D0", command=lambda: close_settings())

settings_button = ctk.CTkButton(tab_frame, text="", image=settings_icon, width=10, height=10,
                             fg_color="#E8E8E8", hover=False, command=show_settings)
settings_button.place(x=380, y=60)

# --- Dragging Functionality ---
drag_offset_x = 0
drag_offset_y = 0

# Bind dragging to the title frame initially
bind_drag(tab_frame)

# Load icons for buttons
play_icon = ctk.CTkImage(light_image=Image.open(play_path), size=(100, 100))
quit_icon = ctk.CTkImage(light_image=Image.open(quit_path), size=(100, 100))

# ======== Title Menu (Inside Tab Frame PNG) ========
title_menu = ctk.CTkFrame(tab_frame, corner_radius=20, fg_color="transparent")
title_menu.place(relx=0.5, rely=0.55, anchor="center")

clean_button_fg = "#FFFFFF"
clean_button_hover = "#F0F0F0"

# Row container for Play and Quit buttons
button_row = ctk.CTkFrame(title_menu, fg_color="#E8E8E8")
button_row.pack(pady=1)

# Play button with label
play_frame = ctk.CTkFrame(button_row, fg_color="#E8E8E8")
play_frame.pack(side="left", padx=20)

play_button = ctk.CTkButton(play_frame, text="", image=play_icon, width=60, height=60,
                            fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                            command=lambda: goto_main_menu())
play_button.pack()

play_label = ctk.CTkLabel(play_frame, text="Play", font=("Helvetica", 14))
play_label.pack(pady=5)

# Quit button with label
quit_frame = ctk.CTkFrame(button_row, fg_color="transparent")
quit_frame.pack(side="left", padx=20)

quit_button = ctk.CTkButton(quit_frame, text="", image=quit_icon, width=60, height=60,
                            fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                            command=app.destroy)
quit_button.pack()

quit_label = ctk.CTkLabel(quit_frame, text="Quit", font=("Helvetica", 14))
quit_label.pack(pady=5)

# ======== Main Menu Widgets ========
theme_button2 = ctk.CTkButton(app, text="", image=moon_icon, width=10, height=10,
                              fg_color="transparent", hover=False, command=toggle_theme)

# Practice tab frame
practice_tab_frame = ctk.CTkFrame(app, width=350, height=300, corner_radius=0, fg_color="#1e1e2f")
practice_bg_label = ctk.CTkLabel(practice_tab_frame, image=practice_frame_image, text="")
practice_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

practice_menu = ctk.CTkFrame(practice_tab_frame, corner_radius=0, fg_color="#E8E8E8")
practice_menu.place(relx=0.5, rely=0.55, anchor="center")

practice_button = ctk.CTkButton(practice_menu, text="Play", font=button_font, width=220, height=45,
                                fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                                text_color="black", image=play_arrow_icon, compound="left", command=lambda: show_quiz())
practice_button.pack(pady=(40, 10))

# Timed tab frame
timed_tab_frame = ctk.CTkFrame(app, width=350, height=300, corner_radius=0, fg_color="#1e1e2f")
timed_bg_label = ctk.CTkLabel(timed_tab_frame, image=timed_frame_image, text="")
timed_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

timed_menu = ctk.CTkFrame(timed_tab_frame, corner_radius=0, fg_color="#E8E8E8")
timed_menu.place(relx=0.5, rely=0.55, anchor="center")

timed_button = ctk.CTkButton(timed_menu, text="Play", font=button_font, width=220, height=45,
                             fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                             text_color="black", image=play_arrow_icon, compound="left", command=lambda: start_countdown(show_timed_quiz))
timed_button.pack(pady=(40, 10))

menu_button = ctk.CTkButton(app, text="Go Back", font=button_font, width=220, height=45,
                            fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                            text_color="black", image=back_icon, compound="left", command=lambda: back_to_title())

# ======== Countdown Overlay ========
countdown_overlay = ctk.CTkFrame(app, fg_color="#000000", corner_radius=0)
countdown_label = ctk.CTkLabel(countdown_overlay, text="", font=ctk.CTkFont(size=72, weight="bold"), text_color="white")
countdown_label.pack(expand=True)

def start_countdown(callback):
    practice_tab_frame.place_forget()
    timed_tab_frame.place_forget()
    menu_button.place_forget()
    theme_button2.place_forget()
    countdown_overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
    countdown_step(3, callback)

def countdown_step(count, callback):
    if count > 0:
        countdown_label.configure(text=str(count))
        app.after(1000, lambda: countdown_step(count - 1, callback))
    else:
        countdown_label.configure(text="GO!")
        app.after(1000, lambda: end_countdown(callback))

def end_countdown(callback):
    countdown_overlay.place_forget()
    callback()

# ======== Quiz Frame (Practice) ========
quiz_frame = ctk.CTkFrame(app, corner_radius=20, fg_color="transparent")

message_question = ctk.CTkLabel(quiz_frame, text="", font=label_font, text_color="black")
entry_label = ctk.CTkLabel(quiz_frame, text="Answer:", font=button_font, text_color="black")
entry = ctk.CTkEntry(quiz_frame, font=button_font, text_color="black", fg_color=entry_bg,
                     border_color=accent_color, border_width=2, corner_radius=8)
hint_label = ctk.CTkLabel(quiz_frame, text="", text_color="gray")
tip_label = ctk.CTkLabel(quiz_frame, text="Tip: Press Enter to submit", font=small_font, text_color="gray")
feedback_label = ctk.CTkLabel(quiz_frame, text="", font=button_font, text_color="black")
retry_button = ctk.CTkButton(quiz_frame, text="Try Again?", font=button_font,
                             fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                             text_color="black", command=lambda: next_question())
hint_button = ctk.CTkButton(quiz_frame, text="Hint", font=button_font,
                            fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                            text_color="black", command=lambda: show_hint())

# Close button for practice_tab_frame (positioned in the red circle)
practice_close_button = ctk.CTkButton(app, text="", image=close_icon, width=20, height=20,
                                      fg_color="#E8E8E8", hover_color="#D0D0D0", command=lambda: back_to_menu())

message_question.pack(pady=30)
entry_label.pack()
entry.pack(pady=(5, 15))
entry.bind("<Return>", lambda event: check_answer())
hint_button.pack(pady=5)
hint_label.pack()
tip_label.pack(pady=5)
feedback_label.pack(pady=10)
retry_button.pack_forget()

# ======== Timed Quiz Frame ========
timed_quiz_frame = ctk.CTkFrame(app, corner_radius=20, fg_color="transparent")

timed_question = ctk.CTkLabel(timed_quiz_frame, text="", font=label_font, text_color="black")
timed_entry = ctk.CTkEntry(timed_quiz_frame, font=button_font, text_color="black", fg_color=entry_bg,
                           border_color=accent_color, border_width=2, corner_radius=8)
timed_feedback = ctk.CTkLabel(timed_quiz_frame, text="", font=button_font, text_color="black")
score_label = ctk.CTkLabel(timed_quiz_frame, text="Score: 0", font=button_font, text_color="black")
timed_back_button = ctk.CTkButton(timed_quiz_frame, text="Back to Menu", font=button_font,
                                  fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                                  text_color="black", command=lambda: back_to_menu())

timed_question.pack(pady=30)
timed_entry.pack(pady=10)
timed_entry.bind("<Return>", lambda event: check_timed_answer())
timed_feedback.pack(pady=10)
score_label.pack(pady=10)
timed_back_button.pack(pady=20)

# ======== Run App ========
title_menu.place(relx=0.5, rely=0.55, anchor="center")
app.mainloop()