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
    is_out_for_turn: bool
    is_disqualified: bool

    def __init__(self, name: str, cards: list[Card], selected_cards: list[Card]):
        self.name = name
        self.cards = cards
        self.selected_cards = selected_cards
        self.is_out_for_turn = False
        self.is_disqualified = False

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
        card = self.cards.pop()
        self.selected_cards.append(card)
        return card

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
        cards.extend(winner_player.selected_cards)
        cards.extend(winner_player.cards)
        winner_player.cards = cards

    def get_printable_string_from_list(self, cards: list[Card]) -> str:
        output = ''
        for card in cards:
            output = f"{output} {card.value} {card.type.name}\n"

        return output

    def __str__(self) -> str:
        return f"""Name: {self.name}\n
                Cards: {self.get_printable_string_from_list(self.cards)}\n
                Selected Cards: {self.get_printable_string_from_list(self.selected_cards)}\n
                Is Out For Turn: {self.is_out_for_turn}\n
                Is Disqualified: {self.is_disqualified}\n
                """
