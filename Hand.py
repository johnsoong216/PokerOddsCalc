import numpy as np
from Exception import *



class Hand:
    """
    A class that identifies the Hand Type

    10: Royal Flush
    9: Straight Flush
    8: Four of A Kind    4, 1, 2
    7. Full House        3, 2, 2
    6: Flush
    5: Straight
    4: Three of a Kind   3, 1, 3
    3: Two Pair          2, 1, 3
    2: One Pair          2, 1, 4
    1: High Card         1, 1, 5
    """

    def __init__(self, cards=[]) -> None:
        print("Create Hand")
        self.hand = self.create_hand(cards)
        self._valid_hand(self.hand)

        if len(self.hand) == 5:
            self.rank, self.in_rank_values = self.assign_rank(self.hand)

    def create_hand(self, cards):
        cardlist = np.empty((len(cards),), dtype=object)
        cardlist[:] = sorted(cards)
        return cardlist

    ### Buggy Don't Need It
    #     def remove_card(self, card):
    #         self.hand = self.hand[self.hand != card]

    def __add__(self, other):
        return Hand(np.append(self.hand, other.hand))

    def __radd__(self, other):
        return Hand(np.append(self.hand, other.hand))

    def _valid_hand(self, hand):
        if len(hand) > 5:
            raise HandException("Hand Size has Exceeded the Limit of 5")
        tupled_card = [tuple(card) for card in hand]
        if len(tupled_card) != len(list(set(tupled_card))):
            raise HandException("Duplicate Cards Found in Hand")

    ### Helper functions to get hand values
    def _hand_values(self, hand):
        return np.array(sorted([card[0] for card in hand]))

    def _hand_suits(self, hand):
        return np.array(sorted([card[1] for card in hand]))

    ### Convenient Quick Check
    """
    Checks if all five cards are of the same suit
    True: 5 cards are of the same suit
    False: 5 cards are of different suit
    """

    def suit_check(self, hand):
        if len(np.unique(self._hand_suits(hand))) == 1:
            return True
        return False

    """
    Checks if the five cards form a straight
    True: 5 cards form a straight
    False: 5 cards do not form a straight
    """

    def straight_check(self, hand):
        hand_values = self._hand_values(hand)
        # print(hand_values)
        # print(type(hand_values))
        # print(np.arange(hand_values[0], hand_values[0] + 5, 1))
        # print(hand_values == np.arange(hand_values[0], hand_values[-1] + 1, 1))
        if (hand_values == np.arange(hand_values[0], hand_values[0] + 5, 1)).all()or (
                hand_values == np.array([2, 3, 4, 5, 14])).all():
            return True
        return False

    """
    Assigns the rank of the hand
    """

    def assign_rank(self, hand):

        suit_check = self.suit_check(hand)
        straight_check = self.straight_check(hand)
        hand_values = self._hand_values(hand)

        ### We could use straight check and suit check to quickly determine certain card types
        if suit_check and straight_check and hand_values[0] == 10:
            return 10, hand_values
        elif suit_check and straight_check:
            return 9, hand_values
        elif suit_check:
            return 6, hand_values
        elif straight_check:
            return 5, hand_values

        ### Assign all other categories
        val, count = np.unique(hand_values, return_counts=True)
        return self._rank_dict((max(count), min(count), len(count))), val[count.argsort()]

    def in_rank_comparison(self, hand_value_1, hand_value_2):

        if (hand_value_1 == np.array([2, 3, 4, 5, 14])).all():
            hand_value_1 = np.array([1, 2, 3, 4, 5])
        if (hand_value_2 == np.array([2, 3, 4, 5, 14])).all():
            hand_value_2 = np.array([1, 2, 3, 4, 5])

        if (hand_value_1 == hand_value_2).all():
            return 0

        for i in range(-1, -len(hand_value_1) - 1, -1):
            if hand_value_1[i] > hand_value_2[i]:
                return 1
            elif hand_value_1[i] < hand_value_2[i]:
                return -1

    def _rank_dict(self, max_min_len):
        rank_params_dict = {(4, 1, 2): 8, (3, 2, 2): 7, (3, 1, 3): 4, (2, 1, 3): 3, (2, 1, 4): 2, (1, 1, 5): 1}
        return rank_params_dict[max_min_len]


    ### Overwriting Comparison Operators
    def __eq__(self, other) -> bool:
        if isinstance(other, Hand):
            if self.rank != other.rank:
                return False
            elif self.in_rank_comparison(self.in_rank_values, other.in_rank_values) == 0:
                return True
            return False
        return False

    def __gt__(self, other) -> bool:
        if isinstance(other, Hand):
            if self.rank > other.rank:
                return True
            elif self.in_rank_comparison(self.in_rank_values, other.in_rank_values) == 1:
                return True
            return False
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Hand):
            if self.rank < other.rank:
                return True
            elif self.in_rank_comparison(self.in_rank_values, other.in_rank_values) == -1:
                return True
            return False
        return False

    def __ge__(self, other) -> bool:
        if isinstance(other, Hand):
            if self.rank < other.rank:
                return True
            elif self.in_rank_comparison(self.in_rank_values, other.in_rank_values) in [0, 1]:
                return True
            return False
        return False

    def __le__(self, other) -> bool:
        if isinstance(other, Hand):
            if self.rank < other.rank:
                return True
            elif self.in_rank_comparison(self.in_rank_values, other.in_rank_values) in [0, -1]:
                return True
            return False
        return False

    def __ne__(self, other) -> bool:
        if isinstance(other, Hand):
            if self.rank != other.rank:
                return True
            elif self.in_rank_comparison(self.in_rank_values, other.in_rank_values) != 0:
                return True
            return False
        return False


    ### Overwriting String Operation
    def __str__(self) -> str:
        category_strings = {10: 'Royal Flush', 9: 'Straight Flush', 8: 'Four of a Kind',
                            7: 'Full House', 6: 'Flush', 5: 'Straight', 4: 'Three of a Kind', 3: 'Two Pairs',
                            2: 'One Pair', 1: 'High Card'}
        if len(self.hand) == 5:
            return category_strings.get(self.rank) + " " + str([card.__str__() for card in self.hand])
        return str([card.__str__() for card in self.hand])

    #     def assign_table(self):
    #         temp = dict()
    #         for card in self.cardlist:
    #             if card[0] in temp.keys():
    #                 temp[card[0]] += 1
    #             else:
    #                 temp[card[0]] = 1
    #         temp = dict(sorted(temp.items(), key=lambda x: x[1], reverse=True))

    #         result = []
    #         for value in list(sorted(set(temp.values()), reverse=True)):
    #             l1 = sorted([k for k, v in temp.items() if v == value], reverse=True)
    #             # print(l1)
    #             for i in range(len(l1)):
    #                 for j in range(value):
    #                     result.append(l1[i])
    #         return result

