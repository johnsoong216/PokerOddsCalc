from utils import *



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

        #         if type(cards) == np.ndarray and cards.ndim == 1:
        #             cards = [cards]
        #         elif type(cards) == list and type(cards[0]) == int:
        #             cards = [cards]
        #         elif type(cards) == str:
        #             cards = [cards]

        for card in cards:
            self.add_card(card)

    def add_card(self, card):

        if type(card) == str:
            if len(self.card_arr) == 0:
                self.card_arr = card_str_to_arr([card])
            else:
                self.card_arr = np.concatenate([
                    self.card_arr,
                    card_str_to_arr([card])
                ], axis=0)

        else:
            if len(self.card_arr) == 0:
                self.card_arr = card_str_to_arr([card])
            else:
                self.card_arr = np.concatenate([
                    self.card_arr,
                    np.array([card])
                ], axis=0)

    def __str__(self):
        return " ".join(card_arr_to_str(self.card_arr))