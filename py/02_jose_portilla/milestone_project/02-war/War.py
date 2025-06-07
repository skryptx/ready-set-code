from Deck import Deck
from Player import Player
from random import shuffle


class War:
    deck: Deck
    players: list[Player]
    player_count: int

    def __init__(self):
        self.deck = Deck()
        self.player_count = int(input("How many players? -> "))
        self.players = []

        for i in range(1, self.player_count + 1):
            self.players.append(Player(f"Player {i}", [], []))

        self.shuffle_and_distribute_deck()

    def shuffle_and_distribute_deck(self) -> None:
        shuffle(self.deck.cards)
        count = 0

        for card in self.deck.cards:
            self.players[count % self.player_count].cards.append(card)
            count += 1

        for player in self.players:
            print(player)


war = War()
