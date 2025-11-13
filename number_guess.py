import random

def main():
    print("Welcome to Guess the Number!")
    secret = random.randint(1, 10)

    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        print("You guessed it!")
    else:
        print("Sorry, the number was", secret)

if __name__ == "__main__":
    main()
