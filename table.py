import numpy as np

from exception import *
from utils import *
from hand import Hand

class Table:

    def __init__(self, deck_type, num_players):

        self.deck_arr = self.generate_deck(deck_type)
        self.player_hands = {player_num: Hand() for player_num in range(1, num_players + 1)}

        self.community = np.zeros(shape=(0, 2), dtype=np.int)

    def generate_deck(self, deck_type):

        if deck_type == "full":
            num = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        elif deck_type == "short":
            num = ["6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        else:
            raise DeckException("Invalid Deck Type. Valid options are: Full/Short ")

        suit = ["d", "c", "s", "h"]
        return card_str_to_arr([n + s for n in num for s in suit])

    def add_to_hand(self, player_num, cards):

        if type(cards) == np.ndarray and cards.ndim == 1:
            cards = [cards]
        elif type(cards) == list and type(cards[0]) == int:
            cards = [cards]
        elif type(cards) == str:
            cards = [cards]

        self.player_hands[player_num].add_cards(cards)

    def simulate(self, num_scenarios, precision):
        pass

    def view_deck(self):
        return " ".join(card_arr_to_str(self.deck_arr))

    def view_players(self):
        return {player: str(self.player_hands[player]) for player in self.player_hands}


    def add_to_community(self, cards):
        pass