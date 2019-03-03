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

    # def besthand_solver(self,) -> "Categorizer":
    #     print()

    def besthand_solver(self):
        all_cards = self.starting_hand + self.flop
        # print(list(itertools.combinations(all_cards, 5)))
        all_hands = itertools.combinations(all_cards, 5)
        best = Categorizer(self.flop)
        # print(best)

        for hands in all_hands:
            curr = Categorizer(hands)
            # print(curr)
            if curr.category < best.category:
                best = curr
            elif curr.category == best.category:
                best = self.rank_under_same_category(best, curr)
        print(best)
        return best

    def rank_under_same_category(self, obj1: "Categorizer", obj2: "Categorizer") -> "Categorizer":
        # print(obj1.assign_table())
        # print(obj2.assign_table())
        for i in range(5):
            if obj1.assign_table()[i] > obj2.assign_table()[i]:
                return obj1
            else:
                return obj2
        return obj1


if __name__ == '__main__':
    b = [Card(10, 1), Card(10, 2), Card(10, 3), Card(11, 4), Card(14, 1)]
    a = [Card(14, 2), Card(14, 3)]
    new = Sorter(a, b)
    new.besthand_solver()
