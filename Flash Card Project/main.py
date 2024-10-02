from tkinter import *
import random
import time
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


current_card = {}

# ---------------------------- FUNCTIONS ------------------------------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back)



def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



#Window

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)



# Cards
canvas = Canvas(width=800, height=526)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400,263,image=front)



card_title = canvas.create_text(400,150,text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)












#Correct Button
right = PhotoImage(file="images/right.png")
correct_button = Button(image=right, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)

#Wrong Button
wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)



next_card()

window.mainloop()
