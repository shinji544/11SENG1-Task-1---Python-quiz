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
play_arrow_path = os.path.join(script_dir, "play-button-arrowhead.png")
back_path = os.path.join(script_dir, "turn-back.png")
close_path = os.path.join(script_dir, "close.png")
hint_path = os.path.join(script_dir, "hints.png")
settings_path = os.path.join(script_dir, "settings.png")
settings_tab_path = os.path.join(script_dir, "boxbox_settings.png")
dark_settings_tab_path = os.path.join(script_dir, "boxbox_settings_dark.png")
tab_frame_path = os.path.join(script_dir, "boxbox_title.png")
dark_tab_frame_path = os.path.join(script_dir, "boxbox_title_dark.png")
practice_frame_path = os.path.join(script_dir, "boxbox_practice.png")
dark_practice_frame_path = os.path.join(script_dir, "boxbox_practice_dark.png")
timed_frame_path = os.path.join(script_dir, "boxbox_timed.png")
dark_timed_frame_path = os.path.join(script_dir, "boxbox_timed_dark.png")
tab_frame_fullscreen_path = os.path.join(script_dir, "boxbox_fullscreen.png")
dark_tab_frame_fullscreen_path = os.path.join(script_dir, "boxbox_fullscreen_darkmode.png")
timed_tab_frame_fullscreen_path = os.path.join(script_dir, "boxbox_timed_fullscreen.png")
dark_timed_tab_frame_fullscreen_path = os.path.join(script_dir, "boxbox_timed_fullscreen_dark.png")
answer_box_path = os.path.join(script_dir, "answer_box.png")  

# Load icons
sun_icon = ctk.CTkImage(light_image=Image.open(sun_path), size=(32, 32))
moon_icon = ctk.CTkImage(light_image=Image.open(moon_path), size=(32, 32))
play_arrow_icon = ctk.CTkImage(light_image=Image.open(play_arrow_path), size=(18, 18))
back_icon = ctk.CTkImage(light_image=Image.open(back_path), size=(18, 18))
close_icon = ctk.CTkImage(light_image=Image.open(close_path), size=(20, 20))
hint_icon = ctk.CTkImage(light_image=Image.open(hint_path), size=(30, 30))
settings_icon = ctk.CTkImage(light_image=Image.open(settings_path), size=(36, 36))
answer_box = ctk.CTkImage(light_image=Image.open(answer_box_path), size=(792, 82))
play_icon = ctk.CTkImage(light_image=Image.open(play_path), size=(100, 100))
quit_icon = ctk.CTkImage(light_image=Image.open(quit_path), size=(100, 100))

# ======== App Setup ========
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Multiplication Quiz Game")
app.geometry("800x600")

# Set window icon
icon_tk = tk.PhotoImage(file=home_path)
app.iconphoto(False, icon_tk)

# Load and adjust background image
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

# Quiz background
quiz_bg_image = ctk.CTkImage(light_image=Image.open(tab_frame_fullscreen_path), size=(800, 600))
quiz_bg_label = ctk.CTkLabel(app, image=quiz_bg_image, text="")

# Timed quiz background
timed_quiz_bg_image = ctk.CTkImage(light_image=Image.open(timed_tab_frame_fullscreen_path), size=(800, 600))
timed_quiz_bg_label = ctk.CTkLabel(app, image=timed_quiz_bg_image, text="")

# Frame images
practice_frame_image = ctk.CTkImage(light_image=Image.open(practice_frame_path), size=(350, 300))
timed_frame_image = ctk.CTkImage(light_image=Image.open(timed_frame_path), size=(350, 300))

# ======== Fonts & Colors ========
title_font = ctk.CTkFont(family="Segoe UI", size=32, weight="bold")
button_font = ctk.CTkFont(family="Segoe UI", size=16)
label_font = ctk.CTkFont(family="Segoe UI", size=20)
small_font = ctk.CTkFont(family="Segoe UI", size=12)
accent_color = "#1E90FF"
entry_bg = "#F0F0F0"
light_bg = "#E8E8E8"  # Light mode background
dark_bg = "#272727"   # Dark mode background
light_text = "black"
dark_text = "white"
hover_light = "#D0D0D0"
hover_dark = "#3A3A3A"

