from tkinter import *
import random
import pandas
from tkinter import messagebox
timer = None
random_card = None

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    to_learn_data = data.to_dict(orient="records")
except IndexError:
    messagebox.showinfo(message="There is no more words to learn!\nGood job!")
else:
    to_learn_data = data.to_dict(orient="records")

def check_button():
    global random_card
    try:
        to_learn_data.remove(random_card)
    except ValueError:
        messagebox.showinfo(message="There is no more words to learn!\nGood job!")
    else:
        next_card()
        data_dict_df = pandas.DataFrame(to_learn_data)
        data_dict_df.to_csv("./data/words_to_learn.csv", index=False)

def flip_card(random_card):
    canvas.itemconfig(current_card, image=card_back_image)
    canvas.itemconfig(title_text, text="Finnish", fill="white")
    canvas.itemconfig(word_text, text=random_card["Finnish"], fill="white")

def next_card():
    global random_card
    global timer
    if timer:
        window.after_cancel(timer)
    try:
        random_card = random.choice(to_learn_data)
    except IndexError:
        messagebox.showinfo(message="There is no more words to learn!\nGood job!")
    else:
        canvas.itemconfig(current_card, image=card_front_image)
        canvas.itemconfig(title_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=random_card["French"], fill="black")
        timer = window.after(3500, flip_card, random_card)

# --------------- UI SETUP -----------------
window = Tk()
window.title("Flashcard App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Images
card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
current_card = canvas.create_image(0,0,image=card_front_image, anchor="nw")
canvas.grid(row=0, column=0)

title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Buttons
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0, sticky=W, padx=(180,0))
right_button = Button(image=right_image, highlightthickness=0, command=check_button)
right_button.grid(row=1,column=0, sticky=E, padx=(0,180))

next_card()

window.mainloop()