from BlackJack import BlackJack_game
from player import Player
from cardset import CardSet


def show_message(message):
    print(message)


def show_cards(card_set):
    print('Cards:')
    print(card_set)


def need_more_card(message):
    print(message, 'y/n')
    answear = input().lower()
    if answear == 'y':
        return True
    else:
        return False


print('This is Black Jack game, write your name')
name = input()
game = BlackJack_game(Player(name, CardSet([])), Player('Croupier', CardSet([])),
                      show_message, show_cards, need_more_card)
game.game_process()