# ======================== All Functions ========================
# ======== Theme Toggle Function ========
current_theme = "light"

def toggle_theme():
    global current_theme
    new_bg_color = light_bg if current_theme == "dark" else dark_bg
    new_text_color = light_text if current_theme == "dark" else dark_text
    new_hover_color = hover_light if current_theme == "dark" else hover_dark

    if current_theme == "dark":
        current_theme = "light"
        ctk.set_appearance_mode("light")
        theme_button.configure(image=moon_icon)
        quiz_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(tab_frame_fullscreen_path), size=(800, 600)))
        timed_quiz_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(timed_tab_frame_fullscreen_path), size=(800, 600)))
        tab_frame.configure(image=ctk.CTkImage(light_image=Image.open(tab_frame_path), size=(450, 400)))
        practice_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(practice_frame_path), size=(350, 300)))
        timed_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(timed_frame_path), size=(350, 300)))
        settings_frame.configure(image=ctk.CTkImage(light_image=Image.open(settings_tab_path), size=(450, 400)))
    else:
        current_theme = "dark"
        ctk.set_appearance_mode("dark")
        theme_button.configure(image=sun_icon)
        quiz_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(dark_tab_frame_fullscreen_path), size=(800, 600)))
        timed_quiz_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(dark_timed_tab_frame_fullscreen_path), size=(800, 600)))
        tab_frame.configure(image=ctk.CTkImage(light_image=Image.open(dark_tab_frame_path), size=(450, 400)))
        practice_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(dark_practice_frame_path), size=(350, 300)))
        timed_bg_label.configure(image=ctk.CTkImage(light_image=Image.open(dark_timed_frame_path), size=(350, 300)))
        settings_frame.configure(image=ctk.CTkImage(light_image=Image.open(dark_settings_tab_path), size=(450, 400)))

    # Update fg_color for frames
    for widget in [title_menu, button_row, play_frame, quit_frame, practice_menu, timed_menu,
                   quiz_frame, timed_quiz_frame, settings_menu, practice_tab_frame, timed_tab_frame,
                   countdown_overlay, answer_frame, timed_answer_frame]:
        widget.configure(fg_color=new_bg_color)

    # Update fg_color for buttons 
    for button in [play_button, quit_button, practice_close_button, settings_button, settings_close_button, theme_button, retry_button]:
        button.configure(fg_color=new_bg_color, hover_color=new_hover_color)

    # Update fg_color for answer_entry and timed_answer_entry
    answer_entry.configure(fg_color=new_bg_color)
    timed_answer_entry.configure(fg_color=new_bg_color)

    # Update text colors for labels
    for label in [play_label, quit_label, message_question, feedback_label, timed_question, timed_feedback, score_label, final_score_label]:
        label.configure(text_color=new_text_color)

    # Update progress bar colors
    progress_bar.configure(fg_color="#D3D3D3" if current_theme == "light" else "#4A4A4A")
    progress_bar.configure(progress_color="#4CAF50")  # Reset to green

    # Update mode selection frame
    mode_select_frame.configure(fg_color=new_bg_color)
    mode_select_label.configure(text_color=new_text_color)
    for button in [ten_questions_button, infinite_mode_button]:
        button.configure(fg_color=new_bg_color, hover_color=new_hover_color, text_color=new_text_color)

# ======== Dragging Frames ========
drag_offset_x = 0
drag_offset_y = 0

def start_drag(event, widget):
    global drag_offset_x, drag_offset_y
    drag_offset_x = event.x_root - widget.winfo_x()
    drag_offset_y = event.y_root - widget.winfo_y()

def do_drag(event, widget):
    new_x = event.x_root - drag_offset_x
    new_y = event.y_root - drag_offset_y
    widget.place(x=new_x, y=new_y)

def bind_drag(widget):
    widget.bind("<Button-1>", lambda event: start_drag(event, widget))
    widget.bind("<B1-Motion>", lambda event: do_drag(event, widget))

