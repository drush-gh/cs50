def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if lettersLength(s) and numberCheck(s):
        return True
    else:
        return False

def lettersLength(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s[0].isalpha() and s[1].isalpha():
            return True
    else:
        return False

def numberCheck(s):
    numbers = 0
    for char in s:
        if char.isnumeric() and char != "0":
            numbers += 1
        elif char == "0" and numbers == 0:
            return False
        elif char.isalpha() and numbers > 0:
            return False
    return True

if __name__ == "__main__":
    main()
