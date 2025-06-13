"""
Represents Deck of 52 Cards
"""
from Card import Card
from enums.CardType import CardType
from enums.CardValue import CardValue
import uuid


class Deck:
    cards: list[Card] = list()

    def __init__(self):
        self.build_deck()

    def build_deck(self) -> None:
        for type in CardType:
            for value in CardValue:
                print(value.value)
                card = Card(str(uuid.uuid4()), type, value.name, value.value)
                self.cards.append(card)

    def __str__(self) -> str:
        res = ''

        for card in self.cards:
            res += f"{card}\n"

        return res
