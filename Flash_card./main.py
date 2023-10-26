from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn ={}

# ---------------------------------Pandas------------------------------------

try:
    data = pd.read_csv("./data./words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data./french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(french_image, image=F_image)
    flip_timer = window.after(3000, func=flip)


# ----------------------------------Flip-------------------------------------
def flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(french_image, image=E_image)


# ----------------------------------Filter-----------------------------------

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data./words_to_learn.csv", index=False)
    next_card()


# -----------------------------------UI--------------------------------------

window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Flash Cards")

flip_timer = window.after(3000, func=flip)

F_image = PhotoImage(file="./images./card_front.png")
E_image = PhotoImage(file="./images./card_back.png")
canvas = Canvas(width=800, height=526)
french_image = canvas.create_image(400, 263, image=F_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images./right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images./wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
