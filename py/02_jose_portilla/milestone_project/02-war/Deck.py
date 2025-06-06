"""
Represents Deck of 52 Cards
"""
from Card import Card
from CardType import CardType
import uuid

class Deck:
    cards: list[Card] = list()

    def __init__(self):
        self.build_deck()

    def build_deck(self) -> None:
        for type in CardType:
            for value in range(2,15):
                card = Card(str(uuid.uuid4()), type, value, value)
                self.cards.append(card)
    
    def __str__(self) -> str:
        res = ''

        for card in self.cards:
            res += f"{card}\n"
        
        return res