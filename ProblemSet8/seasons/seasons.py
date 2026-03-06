from datetime import date
from sys import exit
import re
from inflect import engine

def main():
    birthdate = input("Date of Birth: ")
    if not validate(birthdate):
        exit("Invalid date")
    # difference is a timedelta object with .days attribute
    difference = date.today() - date.fromisoformat(birthdate)
    minutes = difference.days * 24 * 60
    print(engine().number_to_words(minutes, andword="").capitalize(), engine().plural_noun("minute", minutes))

def validate(birthdate):
    if check := re.search(r"^(?P<year>[1-9]\d\d\d|0[1-9]\d\d|00[1-9]\d|000[1-9])-(?P<month>1[0-2]|0[1-9])-(?P<day>[1-2]\d|3[0-1]|0[1-9])$", birthdate):
        year, month, day = check.group("year"), check.group("month"), check.group("day")
        if int(year) % 4 == 0 and month == "02" and day == "29":
            return True
        elif month == "02" and int(day) not in range(29):
            return False
        elif int(month) in [4, 6, 9, 11] and int(day) not in range(31):
            return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
