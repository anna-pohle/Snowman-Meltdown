import random
from ascii_art import STAGES
from words import WORDS


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < 3 and set(guessed_letters) != set(secret_word):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) > 1:
                print("Invalid Input: Please enter single characters only!")
            elif guess in "0123456789":
                print("Invalid Input (number): Please enter letters only!")
            elif guess in "!§$%&/()=?`´+*#'-_.:,;^°<>":
                print("Invalid Character: Please enter letters only!")
            else:
                break
        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1
        display_game_state(mistakes, secret_word, guessed_letters)
    if set(guessed_letters) == set(secret_word):
        print(f"You saved the snowman! You correctly guessed the word '{secret_word}'")
    else:
        print(f"Oh no, the snowman has melted! The secret word was '{secret_word}'")
