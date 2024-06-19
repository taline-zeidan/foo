from higher_lower_data import data
from higher_lower_art import logo, vs
import random
import os

def clear():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def get_follower_count(name):
    """Takes a name as a parameter and returns the follower count. If the person does not exist, returns -1."""
    for entry in data:
        if entry['name'] == name:
            return entry['follower_count']
    return -1

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

def get_random_person():
    """Returns a random person from the data."""
    rand_entry = random.choice(data)
    person = f"{rand_entry['name']}, a {rand_entry['description']} from {rand_entry['country']}."
    return rand_entry['name'], person

def play_game():
    print(logo)
    score = 0
    person_a_name, person_a = get_random_person()
    person_b_name, person_b = get_random_person()

    while person_a_name == person_b_name:
        person_b_name, person_b = get_random_person()

    game_should_continue = True
    while game_should_continue:
        clear()
        print(f"Compare A: {person_a}")
        print(vs)
        print(f"Against B: {person_b}")

        chosen_letter = input("Who has more followers? Type 'A' or 'B': ").upper()
        while chosen_letter not in ['A', 'B']:
            chosen_letter = input("Enter a valid letter. Choose 'A' or 'B': ").upper()

        a_followers = get_follower_count(person_a_name)
        b_followers = get_follower_count(person_b_name)

        if check_answer(chosen_letter, a_followers, b_followers):
            score += 1
            print(f"You're right! Current score: {score}.")
            person_a_name = person_b_name
            person_a = person_b
            person_b_name, person_b = get_random_person()
            while person_a_name == person_b_name:
                person_b_name, person_b = get_random_person()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

def play():
    while True:
        play_game()
        play_again = input("Do you want to play again? Type 'Y' or 'N': ").upper()
        if play_again != 'Y':
            break
        clear()

play()
