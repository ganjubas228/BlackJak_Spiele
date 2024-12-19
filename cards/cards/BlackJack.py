from cards import Card, Suit, Figure
from cardset import CardSet
from player import Player


class BlackJack_game:
    def __init__(self, player, crourier, show_message, show_cards, need_more_card):
        self.player = player
        self.crourier = crourier
        self.show_message = show_message
        self.show_cards = show_cards
        self.need_more_card = need_more_card
        self.deck = self.get_cardset()
        self.deck.full()

    def get_cardset(self):
        return CardSet([])

    def move(self, player: Player):

        self.show_cards(player.hand_cards)
        self.show_message(
            f"Player {player} has {self.get_point(player.hand_cards)} point")

        while not self.is_player_lose(player) and self.need_more_card('Do you need more card?'):
            player.hand_cards.add([self.deck.pull()])
            self.show_cards(self.player.hand_cards)
            self.show_message(
                f"Player {player} has {self.get_point(player.hand_cards)} point")

    def is_player_lose(self, player: Player):
        if self.get_point(player.hand_cards) <= 21:
            return False
        else:
            return True

    def get_point(self, cards: CardSet):
        points = 0
        Ace_count = 0
        for i in cards.cards:
            if i.figure <= 10:
                points += i.figure
            elif i.figure == Figure.ace:
                points += 11
                Ace_count += 1
            else:
                points += 10

        while points > 21 and Ace_count > 0:
            points -= 10
            Ace_count -= 1

        return points

    def get_winner(self):
        if self.is_player_lose(self.player):
            return self.crourier
        if self.is_player_lose(self.crourier):
            return self.player
        if self.get_point(self.player.hand_cards) < self.get_point(self.crourier.hand_cards):
            return self.crourier
        elif self.get_point(self.player.hand_cards) == self.get_point(self.crourier.hand_cards):
            return None
        else:
            return self.player

    # помешать карты
    # раздать по две карты игроку и крупье
    # ход игрока
    # ход крупье
    # отобразить информацио о победителе
    def game_process(self):
        self.deck.mix()
        self.player.hand_cards.add(self.deck.deal(2))
        self.crourier.hand_cards.add(self.deck.deal(2))
        self.show_message(f"{self.player.name} is moving:")
        self.move(self.player)
        self.show_message(f"{self.crourier.name} is moving:")
        self.move(self.crourier)
        self.show_message(f"{self.get_winner().name} win!!!")
