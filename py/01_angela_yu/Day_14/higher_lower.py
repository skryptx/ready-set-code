from enum import Enum
from random import randint
from celeb_generator import celeb_data, generate_list_celebs
from constants import logo, vs

class Selection(Enum):
    A = 1
    B = 2

def higher(celeb_a: celeb_data, celeb_b: celeb_data) -> celeb_data:
    return celeb_a if celeb_a.follower_count > celeb_b.follower_count else celeb_b

def guessed_correct(celeb_a: celeb_data, celeb_b: celeb_data, guess: celeb_data) -> bool:
    higher_celeb: celeb_data = higher(celeb_a, celeb_b)
    return True if guess.name == higher_celeb.name else False

def pick_celeb(celeb_list: list[celeb_data]) -> celeb_data:
    celeb_index: int = randint(0, len(celeb_list))
    picked_celeb: celeb_data = list.pop(celeb_list, celeb_index)
    return picked_celeb

def print_celeb_template(celeb_a: celeb_data, celeb_b: celeb_data) -> None:
    print(f"Compare {Selection.A.name}: {celeb_a.name}, a {celeb_a.description}, from {celeb_a.country}")
    print(vs)
    print(f"Compare {Selection.B.name}: {celeb_b.name}, a {celeb_b.description}, from {celeb_b.country}")
    

def higher_lower() -> None:
    celeb_list: list[celeb_data] = generate_list_celebs()

    celeb_a = pick_celeb(celeb_list)
    score = 0
    lost = False
    
    while not lost:
        celeb_b = pick_celeb(celeb_list)
        print(20*"\n")
        print(logo)
        print_celeb_template(celeb_a, celeb_b);
    
        selection = str(input("Who has more followers? Type 'A' or 'B': "))
        guess = celeb_a if selection == Selection.A.name else celeb_b
        is_guess_correct = guessed_correct(celeb_a, celeb_b, guess)
        if is_guess_correct:
            score+=1
            celeb_a = guess
            print(f"You're right! Current score: {score}")
        else:
            lost = True
            print(f"Sorry, that's wrong. Final score: {score}")
            score = 0
            break

higher_lower()
    

