txt = input("Input: ")

for char in txt:
    if char.lower() in ["a", "e", "i", "o", "u"]:
        l, r = txt.split(char, maxsplit=1)
        txt = l + r

print(txt)
