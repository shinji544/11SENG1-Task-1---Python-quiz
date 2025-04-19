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
practice_path = os.path.join(script_dir, "pencil.png")
timed_path = os.path.join(script_dir, "back-in-time.png")
play_arrow_path = os.path.join(script_dir, "play-button-arrowhead.png")
back_path = os.path.join(script_dir, "turn-back.png")
settings_path = os.path.join(script_dir, "settings.png")
tab_frame_path = os.path.join(script_dir, "boxbox.png")
dark_tab_frame_path = os.path.join(script_dir, "boxbox - dark mode.png")

sun_icon = ctk.CTkImage(light_image=Image.open(sun_path), size=(32, 32))
moon_icon = ctk.CTkImage(light_image=Image.open(moon_path), size=(32, 32))
play_arrow_icon = ctk.CTkImage(light_image=Image.open(play_arrow_path), size=(18, 18))
back_icon = ctk.CTkImage(light_image=Image.open(back_path), size=(18, 18))

# ======== App Setup ========
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Multiplication Quiz Game")
app.geometry("800x600")

# Set the window icon using icon1 (home.png)
icon1_tk = tk.PhotoImage(file=home_path)
app.iconphoto(False, icon1_tk)

# Load background image and adjust brightness and contrast
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

# ======== Fonts & Colors ========
title_font = ctk.CTkFont(family="Segoe UI", size=32, weight="bold")
button_font = ctk.CTkFont(family="Segoe UI", size=16)
label_font = ctk.CTkFont(family="Segoe UI", size=20)
small_font = ctk.CTkFont(family="Segoe UI", size=12)
smaller_tab_header_font = ctk.CTkFont(family="Segoe UI", size=12)
accent_color = "#1E90FF"
entry_bg = "#F0F0F0"

light_text = "black"
dark_text = "white"

# ======== Theme Toggle Function ========
def toggle_theme():
    global current_theme
    if current_theme == "dark":
        current_theme = "light"
        ctk.set_appearance_mode("light")
        theme_button.configure(image=sun_icon)
        theme_button2.configure(image=moon_icon)
        update_text_colors(light_text)
        print("Theme switched to: light")
    else:
        current_theme = "dark"
        ctk.set_appearance_mode("dark")
        theme_button.configure(image=moon_icon)
        theme_button2.configure(image=sun_icon)
        update_text_colors(dark_text)
        print("Theme switched to: dark")

def update_text_colors(color):
    title_label.configure(text_color=color)
    #main_label.configure(text_color=color)
    message_question.configure(text_color=color)
    entry_label.configure(text_color=color)
    hint_label.configure(text_color="gray")
    tip_label.configure(text_color="gray")
    feedback_label.configure(text_color=color)
    timed_question.configure(text_color=color)
    timed_feedback.configure(text_color=color)
    score_label.configure(text_color=color)
    tab_header_label.configure(text_color=color)  # Reintroduce for theme updates

# ======== Variables ========
x = y = correct = 0
score = 0
question_num = 0
max_questions = 10

current_theme = "light"

tab_frame_image = ctk.CTkImage(light_image=Image.open(tab_frame_path), size=(600, 400))  # Match original tab_frame size

# Create the tab frame as a CTkLabel with the PNG as the background
tab_frame = ctk.CTkLabel(app, image=tab_frame_image, text="")
tab_frame.place(relx=0.5, rely=0.5, anchor="center")

# Load the home icon for the tab header
home_icon = ctk.CTkImage(light_image=Image.open(home_path), size=(20, 20))  # Smaller size for tab header

# Add the "Title page" label with the home icon on the tab frame (in the tab header area)
tab_header_label = ctk.CTkLabel(tab_frame, text=" Title page", font=button_font, text_color="black",
                                image=home_icon, compound="left")
tab_header_label.place(x=20, y=8)  # Position in the dark gray tab area

# --- Improved Dragging Functionality ---
drag_offset_x = 0
drag_offset_y = 0

def start_drag(event, widget):
    global drag_offset_x, drag_offset_y
    # Calculate offset relative to the widget's current position
    drag_offset_x = event.x_root
    drag_offset_y = event.y_root 

def do_drag(event, widget):
    # Move the widget to the new position based on current mouse position and offset
    new_x = event.x_root - drag_offset_x
    new_y = event.y_root - drag_offset_y
    widget.place(x=new_x, y=new_y)

