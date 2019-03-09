import random
from card import Card


class Deck:
    """
    A standard deck of cards
    """

    def __init__(self) -> None:
        self.deck = []
        for suit in range(1, 5):
            for num in range(2, 15):
                self.deck.append(Card(num, suit))
                
        self.current = 0    
    
    def __iter__(self) -> 'Deck':
        return self
    
    def __next__(self) -> 'Card':
        if self.current >= len(self.deck):
            raise StopIteration        
        result = self.deck[self.current]
        self.current += 1
        return result

    def removeByCard(self, card: Card) -> None:
        if card in self.deck:
            self.deck.remove(card)
            return card
        return Card(1, 1)

    def removeByIndex(self, index: int) -> None:
        if index <= len(self.deck):
            result = self.deck.get(index)
            self.deck.pop(index)
            return result
        return Card(1, 1)

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def __str__(self) -> str:
        representation = "Deck: ["
        for card in self.deck:
            representation += card.__str__() + " "
        representation += "]"
        return representation


if __name__ == '__main__':
    newDeck = Deck()
    print(newDeck)
    newDeck.shuffle()
    print(newDeck)
