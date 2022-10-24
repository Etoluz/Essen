from random import *
import pandas
from tkinter import *
from PIL import Image, ImageTk
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


cook_data = pandas.read_csv(".\data_home.csv")

koch_gericht = cook_data.to_dict(orient="records")

order_data = pandas.read_csv(".\data_order.csv")

bestell_gericht = order_data.to_dict(orient="records")


heutiges_bestell_gericht = choice(bestell_gericht)
heutiges_koch_gericht = choice(koch_gericht)

#Create Functionality


def cook():
    global current_card
    current_card = choice(koch_gericht)
    new_title = canvas.create_text(500, 50, text="Heute gibt's:", font=("Ariel", 20, "bold"))
    canvas.itemconfig(title, text=current_card["Kochen"], fill="black")


def order():
    global current_card
    current_card = choice(bestell_gericht)
    new_title = canvas.create_text(500, 50, text="Heute gibt's:", font=("Ariel", 20, "bold"))
    canvas.itemconfig(title, text=current_card["Bestellen"], fill="black")



#UI SETUP


window = Tk()
window.title("Heutiges Gericht")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=1000, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(500, 100, text="Essen!", font=("Ariel", 20, "bold"))
kochen = canvas.create_text(250, 150, text="Kochen!", font=("Ariel", 20, "bold"))
bestellen = canvas.create_text(750, 150, text="Bestellen!", font=("Ariel", 20, "bold"))



#Kochen Knopf
kb = Image.open("./649395.png")
kkb = kb.resize((200, 200))
kkb_bild=ImageTk.PhotoImage(kkb)
kochen_bild_knopf = Button(image=kkb_bild, highlightthickness=0, command=cook)
kochen_bild_knopf.grid(row=1, column=0)

#Bestellen Knopf
bb = Image.open("./bestellen.png")
kbb = bb.resize((200, 200))
kbb_bild=ImageTk.PhotoImage(kbb)
bestellen_bild_knopf = Button(image=kbb_bild, highlightthickness=0, command=order)
bestellen_bild_knopf.grid(row=1, column=1)

window.mainloop()