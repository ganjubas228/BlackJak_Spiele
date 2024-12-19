from cardset import CardSet


class Player:
    def __init__(self, name, cards=CardSet([])):
        self.hand_cards = cards
        self.name = name

    def __str__(self):
        return self.name
