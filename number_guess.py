import random

def main():
    print("Welcome to Guess the Number!")
    secret = random.randint(1, 10)
    attempts = 0

    while True:
        attempts += 1
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == secret:
            print(f"You guessed it in {attempts} attempt(s)!")
            break
        else:
            print("Nope, try again.")

if __name__ == "__main__":
    main()

