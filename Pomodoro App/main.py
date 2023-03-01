from tkinter import *
import math

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN = "#183A1D"
LIGHT_GREEN = "#367E18"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_TIME = 1500
SHORT_BREAK_TIME = 300
LONG_BREAK_TIME = 1200
reps = 0
timer = None

# TIMER RESET

def reset_timer():
    global reps
    window.after_cancel(timer)
    check.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=DARK_GREEN)
    reps = 0

# TIMER MECHANISM

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_TIME)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(SHORT_BREAK_TIME)
    else:
        timer_label.config(text="Study", fg=LIGHT_GREEN)
        count_down(WORK_TIME)
    print(reps)

# COUNTDOWN MECHANISM
def count_down(count):
    
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = str(seconds).zfill(2)
    if minutes < 10:
        minutes = str(minutes).zfill(2)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        # Executes a function after 1 second
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0 and reps % 8 != 0:
            new_checkmark = ""
            sessions = int(reps / 2)
            for i in range(sessions):
                new_checkmark += "✔"
            check.config(text=new_checkmark)

# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_image = PhotoImage(file="day28/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=DARK_GREEN, font=(FONT_NAME, 45, "bold"), bg=GREEN)
timer_label.grid(row=0, column=1)

reset_button = Button(text="Reset", width=5, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

start_button = Button(text="Start", width=5, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

check = Checkbutton(bg=GREEN, fg=DARK_GREEN)
check.grid(row=3, column=1)

window.mainloop()