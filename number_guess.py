import random

def play_round():
    secret = random.randint(1, 10)
    attempts = 0
    print("\nI'm thinking of a number between 1 and 10.")

    while True:
        guess_str = input("Take a guess: ")

        # Check it's a number
        if not guess_str.isdigit():
            print("That wasn't a valid number. Please enter a number.")
            continue

        guess = int(guess_str)

        # Check the range
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue

        attempts += 1  # Count only valid guesses

        if guess == secret:
            print(f"You guessed it in {attempts} attempt(s)!")
            break
        elif guess < secret:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

def main():
    print("Welcome to Guess the Number!")

    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
