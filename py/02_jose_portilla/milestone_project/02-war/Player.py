"""
Player class tracks players info and cards stack,
the player holds
"""
from Card import Card
from typing import Self


class Player:
    name: str
    cards: list[Card]
    selected_cards: list[Card]

    def __init__(self, name: str, cards: list[Card], selected_cards: list[Card]):
        self.name = name
        self.cards = cards
        self.selected_cards = selected_cards

    def select_card(self) -> Card:
        """selects the top card from player cards property

        Raises:
            Exception: if the deck is empty an exception will be raised
            stating Player does not have any more cards

        Returns:
            Card: single card from Players cards property
        """
        if len(self.cards) == 0:
            raise Exception("Player does not have any more cards")

        return self.cards.pop()

    def transfer_cards(self, cards: list[Card], winner_player: Self) -> None:
        """removed cards from current user and adds it to
        card property of winner_player

        select card automatically takes care of removing cards from current users
        deck

        Args:
            cards (list[Card]): list of cards to be transferred from current player
                                to winner_player
            winner_player: player who won the current war
        """

        # add cards in front of winner player cards
        cards.extend(winner_player.cards)
        winner_player.cards = cards

    def is_disqualified(self) -> bool:
        return len(self.cards) == 0
