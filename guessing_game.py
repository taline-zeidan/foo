from guessing_art import logo
import random

def update_attempts(user_guess, random_nb, attempts):
    if user_guess > random_nb:
        print("Too high.")
        return attempts - 1
    elif user_guess < random_nb:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {random_nb}.")
def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    while difficulty.lower() != 'easy' and difficulty.lower() != 'hard':
            difficulty = input("Enter a valid difficulty. Type 'easy' or 'hard': ")
    if difficulty.lower() == 'easy':
        return 10
    elif difficulty.lower() == 'hard':
        return 5     
def get_guess():
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
def play():
    random_nb= random.randint(1,100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # print(f"psssttt it's {random_nb}")
    attempts =  choose_difficulty()
    user_guess = 0
    while user_guess != random_nb:
       print(f"You have {attempts} attempts remaining to guess the number.")
       user_guess = get_guess()
       attempts = update_attempts(user_guess, random_nb, attempts)

       if attempts == 0:
          print("You've run out of guesses. You lose.")
          print(f"It was {random_nb}. Do better.")
          return
       elif user_guess != random_nb:
          print("Guess again.")
play()       