"""
This class finds and lists all the distributions of the hand and winning probability
"""
from deck import Deck
from card import Card
from besthand_sorter import Sorter
import itertools


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
        
        print(self.p1)
        print(self.p2)
    
    
    def flip(self, _next: "Card") -> None:
        self.deck.removeByCard(_next)
        self.p1.append(_next)
        self.p2.append(_next)
        
    def model(self) -> None:
        all_hands = itertools.combinations(self.deck, 7 - len(self.p1))
        for hand in all_hands:
            Sorter(self.p1, hand)
            Sorter(self.p2, hand)
            
    def comparison(self, p1:list, p2:list, hand:list) -> None:
        p1 = Sorter(self.p1, hand)
        p2 = Sorter(self.p2, hand)
        platform = Sorter([],[])
        p1 = p1.besthands_solver()
        p2 = p2.besthands_solver()
        platform.hand_compare
            
        
if __name__ == '__main__':
    a = Game()
    a.start(Card(1,1), Card(1,2), Card(1,3),Card(1,4))
    
        
        
    
    
    
    
    
    