def unbind_drag(widget):
    widget.unbind("<Button-1>")
    widget.unbind("<B1-Motion>")

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
    timed_quiz_bg_label.place_forget()  
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    practice_tab_frame.place(relx=0.25, rely=0.5, anchor="center")
    timed_tab_frame.place(relx=0.75, rely=0.5, anchor="center")
    menu_button.place(relx=0.5, rely=0.8, anchor="center")
    unbind_drag(tab_frame)
    bind_drag(practice_tab_frame)
    bind_drag(timed_tab_frame)

def back_to_title():
    practice_tab_frame.place_forget()
    timed_tab_frame.place_forget()
    menu_button.place_forget()
    quiz_bg_label.place_forget()
    timed_quiz_bg_label.place_forget()  
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    title_menu.place(relx=0.5, rely=0.55, anchor="center")
    tab_frame.place(relx=0.5, rely=0.5, anchor="center")
    bind_drag(tab_frame)
    unbind_drag(practice_tab_frame)
    unbind_drag(timed_tab_frame)

def back_to_menu():
    stop_timer()
    quiz_frame.place_forget()
    timed_quiz_frame.place_forget()
    mode_select_frame.place_forget()
    quiz_bg_label.place_forget()
    timed_quiz_bg_label.place_forget()  
    answer_entry.place_forget()
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  
    practice_tab_frame.place(relx=0.25, rely=0.5, anchor="center")
    timed_tab_frame.place(relx=0.75, rely=0.5, anchor="center")
    menu_button.place(relx=0.5, rely=0.8, anchor="center")
    practice_close_button.place_forget()
    timed_entry.configure(state="normal")
    timed_hint_button.configure(state="normal")
    bind_drag(practice_tab_frame)
    bind_drag(timed_tab_frame)

def show_quiz():
    practice_tab_frame.place_forget()
    timed_tab_frame.place_forget()
    menu_button.place_forget()
    bg_label.place_forget()
    timed_quiz_bg_label.place_forget()  
    quiz_bg_label.place(x=0, y=0, relwidth=1, relheight=1)  
    quiz_frame.place(relx=0.5, rely=0.55, anchor="center")
    practice_close_button.place(x=160, y=15)
    unbind_drag(practice_tab_frame)
    unbind_drag(timed_tab_frame)
    next_question()

def show_timed_quiz(infinite=False):
    global score, question_num, time_left, infinite_mode
    score = 0
    question_num = 0
    time_left = time_per_question
    infinite_mode = infinite
    quiz_bg_label.place_forget()
    bg_label.place_forget()
    timed_quiz_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    timed_quiz_frame.place(relx=0.5, rely=0.55, anchor="center")
    practice_close_button.place(x=160, y=15)
    unbind_drag(practice_tab_frame)
    unbind_drag(timed_tab_frame)
    timed_entry.configure(state="normal")
    timed_hint_button.configure(state="normal")
    score_label.configure(text=f"Score: {score}")
    progress_bar.set(1.0)
    progress_bar.configure(progress_color="#4CAF50")
    final_score_label.place_forget()  
    retry_button.place_forget()  
    timed_feedback.configure(text="")  
    progress_bar.pack(pady=10)
    score_label.pack(pady=10)
    timed_entry.bind("<Return>", lambda event: check_timed_answer())
    start_timer()
    next_timed_question()

def show_mode_select():
    practice_tab_frame.place_forget()
    timed_tab_frame.place_forget()
    menu_button.place_forget()
    bg_label.place_forget()  
    timed_quiz_bg_label.place(x=0, y=0, relwidth=1, relheight=1)  
    practice_close_button.place(x=160, y=15)
    mode_select_frame.place(relx=0.5, rely=0.5, anchor="center")

# ======== Practice Mode ========
x = y = correct = 0

def next_question():
    global x, y, correct
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    correct = x * y
    message_question.configure(text=f"{x} x {y}")
    entry.delete(0, ctk.END)
    feedback_label.configure(text="")
    retry_practice_button.pack_forget()

def show_hint():
    if quiz_frame.winfo_ismapped():
        feedback_label.configure(text=f"Hint: The answer is {correct}", text_color="gray")
    elif timed_quiz_frame.winfo_ismapped():
        timed_feedback.configure(text=f"Hint: The answer is {correct}", text_color="gray")
    else:
        print("Neither quiz_frame nor timed_quiz_frame is visible.")  # Debug statement

