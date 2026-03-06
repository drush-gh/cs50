from sys import exit
from inflect import engine

namelist = []

while True:
    try:
        name = input("")
        if name == "":
            continue
        else:
            namelist.append(name)
    except EOFError:
        print (f"Adieu, adieu, to {engine().join(namelist)}")
        exit()
