import re

def main():
    print(count(input("Text: ")))


def count(s):
    umCount = 0
    while True:
        try:
            if s.count(re.search(r"(um\b)", s)) > 0:
                s = s.split(re.search(r"(um\b)", s), maxsplit=1)
                s = s[1]
                umCount += 1
        except:
            return umCount


if __name__ == "__main__":
    main()
