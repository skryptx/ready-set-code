"""
Card class represents a card with having following properties:
id: unique identifier
type: Enum<Spade, Heart, Diamond, Club>
rank: 2 to 14(Ace)
"""
from CardType import CardType

class Card:
    id: str
    type: CardType
    rank: int

    def __init__(self, id: str, type: CardType, rank: int):
        self.id = id
        self.type = type
        self.rank = rank