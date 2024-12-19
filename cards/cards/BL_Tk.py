from tkinter import Canvas, Tk, mainloop, messagebox
from typing import Text
from graphic_cardset import Graphic_cardset
from graphic_BJ import Graphic_Blackjack_game
from player import Player

tk = Tk()
canvas = Canvas(tk, width=1000, height=700)
canvas.pack()

table = canvas.create_text(200, 20, font=('Arial', 8), fill='black')

player = Player("Player", Graphic_cardset(canvas, width=300, coords=(50, 50)))
cr = Player("Cropier", Graphic_cardset(
    canvas, width=300, coords=(50, 250)))


def show_message(message):
    canvas.itemconfig(table, text=message)


def draw_cards(cards):
    cards.draw()


def question(message):
    return messagebox.askyesno(message=message)


game = Graphic_Blackjack_game(
    canvas, player, cr, show_message, draw_cards, question)
game.game_process()
mainloop()
