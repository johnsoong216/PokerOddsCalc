from utils import *
from exception import *



class Hand:

    def __init__(self, cards=None):

        # Two ways to initialize (np.ndarray or list)

        if cards is None:
            self.card_arr = np.zeros(shape=(0, 2), dtype=np.int)

        elif (type(cards) == np.ndarray) or (type(cards) == list and type(cards[0]) == list):
            self.card_arr = np.array(cards)

        else:
            self.card_arr = card_str_to_arr(cards)

    def add_cards(self, cards):

        cards = format_cards(cards)

        for card in cards:
            self.card_arr = add_card(card, self.card_arr)

        if len(self.card_arr) > 2:
            raise HandException("Cannot Have more than two cards in hand")

    def remove_cards(self, cards):

        cards = format_cards(cards)

        for card in cards:
            self.card_arr = remove_card(card, self.card_arr)



    def __str__(self):
        return " ".join(card_arr_to_str(self.card_arr))