import re

def main():
    print(count(input("Text: ")))

def count(s):
    umCount = re.findall(r"\b[uU][mM]\b", s)
    return len(umCount)

if __name__ == "__main__":
    main()
