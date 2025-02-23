from random import choice

def prepare_s_word_dict(s_word):
    s_word_dict = {}
    for i in range(len(s_word)):
        if s_word[i] not in s_word_dict:
            s_word_dict[s_word[i]] = [i]
        else:
            s_word_dict[s_word[i]].append(i)
    return s_word_dict

def fill_the_guess_list(guess_list, s_word_dict, guess_letter):
    for index in s_word_dict[guess_letter]:
        guess_list[index] = guess_letter

def play_hangman():
    words_list = ["Avenger", "Spiderman", "Superman", "Hobbit", "Lordoftherings"]
    win = False
    s_word = choice(words_list).upper()
    lives = 7
    all_guesses = []

    # initialize placeholder list to fill based on user guesses
    guess_list = []
    for i in range(len(s_word)):
        guess_list.append("_")

    # prepare dictionary to track indexes of letters
    s_word_dict = prepare_s_word_dict(s_word)

    # guess loop starts until game over
    while lives > 0 and "_" in guess_list:
        print("\n\n\n\n\n\n***************************\n\n\n\n\n\n\n\n\n\n\n\n")
        print("".join(guess_list))
        print(f"All Guesses: {" ".join(all_guesses)}")
        print(f"Lives left: {lives}")

        guess_letter = input("Guess -> ")
        guess_letter = guess_letter.upper()

        if guess_letter in all_guesses:
            print("Already used the letter. Please try again.")
            continue

        all_guesses.append(guess_letter)

        if guess_letter in s_word_dict:
            print("Right!")
            fill_the_guess_list(guess_list, s_word_dict, guess_letter)
        else:
            print("Wrong!")
            lives -= 1

    if not lives:
        print("You dead!")
    else:
        print("You live!")


play_hangman()

