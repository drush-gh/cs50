from sys import exit
from inflect import engine

namelist = []

while True:
    try:
        name = input("Name: ")
        if name == "":
            continue
        else:
            namelist.append(name)
    except EOFError:
        print (f"\nAdieu, adieu, to {engine().join(namelist)}")
        exit()
