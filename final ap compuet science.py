import random

# Define a procedure to get user input for the game
def get_guess():
    while True:
        guess = input("Guess a number between 1 and 10: ")
        if guess.isdigit() and 1 <= int(guess) <= 10:
            return int(guess)
        else:
            print("Invalid input. Please enter a number between 1 and 10.")

# Define a procedure to check if the user's guess matches the randomly generated number
def check_guess(guess, num):
    if guess == num:
        print("Congratulations! You guessed the correct number!")
        return True
    else:
        if guess > num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        return False

# Define the main game procedure
def play_game():
    print("Welcome to the Guessing Game!")
    num = random.randint(1, 10)
    guesses = []
    while len(guesses) < 5:
        guess = get_guess()
        guesses.append(guess)
        if check_guess(guess, num):
            break
    else:
        print("Sorry, you ran out of guesses. The number was", num)

# Call the main game procedure to start the game
play_game()
