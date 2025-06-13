from Deck import Deck
from Player import Player
from random import shuffle


class War:
    deck: Deck
    players: list[Player]
    player_count: int
    eligible_players: list[Player]

    def __init__(self):
        self.deck = Deck()
        self.player_count = int(input("How many players? -> "))
        self.players = []
        self.eligible_players = []

        for i in range(1, self.player_count + 1):
            self.players.append(Player(f"Player {i}", [], []))

        self.shuffle_and_distribute_deck()
        self.set_eligible_players()

    def shuffle_and_distribute_deck(self) -> None:
        shuffle(self.deck.cards)
        count = 0

        for card in self.deck.cards:
            self.players[count % self.player_count].cards.append(card)
            count += 1

    def set_eligible_players(self) -> None:
        self.eligible_players = []

        for player in self.players:
            if player.is_eligible() == True:
                self.eligible_players.append(player)

    def move_all_losers_cards_to_winning_player(self, winning_player: Player) -> None:
        for player in self.players:
            if player.name == winning_player.name:
                continue
            player.transfer_cards(winning_player)

    def draw_one_card_each_player(self) -> None:
        for player in self.eligible_players:
            if not player.is_eligible():
                continue
            player.draw_one_card()

    def evaluate_drawn_cards(self) -> None:
        highest_card_players: list[Player] = []
        highest_card_rank = -1
        for player in self.eligible_players:
            highest_card_rank = max(
                player.selected_cards[-1].rank, highest_card_rank)
            print(f"{player.name} Cards: {player.selected_cards[-1]}")

        for player in self.eligible_players:
            if player.selected_cards[-1].rank == highest_card_rank:
                highest_card_players.append(player)
            else:
                player.is_out_for_turn = True

        if len(highest_card_players) > 1:
            self.set_eligible_players()
            self.draw_one_card_each_player()
        elif len(highest_card_players) == 1:
            self.move_all_losers_cards_to_winning_player(
                highest_card_players[0])

    def reset_out_of_turn_prop(self) -> None:
        for player in self.players:
            player.is_out_for_turn = False

    def play(self) -> None:
        while len(self.eligible_players) != 1:
            self.draw_one_card_each_player()
            self.evaluate_drawn_cards()

            self.reset_out_of_turn_prop()
            self.set_eligible_players()


war = War()
war.play()
print(f"Congratulations {war.eligible_players[0].name}")