def unbind_drag(widget, header_label):
    widget.unbind("<Button-1>")
    widget.unbind("<B1-Motion>")
    header_label.unbind("<Button-1>")
    header_label.unbind("<B1-Motion>")

# Helper function to bind drag events to a widget and its header label
def bind_drag(widget, header_label):
    widget.bind("<Button-1>", lambda event: start_drag(event, widget))
    widget.bind("<B1-Motion>", lambda event: do_drag(event, widget))
    header_label.bind("<Button-1>", lambda event: start_drag(event, widget))
    header_label.bind("<B1-Motion>", lambda event: do_drag(event, widget))

# Bind dragging to the tab_frame and the tab_header_label initially
bind_drag(tab_frame, tab_header_label)

# Load icons for other uses
play_icon = ctk.CTkImage(light_image=Image.open(play_path), size=(100, 100))
quit_icon = ctk.CTkImage(light_image=Image.open(quit_path), size=(100, 100))

# ======== Title Menu (Inside Tab Frame PNG) ========
title_menu = ctk.CTkFrame(tab_frame, corner_radius=20, fg_color="transparent")
title_menu.place(relx=0.5, rely=0.55, anchor="center")  # Adjusted rely to fit within the light gray area

theme_button = ctk.CTkButton(title_menu, text="", image=moon_icon, width=10, height=10,
                             fg_color="transparent", hover=False, command=toggle_theme)
theme_button.place(x=20, y=20)

title_label = ctk.CTkLabel(title_menu, text="Multiplication Quiz", font=title_font, text_color="black")
title_label.pack(pady=(60, 40))

clean_button_fg = "#FFFFFF"
clean_button_hover = "#F0F0F0"

# Row container to hold the Play and Quit sections side by side
button_row = ctk.CTkFrame(title_menu, fg_color="transparent")
button_row.pack(pady=10)

# Play button with label below
play_frame = ctk.CTkFrame(button_row, fg_color="transparent")
play_frame.pack(side="left", padx=20)

play_button = ctk.CTkButton(play_frame, text="", image=play_icon, width=60, height=60,
                            fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                            command=lambda: goto_main_menu())
play_button.pack()

play_label = ctk.CTkLabel(play_frame, text="Play", font=("Helvetica", 14))
play_label.pack(pady=5)

# Quit button with label below
quit_frame = ctk.CTkFrame(button_row, fg_color="transparent")
quit_frame.pack(side="left", padx=20)

quit_button = ctk.CTkButton(quit_frame, text="", image=quit_icon, width=60, height=60,
                            fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                            command=app.destroy)
quit_button.pack()

quit_label = ctk.CTkLabel(quit_frame, text="Quit", font=("Helvetica", 14))
quit_label.pack(pady=5)

# ======== Main Menu ========
main_menu = ctk.CTkFrame(tab_frame, corner_radius=20, fg_color="transparent")
# main_menu.place(relx=0.5, rely=0.55, anchor="center")

mm_tab_frame_image = ctk.CTkImage(light_image=Image.open(tab_frame_path), size=(300, 200))  # Match original tab_frame size

theme_button2 = ctk.CTkButton(main_menu, text="", image=moon_icon, width=10, height=10,
                              fg_color="transparent", hover=False, command=toggle_theme)
theme_button2.place(x=20, y=20)

# Practice tab frame (CTkFrame with sub-frame for content)
practice_tab_frame = ctk.CTkFrame(app, width=300, height=200, corner_radius=0, fg_color="transparent")
practice_bg_label = ctk.CTkLabel(practice_tab_frame, image=mm_tab_frame_image, text="")
practice_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

practice_icon = ctk.CTkImage(light_image=Image.open(practice_path), size=(18, 18))
practice_tab_header_label = ctk.CTkLabel(practice_tab_frame, text=" Practice questions", font=smaller_tab_header_font, text_color="black",
                                        image=practice_icon, compound="left")
practice_tab_header_label.place(x=8, y=1)

# Sub-frame to hold the button (inspired by title_menu)
practice_menu = ctk.CTkFrame(practice_tab_frame, corner_radius=20, fg_color="transparent")
practice_menu.place(relx=0.5, rely=0.55, anchor="center")

