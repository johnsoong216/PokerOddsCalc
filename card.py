class Card:
    """
    A standard poker card with value and suit
    Suit:
    - Diamond 1
    - Club 2
    - Heart 3
    - Spade 4
    
    
    Value:
    - 
    """
    
    def __init__(self, suit:int, value:int) -> None:
        self.suit = suit
        self.value = value
    
    
    def __equals__(self, other:Card) -> bool:
        return self.value == other.value
    