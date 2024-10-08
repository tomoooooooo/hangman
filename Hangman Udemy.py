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
    """
    :return: A specific list of car brands
    """
    return ["daewoo", "lancia", "abarth", "rambler", "subaru", "suzuki", "nissan", "toyota", "jaguar", "hummer",
            "alpina", "brabus", "bugatti"]

def get_player_name():
    """
    :return: The name entered by the person who will play the game
    """
    return input("Enter your name : ")

def choose_lives(player_name):
    """
    Description: The function is designed to control the player's lives in the game,
    where the number of lives is fixed at 7.
    :param player_name: String, the name of the player for personalized messages and feedback.
    :return: The function always returns the integer value 7,
    which represents the number of lives a player has in the game.
    """
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
    """
    Descripiton: Function will display the current state of the game. It outputs the illustration based on
    the number of incorrect guesses, the current progress of the word being guessed,
    and the number of remaining lives.
    :param hangman_pics: list of strings, where each string represents an image showing the
    Hangman figure at different stages.
    :param wrong_guesses: integer, the current count of incorrect guesses the player has made and
    the number of remaining lives.
    :param guessed_word: list of string, representing the current state of the word being guessed.
    :param lives: integer,the total number of lives the player has at the beginning of the game. In our case, 7.
    :return: The function prints information to the console: current Hangman stage, word progress, the
    current state of the guessed word and the remaining lives.
    """
    print(hangman_pics[wrong_guesses])
    print("\nWord:", ' '.join(guessed_word))
    print(f"Lives left: {lives - wrong_guesses}")

def get_valid_guess(guessed_letters):
    """
    Description: The function is responsible for prompting the player to input a valid guess during the game.
    :param guessed_letters: list of strings, represents the letters that have already been guessed in the current game.
    :return: A valid guessed letter that the player has entered.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
        elif guess in guessed_letters:
            print(f"No! Come on! No! '{guess}' was guessed already! Try again!")
        else:
            return guess

def update_guessed_brand(word, guess, guessed_word):
    """
    Description: The function is used to update the current state of the guessed word.
    :param word: string, the target word that the player is trying to guess.
    :param guess: string, the letter guessed by the player.
    :param guessed_word: list of strings, representing the current state of the guessed word,
    where each element is either a correctly guessed letter or a placeholder.
    :return: This function operates by modifying the guessed_word list in place,
    updating it with correctly guessed letters.
    """
    for i in range(len(word)):
        if word[i] == guess:
            guessed_word[i] = guess

def play_again():
    """
    Description: The function is designed to ask the player if they would like to play the game again.
    It prompts the player for input and only accepts valid responses ('y' for yes or 'n' for no).
    The function uses a loop to ensure valid input is provided before making a decision.
    :return:True: If the player chooses to play again the game can be restarted based on the return value.
            False: If the player chooses not to play again he can exit or conclude based on the return value.
    """
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == 'y':
            print("Yay! You wanna dance?")
            return True
        elif play_again == 'n':
            print("Thanks for playing!")
            return False

def hangman():
    """
    Description: The function implements the classic Hangman game with a theme centered around guessing car brands.
    Players are given 7 lives to guess the letters of a randomly car brand. It uses multiple helper functions to handle
    guessing logic, display updates, and user interaction, creating an engaging gameplay experience.
    The addition of sound effects and humorous messages adds to the entertainment value.
    :return: The game loop, tracks guesses, displays the hangman stages, and determines if the player wins or loses.
    """
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