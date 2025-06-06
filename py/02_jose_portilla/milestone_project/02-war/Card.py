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
    value: int
    rank: int

    def __init__(self, id: str, type: CardType, value: int, rank: int):
        self.id = id
        self.type = type
        self.value = value
        self.rank = rank

    def __str__(self) -> str:
        return f"Type: {self.type.name}  value: {self.value}"