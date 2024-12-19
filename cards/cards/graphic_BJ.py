from graphic_cardset import Graphic_cardset
from BlackJack import BlackJack_game


class Graphic_Blackjack_game(BlackJack_game):
    def __init__(self, canvas, player, crourier, show_message, show_cards, need_more_card):
        self.canvas = canvas
        super().__init__(player, crourier, show_message, show_cards, need_more_card)

    def get_cardset(self):
        return Graphic_cardset(self.canvas)