def check_answer():
    global correct
    user_input = entry.get()
    if not user_input:
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
        retry_practice_button.place(relx=0.5, rely=0.65, anchor="center")  
    else:
        feedback_label.configure(text=f"Unlucky, the answer was {correct}", text_color="red")
    retry_practice_button.pack(pady=10)

# ======== Timed Mode ========
score = 0
question_num = 0
max_questions = 10  # For 10 Questions mode
time_per_question = 5.0  # 5 seconds per question 
time_left = time_per_question  # Remaining time for current question
timer_running = False  # Timer state
infinite_mode = False  # True for Infinite Mode, False for 10 Questions mode

def next_timed_question():
    global x, y, correct, question_num
    if not infinite_mode and question_num >= max_questions:
        timed_feedback.configure(text=f"Quiz Complete! Score: {score}/{max_questions}", text_color="cyan")
        stop_timer()
        timed_entry.configure(state="disabled")
        timed_hint_button.configure(state="disabled")
        return
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    correct = x * y
    timed_question.configure(text=f"{x} x {y}")
    timed_entry.delete(0, ctk.END)
    timed_feedback.configure(text="")
    question_num += 1
    progress_bar.set(1.0)  
    progress_bar.configure(progress_color="#4CAF50")  
    start_timer() 

def check_timed_answer():
    global score, correct
    if not timer_running:  
        return
    user_input = timed_entry.get()
    try:
        user_answer = int(user_input)
    except ValueError:
        timed_feedback.configure(text="Invalid input", text_color="orange")
        return
    stop_timer()  
    if user_answer == correct:
        score += 1
        timed_feedback.configure(text="Correct!", text_color="green")
        score_label.configure(text=f"Score: {score}")
        if infinite_mode or question_num < max_questions:
            app.after(1000, next_timed_question)
        else:
            final_score_label.configure(text=f"Quiz Complete! Score: {score}/{max_questions}")
            final_score_label.place(relx=0.5, rely=0.5, anchor="center")
            final_score_label.lift()  
            timed_quiz_frame.lift()  
            retry_button.place(relx=0.5, rely=0.65, anchor="center")  
            retry_button.lift()  
            timed_entry.configure(state="disabled")
            timed_hint_button.configure(state="disabled")
            timed_entry.unbind("<Return>")  
            score_label.pack_forget()
    else:
        timed_feedback.configure(text=f"Wrong. It was {correct}.", text_color="red")
        score_label.configure(text=f"Score: {score}")
        final_score_label.configure(text=f"Final Score: {score}" if infinite_mode else f"Final Score: {score}/{max_questions}")
        final_score_label.place(relx=0.5, rely=0.5, anchor="center")
        final_score_label.lift()  
        timed_quiz_frame.lift()  
        retry_button.place(relx=0.5, rely=0.65, anchor="center")  
        retry_button.lift() 
        timed_entry.configure(state="disabled")
        timed_hint_button.configure(state="disabled")
        timed_entry.unbind("<Return>")  
        end_timed_quiz()  
    progress_bar.configure(progress_color="#4CAF50")  

def start_timer():
    global time_left, timer_running
    time_left = time_per_question
    timer_running = True
    progress_bar.set(1.0)
    update_timer()

def update_timer():
    global time_left, timer_running
    if timer_running and time_left > 0:
        time_left -= 0.1 
        progress_bar.set(time_left / time_per_question)
        if time_left / time_per_question < 0.3:
            progress_bar.configure(progress_color="#FF0000") 
            progress_bar.configure(progress_color="#FFA500") 
        app.after(100, update_timer) 
    elif time_left <= 0:
        end_timed_quiz()

def stop_timer():
    global timer_running
    timer_running = False

