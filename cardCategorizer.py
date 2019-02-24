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
    
    def __init__(self, cardList: list) -> None:
        self.cardList = sorted(cardList)
        self.category = 0
        
        
        
        
        
    """
    Checks if all five cards are of the same suit
    True: 5 cards are of the same suit
    False: 5 cards are of different suit
    """
    
    def suit_check(self) -> bool:
        suit = self.cardList[0][1]
        for card in self.cardList:
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
            if (self.cardList[i+1][0] - self.cardList[i][0])!= 1:
                return False
        return True
    
    """
    Assigns the category of each item
    """
    
    def assign_category(self) -> None:
        nums = [card[0] for card in self.cardList]
        numsOrdered = list(Counter(nums).values())
        
        if len(set(self.cardList)) != len(self.cardList):
            self.category = 0
        elif (self.suit_check()) and (self.straight_check()) and (nums == [i for i in range(10,15)]):
            self.category = 1
        elif (self.suit_check()) and (self.straight_check()):
            self.category = 2
        elif 4 in numsOrdered:
            self.category = 3
        elif (3 in numsOrdered) and (2 in numsOrdered):
            self.category = 4
        elif self.suit_check():
            self.category = 5
        elif self.straight_check():
            self.category = 6
        elif (3 in numsOrdered) and (2 not in numsOrdered):
            self.category = 7 
        elif (2 in numsOrdered) and (len(numsOrdered) == 3):
            self.category = 8
        elif (2 in numsOrdered) and (len(numsOrdered) == 4):
            self.category = 9
        else:
            self.category = 10
          
        
    def __str__(self) -> str:
        categoryStrings = {0: 'Impossible Combination', 1: 'Royal Flush', 2: 'Straight Flush', 3: 'Four of a Kind', 4: 'Full House', 5: 'Flush', 
                           6: 'Straight', 7: 'Three of a Kind', 8: 'Two Pairs', 9: 'One Pair', 10: 'High Card'}
        return categoryStrings.get(self.category) + " " + str([card.__str__() for card in self.cardList])
        
if __name__ == '__main__':
    b = [Card(10,1), Card(10,2), Card(10,3), Card(10,4), Card(14,1)]
    a = Categorizer(b)
    a.assign_category()
    print(a)
