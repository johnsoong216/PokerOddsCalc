class Card(tuple):
    """
    A standard poker card with value and suit
    Suit:
    - Diamond 1
    - Club 2
    - Heart 3
    - Spade 4

    Value:
    - Two 2
    ....
    - King 13
    - Ace 14
    """

    def __init__(self, value: int, suit: int) -> None:
        self.suit = suit
        self.value = value

    def __new__(self, value: int, suit: int) -> tuple:
        return tuple.__new__(Card, (value, suit))


    def __equals__(self, other) -> bool:
        if isinstance(other, Card):
            return self.value == other.value
        return False


    def __str__(self) -> str:
        suitStrings = {1: 'd', 2: 'c', 3: 'h', 4: 's'}
        numStrings = {2: '2', 3: '3', 4: '4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
                      10: '10', 11: 'J', 12: 'Q', 13:'K', 14:'A'}
        return numStrings.get(self.value) + suitStrings.get(self.suit)


if __name__ == '__main__':
    a = Card(7, 3)
    print(a[1])
    print(a)
    print(a.value)
    print(a.suit)
