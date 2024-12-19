from enum import IntEnum


class Suit(IntEnum):
    diamond = 1
    club = 2
    heart = 3
    spade = 4


class Figure(IntEnum):
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14


class Card:
    def __init__(self, figure, suit):
        self.figure = figure
        self.suit = suit
        self.is_opened = False

    def show(self):
        self.is_opened = True

    def hide(self):
        self.is_opened = False

    def rotate(self):
        self.is_opened = not self.is_opened

    def __str__(self):
        return f"{self.figure.name} {self.suit.name}"
