from card import *
from collections import Counter, OrderedDict

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
        # print(nums)
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

    def assign_table(self):
        temp = dict()
        for card in self.cardlist:
            if card[0] in temp.keys():
                temp[card[0]] += 1
            else:
                temp[card[0]] = 1
        temp = dict(sorted(temp.items(), key=lambda x: x[1], reverse=True))
        # print(temp)
        # mydict.keys()[mydict.values().index(16)]

        result = []
        for value in list(sorted(set(temp.values()), reverse=True)):
            l1 = sorted([k for k, v in temp.items() if v == value], reverse=True)
            # print(l1)
            for i in range(len(l1)):
                for j in range(value):
                    result.append(l1[i])
        # print(result)
        return result

        # result = []
        # for item in temp:
        #     for occurence in range(item[1]):
        #         result.append(item[0])
        # return result


if __name__ == '__main__':
    b = [Card(10, 1), Card(10, 3), Card(8, 3), Card(10, 4), Card(8, 1)]
    a = Categorizer(b)
    a.assign_table()
    print(a)