def end_timed_quiz():
    global timer_running
    timer_running = False
    timed_question.configure(text="Game Over!")
    if not timed_feedback.cget("text").startswith("Wrong. It was"):  
        timed_feedback.configure(text=f"Final Score: {score}" if infinite_mode else f"Final Score: {score}/{max_questions}", text_color="cyan")
    final_score_label.configure(text=f"Final Score: {score}" if infinite_mode else f"Final Score: {score}/{max_questions}")
    final_score_label.place(relx=0.5, rely=0.5, anchor="center")
    final_score_label.lift()  
    timed_quiz_frame.lift() 
    retry_button.place(relx=0.5, rely=0.65, anchor="center") 
    retry_button.lift()
    timed_entry.configure(state="disabled")
    timed_hint_button.configure(state="disabled")
    timed_entry.unbind("<Return>")  
    score_label.pack_forget()

def reset_timed_quiz():
    global score, question_num, time_left, timer_running
    score = 0
    question_num = 0
    time_left = time_per_question
    timer_running = False
    timed_entry.configure(state="normal")
    timed_hint_button.configure(state="normal")
    timed_feedback.configure(text="")
    final_score_label.place_forget()
    retry_button.place_forget()
    score_label.configure(text=f"Score: {score}")
    progress_bar.set(1.0)
    progress_bar.configure(progress_color="#4CAF50")
    score_label.pack(pady=10)
    timed_entry.bind("<Return>", lambda event: check_timed_answer())
    start_timer()
    next_timed_question()

# ======== Countdown Overlay ========
countdown_overlay = ctk.CTkFrame(app, fg_color=light_bg, corner_radius=0)
countdown_label = ctk.CTkLabel(countdown_overlay, text="", font=ctk.CTkFont(size=72, weight="bold"), text_color="white")
countdown_label.pack(expand=True)

def start_countdown(callback):
    practice_tab_frame.place_forget()
    timed_tab_frame.place_forget()
    menu_button.place_forget()
    mode_select_frame.place_forget()
    practice_close_button.place_forget()
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

# ======== UI Widgets ========
# ======================== Title frame ========================
tab_frame_image = ctk.CTkImage(light_image=Image.open(tab_frame_path), size=(450, 400))
tab_frame = ctk.CTkLabel(app, image=tab_frame_image, text="", fg_color="transparent")
tab_frame.place(relx=0.5, rely=0.5, anchor="center")
bind_drag(tab_frame)

title_menu = ctk.CTkFrame(tab_frame, fg_color=light_bg, width=200, height=200)
title_menu.place(relx=0.5, rely=0.55, anchor="center")

button_row = ctk.CTkFrame(title_menu, fg_color=light_bg)
button_row.pack(pady=1)

play_frame = ctk.CTkFrame(button_row, fg_color=light_bg)
play_frame.pack(side="left", padx=20)
play_button = ctk.CTkButton(play_frame, text="", image=play_icon, width=60, height=60,
                            fg_color=light_bg, hover_color=hover_light, corner_radius=10,
                            command=goto_main_menu)
play_button.pack()
play_label = ctk.CTkLabel(play_frame, text="Play", font=("Helvetica", 14), text_color=light_text)
play_label.pack(pady=5)

quit_frame = ctk.CTkFrame(button_row, fg_color=light_bg)
quit_frame.pack(side="left", padx=20)
quit_button = ctk.CTkButton(quit_frame, text="", image=quit_icon, width=60, height=60,
                            fg_color=light_bg, hover_color=hover_light, corner_radius=10,
                            command=app.destroy)
quit_button.pack()
quit_label = ctk.CTkLabel(quit_frame, text="Quit", font=("Helvetica", 14), text_color=light_text)
quit_label.pack(pady=5)

# ======================== Settings ========================
settings_frame_image = ctk.CTkImage(light_image=Image.open(settings_tab_path), size=(450, 400))
settings_frame = ctk.CTkLabel(app, image=settings_frame_image, text="", fg_color="transparent")
settings_menu = ctk.CTkFrame(settings_frame, fg_color=light_bg, width=200, height=200)
settings_menu.place(relx=0.3, rely=0.55, anchor="center")
theme_button = ctk.CTkButton(settings_menu, text="", image=moon_icon, width=10, height=10,
                             fg_color=light_bg, hover_color=hover_light, command=toggle_theme)
