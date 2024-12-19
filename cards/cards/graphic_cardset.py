from tkinter import Canvas
from cardset import CardSet
from cards import Card, Figure, Suit
from graphic_card import Graphic_card


class Graphic_cardset(CardSet):
    def __init__(self, canvas: Canvas, coords=(0, 0), cards=None, width=75):
        super().__init__(cards)
        self.width = width
        self.canvas = canvas
        self.coords = coords

    def draw(self, coords=(0, 0)):
        for i in range(len(self.cards)):
            card = self.cards[i]
            card.draw()
            self.canvas.coords(
                card.image, coords[0] + i * (self.width - 150)/len(self.cards), self.coords[1])
            self.canvas.tag_raise(card.image)

    def get_card(self, f, s):
        return Graphic_card(self.canvas, f, s)
