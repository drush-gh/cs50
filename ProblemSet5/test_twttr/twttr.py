def main():
    txt = input("Input: ")
    txt = shorten(txt)
    print(txt)


def shorten(word):
    for char in word:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            l, r = word.split(char, maxsplit=1)
            word = l + r
    return word

if __name__ == "__main__":
    main()
