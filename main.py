from random import randint
from art import logo
import os
clear = lambda: os.system('cls')

chosen_number = randint(1, 100)

def guessing_attempts(attempts):
    """Comparing the user's number with the chosen number and decreasing the number of attempts for incorrect guesses."""
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_number = int(input("Make a guess: "))
        if user_number < chosen_number:
            attempts -= 1
            print("Too low.")
        elif user_number > chosen_number:
            attempts -= 1
            print("Too high.")
        elif user_number == chosen_number:
            print(f"You got it! The answer is {chosen_number}.")
            attempts = 0
        if attempts < 1 and user_number != chosen_number:
            print(f"You have run out of guesses, you lose.\nThe correct number was {chosen_number}.")
        elif attempts > 0 and user_number != chosen_number:
            print("Guess again.")

def play_game():
    """Starts the game of guessing a number."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # print(f"Psst the number is {chosen_number}.")
    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if difficulty_level == "easy":
        guessing_attempts(10)
    elif difficulty_level == "hard":
        guessing_attempts(5)

play_game()

continue_playing = True
while continue_playing:
    repeat_game = input("Do you want to play another game? Type 'y' or 'n': ").lower()
    if repeat_game == "y":
        clear()
        chosen_number = randint(1, 100)
        play_game()
    else:
        print("Maybe next time! Goodbye!")
        continue_playing = False