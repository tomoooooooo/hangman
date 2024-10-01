import random

import pygame.mixer

pygame.mixer.init()

correct_sound = pygame.mixer.Sound("correct.wav")
incorrect_sound = pygame.mixer.Sound("wrong.wav")
clap = pygame.mixer.Sound("clap.wav")
lose = pygame.mixer.Sound("lose.wav")


def hangman_logo():
    hang_logo="""
     _
    | |
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
    | '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/                       """

    print(hang_logo)

def get_brand_list():
    return ["daewoo", "lancia", "abarth", "rambler", "subaru", "suzuki", "nissan", "toyota", "jaguar", "hummer",
            "alpina", "brabus", "bugatti"]

def get_player_name():
    return input("Enter your name : ")

def choose_lives(player_name):
    while True:
        try:
            lives = 7    #int(input("Lives must be set to 7 to match the hangman stages: "))
            if lives == 7:
                return lives
            else:
                print(f"{player_name}, remember the game will end after 7 wrong choices!")
        except ValueError:
            print("Please enter a valid number.") #

def display_status(hangman_pics, wrong_guesses, guessed_word, lives):
    print(hangman_pics[wrong_guesses])
    print("\nWord:", ' '.join(guessed_word))
    print(f"Lives left: {lives - wrong_guesses}")

def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
        elif guess in guessed_letters:
            print(f"No! Come on! No! '{guess}' was guessed already! Try again!")
        else:
            return guess

def update_guessed_brand(word, guess, guessed_word):
    for i in range(len(word)):
        if word[i] == guess:
            guessed_word[i] = guess

def play_again():
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == 'y':
            print("Yay! You wanna dance?")
            return True
        elif play_again == 'n':
            print("Thanks for playing!")
            return False

def hangman():
    word_list = get_brand_list()
    hangman_pics = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           😢   |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           😢   |
           |   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           😢   |
          /|   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           😢   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           😢   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           +---+
           |   |
           😢   |
          /|\\  |
          / \\  |
               |
        =========
        ''',
        '''
          +---+
          |   |
          😵   |
         /|\\   |
         / \\   |
        🔥🔥🔥|
        =========
        '''
]

    word = random.choice(word_list)
    guessed_word = ['_'] * len(word)
    guessed_letters = []

    print(f"Welcome {player_name}, to the best Hangman game you ever played! (Car Brands Edition 🚗.)")
    lives = choose_lives(player_name)
    wrong_guesses = 0

    while wrong_guesses < lives and '_' in guessed_word:
        display_status(hangman_pics, wrong_guesses, guessed_word, lives)
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            update_guessed_brand(word, guess, guessed_word)
            print(f"AAhhh... much better! {player_name} The letter '{guess}' is in the word.")
            correct_sound.play()
        else:
            print(f"Not in this lifetime! {player_name} The letter '{guess}' is not in the word.")
            incorrect_sound.play()
            wrong_guesses += 1

    if '_' not in guessed_word:
        print(f"\nDear diary... Jackpot! {player_name} guessed the word: {word.upper()}")
        clap.play()
    else:
        print(hangman_pics[wrong_guesses])
        print(f"\nDying ain't much of a living, boy. The word was: {word.upper()}")
        lose.play()

    if play_again():
        hangman()

# Start the game
hangman_logo()
player_name = get_player_name()
hangman()

