"""     ------ Higher Lower Game ------

        Rules: Select which account has more followers (at the time this program was made): A or B
               If correct, account B will become account A, and new account B will be randomly selected.
               If incorrect, the game ends. 
"""

import random
from game_data import data
import art


def choose_random_account():
    """Function to randomly select an account from a list of accounts."""
    return random.choice(data)


def check_followers(account_1, account_2):
    """Check which account has more followers.
    If both accounts have same number of followers, then replace the first account
    by another account from the list."""
    if account_1['follower_count'] == account_2['follower_count']:
        account_1 = choose_random_account()
    if account_1['follower_count'] > account_2['follower_count']:
        return "A"
    else:
        return "B"


final_score = 0
stop_game = False

# Randomly selecting any 2 accounts.
person_1 = choose_random_account()
person_2 = choose_random_account()

while not stop_game:
    # Print the logos and description of both accounts.
    print(art.logo)
    print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}.")
    print(art.vs)
    print(f"Against B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}.")

    # Input user's guess.
    user_guess = input("Who has more followers? Type 'A' or 'B': ")

    is_correct = check_followers(person_1, person_2)

    # Check if the user guessed correctly.
    # If yes, increase the score,
    # The previous 2nd account is 1st account now. New 2nd account is randomly picked.
    if user_guess == is_correct:
        final_score += 1
        print(f"You're right! Current score: {final_score}")
        person_1 = person_2
        person_2 = random.choice(data)

    # If the user didn't guess correctly,
    # Print the final score and end the game.
    else:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        stop_game = True
