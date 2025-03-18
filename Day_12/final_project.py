from enum import Enum
import random
from art import art

class Difficulty(Enum):
    HARD = 5
    MEDIUM = 7
    EASY = 10

def evaluate_guess(actual_num, guessed_num) -> bool:
    if guessed_num > actual_num:
        print("Too High.")
        return False
    elif(guessed_num < actual_num):
        print("Too Low.")
        return False
    print("You Win")
    return True

def play_guess_the_number(num: int, guess_count: int) -> None:
    number_found = False

    while guess_count > 0 and not number_found:
        print(f"You have {guess_count} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        number_found = evaluate_guess(num, guess)
        guess_count-=1
        if number_found:
            return
        if guess_count > 0 and not number_found:
            print("Guess again.")
    
    print("You Lost!")

print(art)
print("I'm thinking of a number between 1 and 100")
user_diff_input = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
guess_count = int(Difficulty[user_diff_input.upper()].value)

play_guess_the_number(random.randint(1,100), guess_count)