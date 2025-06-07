from enum import Enum


class CardType(Enum):
    HEART = 1,
    DIAMOND = 2,
    SPADE = 3,
    CLUB = 4

    def __iter__(self):
        return super().__iter__()
