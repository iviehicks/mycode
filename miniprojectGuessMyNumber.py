import random

def guess_my_number_game():
    # Generate a random number between 1 and 10 (you can adjust the range as needed)
    secret_number = random.randint(1, 10)

    print("Welcome to Guess My Number game! Think you can do it??")
    print("I'm thinking of a number between 1 and 10. Can you tell me what it is?")

    max_attempts = 3
    attempts = 0

    #while loop to let user keep guessing
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))

    # Allow the user three attempts to guess the number
   # for attempt in range(3):
    #    guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Holy Sh...!! You did it! You got my number! Well done!")
            break  # Exit the loop if the guess is correct
        elif guess < secret_number:
            print("Too low! Aim higher and try again.")
        else:
            print("Too high! Take it down a notch and try again.")
    else:
        print(f"Well... you didn't make it and you've run out of attempts. The correct number was {secret_number}.")

    attempts += 1

# Run the game
guess_my_number_game()
