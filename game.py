"""
This class finds and lists all the distributions of the hand and winning probability
"""
from deck import Deck
from card import Card
from besthand_sorter import Sorter
from card_categorizer import Categorizer
from collections import Counter
import itertools
import time
from matplotlib import pyplot as plt
import pandas as pd


class Game:
    
    def __init__(self) -> None:
        self.deck = Deck()
        self.p1 = []
        self.p2 = []
        
        
    def start(self, p1c1: "Card", p1c2: "Card", p2c1: "Card", p2c2: "Card") -> None:
        
        self.p1.append(p1c1)
        self.p1.append(p1c2)
        self.p2.append(p2c1)
        self.p2.append(p2c2)
        
        self.deck.removeByCard(p1c1)
        self.deck.removeByCard(p1c2)
        self.deck.removeByCard(p2c1)
        self.deck.removeByCard(p2c2)
        
        self.p1Outcome = []
        self.p2Outcome = []
        self.wld = []
    
    
    def flip(self, _next: "Card") -> None:
        self.deck.removeByCard(_next)
        self.p1.append(_next)
        self.p2.append(_next)
        
        self.p1Outcome = []
        self.p2Outcome = []
        self.wld = []
        
    def model(self):
        all_hands = itertools.combinations(self.deck, 7 - len(self.p1))
        for hand in all_hands:
            self.comparison(self.p1, self.p2, list(hand))


            
    def comparison(self, p1:list, p2:list, hand:list) -> None:
        p1 = Sorter(p1, hand)
        p2 = Sorter(p2, hand)
        platform = Sorter([],[])
        p1 = p1.besthand_solver()
        p2 = p2.besthand_solver()
        
        
    
        p1C = Categorizer(p1)
        p2C = Categorizer(p2)
        
        print(p1C)
        print(p2C)
        
        
        self.p1Outcome.append(p1C.category)
        self.p2Outcome.append(p2C.category)
        
        outcome = platform.hand_compare(p1, p2, True)
        if outcome == p1:
            self.wld.append(1)
        elif outcome == p2:
            self.wld.append(-1)
        else:
            self.wld.append(0)
            
        
        
            
        
if __name__ == '__main__':
    t1 = time.time()
    a = Game()
    a.start(Card(14,1), Card(13,1), Card(11,2),Card(10,2))
    a.flip(Card(11,1))
    a.flip(Card(10,1))
    a.flip(Card(5,2))
    a.model()
    t2 = time.time()
    print(t2 - t1)
    
    p1Count = Counter(a.p1Outcome)
    p2Count = Counter(a.p2Outcome)
    pWLD = Counter(a.wld)
    
    df = pd.DataFrame.from_dict(p1Count, orient='index')
    df.plot(kind='bar')    
    plt.show()
    df = pd.DataFrame.from_dict(p2Count, orient='index')
    df.plot(kind='bar') 
    plt.show()
    df = pd.DataFrame.from_dict(pWLD, orient='index')
    df.plot(kind='bar')     
    plt.show()
    
    
    
    
    