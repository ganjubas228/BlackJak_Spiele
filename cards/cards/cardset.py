from cards import Card, Suit, Figure
from operator import attrgetter
from random import *


class CardSet:
    def __init__(self, cards: list):
        if cards is None:
            cards = list()
        self.cards = cards

    def full(self):
        for f in Figure:
            for s in Suit:
                self.cards.append(self.get_card(f, s))

    def get_card(self, f, s):
        return Card(f, s)

    def __str__(self):
        res = ""
        for c in self.cards:
            res += str(c) + '\n'

        return res

    # потянуть карту
    # f, s - ?
    def pull(self, n=0):
        return self.cards.pop(n)

    # sdacha kart

    def deal(self, amount):
        deal_deck = self.cards[0: amount]
        del self.cards[0: amount]
        return deal_deck

    def mix(self):
        for i in range(3):
            for j in range(len(self.cards)):
                index = randint(0, len(self.cards) - 1)
                self.cards[i], self.cards[index] = self.cards[index], self.cards[i]

        # dobavit' kart v kolod

    def add(self, cards: list):
        self.cards += cards

    def sort(self):
        self.cards.sort(key=attrgetter('figure', 'suit'))

    def show(self):
        for i in self.cards:
            i.show()
