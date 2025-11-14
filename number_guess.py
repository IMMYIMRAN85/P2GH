import random

def main():
    print("Welcome to Guess the Number!")
    secret = random.randint(1, 10)

    user_input = input("Guess a number between 1 and 10: ")

    try:
        guess = int(user_input)
    except ValueError:
        print("That wasn't a valid number. Please run the game again and enter a number.")
        return

    if guess == secret:
        print("You guessed it!")
    else:
        print("Sorry, the number was", secret)

if __name__ == "__main__":
    main()

