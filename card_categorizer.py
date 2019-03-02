from card import *
from collections import Counter


class Categorizer:
    """
    A class that identifies the Hand Type

    1: Royal Flush
    2: Straight Flush
    3: Four of A Kind
    4. Full House
    5: Flush
    6: Straight
    7: Three of a Kind
    8: Two Pair
    9: One Pair
    10: High Card
    """

    def __init__(self, cardlist: list) -> None:
        self.cardlist = sorted(cardlist)
        self.category = 0
        self.assign_category()


    """
    Checks if all five cards are of the same suit
    True: 5 cards are of the same suit
    False: 5 cards are of different suit
    """

    def suit_check(self) -> bool:
        suit = self.cardlist[0][1]
        for card in self.cardlist:
            if card[1] != suit:
                return False
        return True

    """
    Checks if the five cards form a straight
    True: 5 cards form a straight
    False: 5 cards do not form a straight
    """

    def straight_check(self) -> bool:
        for i in range(4):
            if (self.cardlist[i + 1][0] - self.cardlist[i][0])!= 1:
                return False
        return True

    """
    Assigns the category of each item
    """

    def assign_category(self) -> None:
        nums = [card[0] for card in self.cardlist]
        nums_ordered = list(Counter(nums).values())
        # print(nums_ordered)

        if len(set(self.cardlist)) != len(self.cardlist):
            self.category = 0
        elif (self.suit_check()) and (self.straight_check()) and (nums == [i for i in range(10,15)]):
            self.category = 1
        elif (self.suit_check()) and (self.straight_check()):
            self.category = 2
        elif 4 in nums_ordered:
            self.category = 3
        elif (3 in nums_ordered) and (2 in nums_ordered):
            self.category = 4
        elif self.suit_check():
            self.category = 5
        elif self.straight_check():
            self.category = 6
        elif (3 in nums_ordered) and (2 not in nums_ordered):
            self.category = 7
        elif (2 in nums_ordered) and (len(nums_ordered) == 3):
            self.category = 8
        elif (2 in nums_ordered) and (len(nums_ordered) == 4):
            self.category = 9
        else:
            self.category = 10


    def __str__(self) -> str:
        category_strings = {0: 'Impossible Combination', 1: 'Royal Flush', 2: 'Straight Flush', 3: 'Four of a Kind',
                            4: 'Full House', 5: 'Flush', 6: 'Straight', 7: 'Three of a Kind', 8: 'Two Pairs',
                            9: 'One Pair', 10: 'High Card'}
        return category_strings.get(self.category) + " " + str([card.__str__() for card in self.cardlist])


if __name__ == '__main__':
    b = [Card(10, 1), Card(10, 2), Card(10, 3), Card(10, 4), Card(14, 1)]
    a = Categorizer(b)
    print(a.cardlist)
    print(a.category)
    # print(a)