practice_button = ctk.CTkButton(practice_menu, text="Play", font=button_font, width=220, height=45,
                                fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                                text_color="black", image=play_arrow_icon, compound="left", command=lambda: show_quiz())
practice_button.pack(pady=(40, 10))  # Adjusted padding to fit smaller frame

# Timed tab frame (CTkFrame with sub-frame for content)
timed_tab_frame = ctk.CTkFrame(app, width=300, height=200, corner_radius=0, fg_color="transparent")
timed_bg_label = ctk.CTkLabel(timed_tab_frame, image=mm_tab_frame_image, text="")
timed_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

timed_icon = ctk.CTkImage(light_image=Image.open(timed_path), size=(18, 18))
timed_tab_header_label = ctk.CTkLabel(timed_tab_frame, text=" Timed questions", font=smaller_tab_header_font, text_color="black",
                                     image=timed_icon, compound="left")
timed_tab_header_label.place(x=8, y=1)

# Sub-frame to hold the button (inspired by title_menu)
timed_menu = ctk.CTkFrame(timed_tab_frame, corner_radius=20, fg_color="transparent")
timed_menu.place(relx=0.5, rely=0.55, anchor="center")

timed_button = ctk.CTkButton(timed_menu, text="Play", font=button_font, width=220, height=45,
                             fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                             text_color="black", image=play_arrow_icon, compound="left", command=lambda: start_countdown(show_timed_quiz))
timed_button.pack(pady=(40, 10))  # Adjusted padding to fit smaller frame

menu_button = ctk.CTkButton(app, text="Go Back", font=button_font, width=220, height=45,
                            fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                            text_color="black", image=back_icon, compound="left", command=lambda: back_to_title())


# ======== Countdown Overlay ========
countdown_overlay = ctk.CTkFrame(app, fg_color="#000000", corner_radius=0)
countdown_label = ctk.CTkLabel(countdown_overlay, text="", font=ctk.CTkFont(size=72, weight="bold"), text_color="white")
countdown_label.pack(expand=True)

def start_countdown(callback):
    main_menu.place_forget()
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
quiz_frame = ctk.CTkFrame(tab_frame, corner_radius=20, fg_color="transparent")
# quiz_frame.place(relx=0.5, rely=0.55, anchor="center")

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
back_button = ctk.CTkButton(quiz_frame, text="Back to Menu", font=button_font,
                            fg_color=clean_button_fg, hover_color=clean_button_hover, corner_radius=10,
                            text_color="black", command=lambda: back_to_menu())

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
timed_quiz_frame = ctk.CTkFrame(tab_frame, corner_radius=20, fg_color="transparent")
# timed_quiz_frame.place(relx=0.5, rely=0.55, anchor="center")

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

# ======== Navigation ========
def goto_main_menu():
    title_menu.place_forget()
    main_menu.place(relx=0.5, rely=0.55, anchor="center")
    tab_frame.place_forget()

    practice_tab_frame.place(relx=0.25, rely=0.5, anchor="center")
    timed_tab_frame.place(relx=0.75, rely=0.5, anchor="center")
    menu_button.place(relx=0.5, rely=0.75, anchor="center")

    unbind_drag(tab_frame, tab_header_label)
    bind_drag(practice_tab_frame, practice_tab_header_label)
    bind_drag(timed_tab_frame, timed_tab_header_label)


def back_to_title():
    main_menu.place_forget()
    practice_tab_frame.place_forget()
    timed_tab_frame.place_forget()
    menu_button.place_forget()  # Hide back button
    title_menu.place(relx=0.5, rely=0.55, anchor="center")
    tab_frame.place(relx=0.5, rely=0.5, anchor="center")
    bind_drag(tab_frame, tab_header_label)

def back_to_menu():
    for f in [quiz_frame, timed_quiz_frame]:
        f.place_forget()
    main_menu.place(relx=0.5, rely=0.55, anchor="center")

# ======== Practice Mode ========
def show_quiz():
    main_menu.place_forget()
    quiz_frame.place(relx=0.5, rely=0.55, anchor="center")
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

# ======== Timed Mode ========
def show_timed_quiz():
    global score, question_num
    score = 0
    question_num = 0
    main_menu.place_forget()
    timed_quiz_frame.place(relx=0.5, rely=0.55, anchor="center")
    next_timed_question()

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

# ======== Run App ========
title_menu.place(relx=0.5, rely=0.55, anchor="center")
app.mainloop()