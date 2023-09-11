from tkinter import *
import pandas
from random import choice

# ------------------------#

BACKGROUND_COLOR = "#B1DDC6"
word = ""
french_dict = {}
# ------ FLASHCARDS ------#

try:
    french = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    french_og = pandas.read_csv("data/french_words.csv")
    french_dict = {row.French: row.English for (index, row) in french_og.iterrows()}

else:

    french_dict = {row.French: row.English for (index, row) in french.iterrows()}


def new_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = choice(list(french_dict.keys()))
    canvas.itemconfig(words, text=word)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(card, image=front)
    canvas.itemconfig(title, fill="black")
    canvas.itemconfig(words, fill="black")
    flip_timer = window.after(3000, flip)


def knows():
    global french_dict
    french_dict.pop(word)
    new_word()
    new = pandas.DataFrame.from_dict(french_dict, orient="index", columns=["English"])
    new.index.name = "French"
    new.to_csv("data/words_to_learn.csv")


def flip():
    canvas.itemconfig(card, image=back)
    canvas.itemconfig(title, fill="white", text="English")
    canvas.itemconfig(words, text=french_dict[word], fill="white")


# ------ UI Setup ------#

window = Tk()
window.title("FlashCards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
words = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
flip_timer = window.after(3000, flip)

check = PhotoImage(file="images/right.png")
check_button = Button(image=check, highlightthickness=0, borderwidth=0, command=knows)
check_button.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, borderwidth=0, command=new_word)
wrong_button.grid(column=0, row=1)


copy = canvas.create_text(400, 496, text="© Copyright Mikazaki™", font=("Courier", 10, "bold"))

new_word()

window.mainloop()
