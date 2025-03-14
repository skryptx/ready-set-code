from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def pick_random_card(total: int) -> int:
    card = choice(cards)
    if total + card > 21:
        card = 1

    return card


def get_total(cards: list[int]) -> int:
    return sum(cards, 0)


def game_kickoff() -> None:
    user_total = 0
    comp_total = 0
    user_cards: list[int] = [pick_random_card(user_total)]
    comp_cards: list[int] = []
    user_choice = "y"
    MAX_TOTAL = 21

    while comp_total < MAX_TOTAL and user_total < MAX_TOTAL and user_choice == "y":
        user_cards.append(pick_random_card(user_total))
        user_total = get_total(user_cards)
        print(f"Your cards: {user_cards}, Total: {user_total} ")

        if user_total > MAX_TOTAL:
            break

        comp_cards.append(pick_random_card(comp_total))
        comp_total = get_total(comp_cards)
        print(f"Computer cards: {comp_cards}, Total: {comp_total} ")

        user_choice = input("Want to pick one more card? y/n: ")

    if user_choice == "y":
        if user_total > MAX_TOTAL:
            print("You Lost!")
            return
        print("You Win!")

    if user_choice == "n":
        comp_cards.append(pick_random_card(comp_total))
        comp_total = get_total(comp_cards)
        print(f"Computer cards: {comp_cards}, Total: {comp_total} ")

        if comp_total > MAX_TOTAL or user_total > comp_total:
            print("You Win!")
        elif comp_total == 21 or comp_total > user_total:
            print("You Lost!")
        else:
            print("It is a tie!")


def play_blackjack() -> None:
    play = input("Wanna play blackjack? y/n: ")
    if play == "n":
        return
    game_kickoff()


play_blackjack()
