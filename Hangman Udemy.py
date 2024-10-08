import random
import pygame.mixer # This needs to be installed using the terminal : pip install pygame

pygame.mixer.init()
correct_sound = pygame.mixer.Sound("correct.wav")
incorrect_sound = pygame.mixer.Sound("wrong.wav")
clap = pygame.mixer.Sound("clap.wav")
lose = pygame.mixer.Sound("lose.wav")


def hangman_logo():
    """Generated a logo to match the game name.
    """
    hang_logo = """
    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    """

    print(hang_logo)


def get_brand_list():
    """
    Created a list of max seven letters car brands from which the game will randomly choose a brand.
    """
    return ["daewoo", "lancia", "abarth", "rambler", "subaru", "suzuki", "nissan", "toyota", "jaguar", "hummer",
            "alpina", "brabus", "bugatti", "ferrari", "peugeot", "bentley", "renault"]


def get_player_name():
    """
    Asking the player's name, which will follow throughout the game.
    """
    return input("Enter your name: ")


def display_status(hangman_pics, wrong_guesses, guessed_word, lives):
    """
    Description: Function will display the current state of the game. It outputs the illustration based on
    the number of incorrect guesses, the current progress of the word being guessed,
    and the number of remaining lives.
    :param hangman_pics: List of strings, where each string represents an image showing the
                        Hangman figure at different stages.
    :param wrong_guesses: Integer, the current count of incorrect guesses the player has made and
                          the number of remaining lives.
    :param guessed_word: List of string, representing the current state of the word being guessed.
    :param lives: Integer,the total number of lives the player has at the beginning of the game. In our case, 7.
    :return: The function prints information to the console: current Hangman stage, word progress, the
             current state of the guessed word and the remaining lives.
    """
    print(hangman_pics[wrong_guesses])
    print("\nWord:", ' '.join(guessed_word))
    print(f"Lives left: {lives - wrong_guesses}")


def get_valid_guess(guessed_letters):
    """
    The function is responsible for prompting the player to input a valid guess during the game.
    :param guessed_letters: List of strings, represents the letters that have already been guessed in the current game.
    :return: A valid guessed letter that the player has entered.
    """
    while True:
    #This is an infinite loop that will keep running until a valid input (guess) is provided by the player.
        guess = input("Guess a letter: ").lower()
        #The program prompts the player to input a letter with the message and stores it in guess variable.
        if len(guess) != 1:
        #The player is only allowed to enter exactly one character per guess.
            print("Invalid input! Please enter exactly one character.")
        elif guess in guessed_letters:
        #This checks if the guessed letter has already been guessed by the player.
            print(f"No! Come on! No! '{guess}' was guessed already! Try again!")
        else:
            #If none of the above conditions are met, the program executes the code in this block.
            return guess
            #The valid guess is returned, and the loop stops.


def update_guessed_brand(word, guess, guessed_word):
    """
    Description: The function is used to update the current state of the guessed word.
    :param word: String, the target word that the player is trying to guess.
    :param guess: String, the letter guessed by the player.
    :param guessed_word: List of strings, representing the current state of the guessed word,
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
        replay = input("\nWould you like to play again? (y/n): ").lower()
        if replay == 'y':
            print("Yay! You wanna dance?")
            return True
        elif replay == 'n':
            print("Thanks for playing!")
            return False


def hangman():
    """
    Description: The function implements the classic Hangman game with a theme centered around guessing car brands.
    Players are given 7 lives to guess the letters of a random car brand. It uses multiple helper functions to handle
    guessing logic, display updates, and user interaction, creating an engaging gameplay experience.
    The addition of sound effects and humorous messages adds to the entertainment value.
    :return: The game loop, tracks guesses, displays the hangman stages, and determines if the player wins or loses.
    """

    word_list = get_brand_list()
    hangman_pics = ['''+---+\n|   |\n    |\n    |\n    |\n    |\n=========''',
                    '''+---+\n|   |\n😢  |\n    |\n    |\n    |\n=========''',
                    '''+---+\n|   |\n😢  |\n|   |\n    |\n    |\n=========''',
                    '''+---+\n|   |\n😢  |\n/|   |\n    |\n    |\n=========''',
                    '''+---+\n|   |\n😢  |\n/|\\ |\n    |\n    |\n=========''',
                    '''+---+\n|   |\n😢  |\n/|\\ |\n/    |\n    |\n=========''',
                    '''+---+\n|   |\n😢  |\n/|\\ |\n/ \\ |\n    |\n=========''',
                    '''+-----+\n|     |\n😵    |\n/|\\   |\n/ \\   |\n🔥🔥🔥   |\n=========''']

    word = random.choice(word_list) #This line randomly selects a word from the word_list.
    guessed_word = ['_'] * len(word) #This line creates a list of underscores with the same length as the chosen word.
    guessed_letters = [] # This initializes an empty list that will store the letters the player has already guessed.
    lives = 7  # Directly setting lives to 7

    print(f"Welcome {player_name}, to the best Hangman game you ever played! (Car Brands Edition 🚗.)")
    wrong_guesses = 0

    while wrong_guesses < lives and '_' in guessed_word: #This is the main loop of the game.
        ##The game continues running as long as the number of wrong guesses is less than the number of lives
        ##and there are still underscores in guessed_word, meaning that the word hasn’t been fully guessed yet.
        display_status(hangman_pics, wrong_guesses, guessed_word, lives)
        #This function displays the current status of the game
        guess = get_valid_guess(guessed_letters)
        #This prompts the player to guess a letter, ensuring it's a valid input (one letter and not repeated).
        guessed_letters.append(guess)
        #This adds the guessed letter to the list so that the player cannot guess the same letter again.

        if guess in word: #This checks if the guessed letter is present in the chosen word.
            update_guessed_brand(word, guess, guessed_word)
            #This function updates guessed_word by replacing the underscores with the correctly
            #guessed letter at the appropriate positions.
            print(f"AAhhh... much better, {player_name}! The letter '{guess}' is in the word.")
            correct_sound.play()
        else: #If the guessed letter is not in the word this will run.
            print(f"Not in this lifetime, {player_name}! The letter '{guess}' is not in the word.")
            incorrect_sound.play()
            wrong_guesses += 1 #The counter is incremented by 1 since the player guessed incorrectly

    if '_' not in guessed_word: #This checks if the player has guessed the entire word.
        print(f"\nDear diary... Jackpot! {player_name} guessed the word: {word.upper()}")
        clap.play()
    else:
        print(hangman_pics[wrong_guesses])
        print(f"\nDying ain't much of a living, {player_name}. The word was: {word.upper()}")
        lose.play()

    if play_again():
        #This checks if the player wants to play another round of the game by calling the play_again() function
        hangman()


# Start the game
hangman_logo()
player_name = get_player_name()
hangman()
