from sys import exit
from random import randint

def main():
    while True:
        try:
            level = int(input("Level: "))
            level = randint(1, level)
            break
        except ValueError:
            continue

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            game(level, guess)
        except ValueError:
            continue

def game(level, guess):
    if level == guess:
        print("Just Right!")
        exit()
    elif guess > level:
        print("Too large!")
    else:
        print("Too small!")

if __name__ == "__main__":
    main()
