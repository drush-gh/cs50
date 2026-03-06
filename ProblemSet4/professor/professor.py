from random import randint

def main():
    level = get_level()
    equations = 0
    score = 0
    while equations < 10:
        if correct_check(level):
            score += 1
        equations += 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level not in range(1, 4):
        raise ValueError
    elif level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)

def correct_check(level):
    x = generate_integer(level)
    y = generate_integer(level)
    attempt = 0
    answer = -1
    while answer != (x + y):
        try:
            if attempt > 2:
                print(f"{x} + {y} = {x + y}")
                return False
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                print("EEE")
                answer = -1
                attempt += 1
                continue
        except ValueError:
            print("EEE")
            answer = -1
            attempt += 1
            continue


if __name__ == "__main__":
    main()