theme_button.pack()
settings_button = ctk.CTkButton(tab_frame, text="", image=settings_icon, width=10, height=10,
                                fg_color=light_bg, hover=False, command=show_settings)
settings_button.place(x=380, y=60)
settings_close_button = ctk.CTkButton(settings_frame, text="", image=close_icon, width=20, height=20,
                                      fg_color=light_bg, hover_color=hover_light, command=close_settings)

# ======================== Practice tab ========================
practice_tab_frame = ctk.CTkFrame(app, width=350, height=300, corner_radius=0, fg_color=light_bg)
practice_bg_label = ctk.CTkLabel(practice_tab_frame, image=practice_frame_image, text="", fg_color="transparent")
practice_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
practice_menu = ctk.CTkFrame(practice_tab_frame, corner_radius=0, fg_color=light_bg)
practice_menu.place(relx=0.5, rely=0.55, anchor="center")
practice_button = ctk.CTkButton(practice_menu, text="Play", font=button_font, width=220, height=45,
                                fg_color=light_bg, hover_color=hover_light, corner_radius=10,
                                text_color=light_text, image=play_arrow_icon, compound="left",
                                command=show_quiz)
practice_button.pack(pady=(40, 10))

# ======================== Timed tab ========================
timed_tab_frame = ctk.CTkFrame(app, width=350, height=300, corner_radius=0, fg_color=light_bg)
timed_bg_label = ctk.CTkLabel(timed_tab_frame, image=timed_frame_image, text="", fg_color="transparent")
timed_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
timed_menu = ctk.CTkFrame(timed_tab_frame, corner_radius=0, fg_color=light_bg)
timed_menu.place(relx=0.5, rely=0.55, anchor="center")
timed_button = ctk.CTkButton(
    timed_menu, text="Play", font=button_font, width=220, height=45,
    fg_color=light_bg, hover_color=hover_light, corner_radius=10,
    text_color=light_text, image=play_arrow_icon, compound="left",
    command=lambda: show_mode_select()
)
timed_button.pack(pady=(40, 10))

# Menu button
menu_button = ctk.CTkButton(app, text="Go Back", font=button_font, width=220, height=45,
                            fg_color=light_bg, hover_color=hover_light, corner_radius=10,
                            text_color=light_text, image=back_icon, compound="left",
                            command=back_to_title)

# ======================== Quiz frame (Practice) ======================== 
quiz_frame = ctk.CTkFrame(app, corner_radius=20, fg_color=light_bg)
message_question = ctk.CTkLabel(quiz_frame, text="", font=("label_font", 35, "bold"), text_color=light_text)

# Answer box with overlaid entry
answer_entry = ctk.CTkLabel(quiz_frame, text="", image=answer_box, fg_color=light_bg)
entry = ctk.CTkEntry(quiz_frame, font=button_font, text_color=light_text, fg_color="#E8E8E8",  
                     border_width=0, corner_radius=0, placeholder_text="Enter your answer here.")
entry.bind("<Return>", lambda event: check_answer())

# Hint button with icon, to be overlaid
hint_button = ctk.CTkButton(quiz_frame, text="", image=hint_icon, width=30, height=30,
                            fg_color=light_bg, hover_color=hover_light, command=show_hint)
feedback_label = ctk.CTkLabel(quiz_frame, text="", font=button_font, text_color=light_text)
retry_practice_button = ctk.CTkButton(quiz_frame, text="Try Again?", font=button_font,
                             fg_color=light_bg, hover_color=hover_light, corner_radius=10,
                             text_color=light_text, command=next_question)
practice_close_button = ctk.CTkButton(app, text="", image=close_icon, width=20, height=20,
                                      fg_color=light_bg, hover_color=hover_light, command=back_to_menu)

# Layout
message_question.pack(pady=30)

# Frame to hold answer_entry
answer_frame = ctk.CTkFrame(quiz_frame, fg_color=light_bg)
answer_frame.pack(pady=5)
answer_entry.pack()

# Overlay the entry on the answer_entry
entry.place(in_=answer_entry, relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.5)

# Overlay the hint button on the far right of answer_entry
hint_button.place(in_=answer_entry, relx=0.95, rely=0.5, anchor="e")

