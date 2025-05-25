from tabnanny import check
from typing import Literal, cast

ValidPlayers = Literal['X', 'O']


def display_current_state(state: list[list[ValidPlayers | int]]) -> None:
    for ls in state:
        print(ls)


def move_by_player(state: list[list[ValidPlayers | int]], player: ValidPlayers, position: int) -> None:
    x_index: int
    y_index: int
    for i, val_1 in enumerate(state):
        for j, val_2 in enumerate(val_1):
            if val_2 == position:
                x_index = i
                y_index = j

    if state[x_index][y_index] in ['X', 'O']:
        raise Exception("Sorry, invalid position")
    else:
        state[x_index][y_index] = player


def check_winner(state: list[list[ValidPlayers | int]]) -> ValidPlayers | None:
    winning_positions = [[(0, 0), (0, 1), (0, 2)],
                         [(1, 0), (1, 1), (1, 2)],
                         [(2, 0), (2, 1), (2, 2)],
                         [(0, 0), (1, 0), (2, 0)],
                         [(0, 1), (1, 1), (2, 1)],
                         [(0, 2), (1, 2), (2, 2)],
                         [(0, 0), (1, 1), (2, 2)],
                         [(0, 2), (1, 1), (2, 0)]]

    for position in winning_positions:
        starting_symbol:  ValidPlayers | int

        if state[position[0][0]][position[0][1]] in ('X', 'O'):
            starting_symbol = state[position[0][0]][position[0][1]]
        else:
            continue

        if starting_symbol not in ['X', 'O']:
            continue

        if (state[position[1][0]][position[1][1]] == starting_symbol and
                state[position[2][0]][position[2][1]] == starting_symbol):
            return cast(ValidPlayers, starting_symbol)

    return None


def lets_play_tictactoe() -> None:
    state: list[list[ValidPlayers | int]] = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    turns_completed = 0

    player_turn: ValidPlayers = 'X'

    while check_winner(state) == None and turns_completed != 9:
        display_current_state(state)
        box_played = int(input("Please enter the position: "))
        move_by_player(state, player_turn, box_played)

        turns_completed += 1
        player_turn = 'O' if player_turn == 'X' else 'X'

    winner = check_winner(state)

    if winner in ['X', 'O']:
        print(f"Congratulations {winner}!")
    else:
        print("It is a draw!")


lets_play_tictactoe()
