from card import *
from card_categorizer import *
import itertools

"""
This class compares all possible hands and finds the best hand
"""


class Sorter:
    def __init__(self, starting_hand: list, flop: list) -> None:
        self.starting_hand = starting_hand
        self.flop = flop

    def besthand_solver(self,) -> "Categorizer":
        print()

    def list_all_hands(self):
        all_cards = self.starting_hand + self.flop
        # print(list(itertools.combinations(all_cards, 5)))
        all_hands = itertools.combinations(all_cards, 5)
        best = Categorizer(all_hands[0])
        for hands in all_hands:
            curr = Categorizer(hands)
            if best.category


if __name__ == '__main__':
    b = [Card(10, 1), Card(10, 2), Card(10, 3), Card(11, 4), Card(14, 1)]
    a = [Card(14, 2), Card(14, 3)]
    new = Sorter(a, b)
    new.list_all_hands()