feedback_label.pack(pady=10)

# ======================== Timed quiz frame ======================== 
timed_quiz_frame = ctk.CTkFrame(app, corner_radius=20, fg_color=light_bg)

# Question label
timed_question = ctk.CTkLabel(timed_quiz_frame, text="", font=("label_font", 35, "bold"), text_color=light_text)
timed_question.pack(pady=30)

# Progress bar for time remaining
progress_bar = ctk.CTkProgressBar(
    timed_quiz_frame,
    width=300,
    height=20,
    corner_radius=10,
    border_width=2,
    mode="determinate",
    determinate_speed=0.1 / time_per_question,  # Update per 0.1s
    fg_color="#D3D3D3",
    progress_color="#4CAF50"
)
progress_bar.set(1.0)  # Start at full
progress_bar.pack(pady=10)

# Score label
score_label = ctk.CTkLabel(timed_quiz_frame, text="Score: 0", font=button_font, text_color=light_text)
score_label.pack(pady=10)

# Answer box with overlaid entry
timed_answer_entry = ctk.CTkLabel(timed_quiz_frame, text="", image=answer_box, fg_color=light_bg)
timed_entry = ctk.CTkEntry(timed_quiz_frame, font=button_font, text_color=light_text, fg_color="#E8E8E8",
                           border_width=0, corner_radius=0, placeholder_text="Enter your answer here.")
timed_entry.bind("<Return>", lambda event: check_timed_answer())

# Hint button with icon, to be overlaid
timed_hint_button = ctk.CTkButton(timed_quiz_frame, text="", image=hint_icon, width=30, height=30,
                                  fg_color=light_bg, hover_color=hover_light, command=show_hint)
timed_feedback = ctk.CTkLabel(timed_quiz_frame, text="", font=button_font, text_color=light_text)

# Final score label (centered, hidden initially)
final_score_label = ctk.CTkLabel(timed_quiz_frame, text="", font=ctk.CTkFont(family="Segoe UI", size=40, weight="bold"), text_color="cyan")
final_score_label.place_forget()  

# Retry button (hidden initially)
retry_button = ctk.CTkButton(
    timed_quiz_frame,
    text="Retry",
    font=button_font,
    width=220,
    height=45,
    fg_color=light_bg,
    hover_color=hover_light,
    corner_radius=10,
    text_color=light_text,
    image=play_arrow_icon,
    compound="left",
    command=lambda: reset_timed_quiz()
)
retry_button.place_forget()  

timed_answer_frame = ctk.CTkFrame(timed_quiz_frame, fg_color=light_bg)
timed_answer_frame.pack(pady=5)
timed_answer_entry.pack()
timed_entry.place(in_=timed_answer_entry, relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.5)
timed_hint_button.place(in_=timed_answer_entry, relx=0.95, rely=0.5, anchor="e")
timed_feedback.pack(pady=10)

# ======================== Mode selection frame ======================== 
mode_select_frame = ctk.CTkFrame(app, corner_radius=20, fg_color=light_bg)
mode_select_label = ctk.CTkLabel(mode_select_frame, text="Select Timed Mode", font=title_font, text_color=light_text)
mode_select_label.pack(pady=20)
ten_questions_button = ctk.CTkButton(
    mode_select_frame, text="10 Questions", font=button_font, width=220, height=45,
    fg_color=light_bg, hover_color=hover_light, corner_radius=10, text_color=light_text,
    image=play_arrow_icon, compound="left",
    command=lambda: start_countdown(lambda: show_timed_quiz(False))
)
ten_questions_button.pack(pady=10)
infinite_mode_button = ctk.CTkButton(
    mode_select_frame, text="Infinite Mode", font=button_font, width=220, height=45,
    fg_color=light_bg, hover_color=hover_light, corner_radius=10, text_color=light_text,
    image=play_arrow_icon, compound="left",
    command=lambda: start_countdown(lambda: show_timed_quiz(True))
)
infinite_mode_button.pack(pady=10)

# ======== Run App ========
title_menu.place(relx=0.5, rely=0.55, anchor="center")
app.mainloop()