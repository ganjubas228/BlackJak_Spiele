from cards import Card, Figure, Suit
from tkinter import *
from PIL import Image, ImageTk


class Graphic_card(Card):
    def __init__(self, canvas: Canvas, figure, suit):
        super().__init__(figure, suit)
        self.canvas = canvas
        self.picture = Image.open(
            f"images\\{self.suit.name}s {self.figure.name}.png")
        self.picture = self.picture.resize((150, 200), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.picture)
        self.image = self.canvas.create_image(
            0, 0, image=self.photo, anchor='nw')
        self.canvas.itemconfig(self.image, state=HIDDEN)

    def draw(self):
        self.canvas.itemconfig(self.image, state=NORMAL)
