import re

def main():
    print(convert("12:00 AM to 5:00 AM")) #input("Hours: ")
    print(convert("12 AM to 5 AM"))
    print(convert("12:00 AM to 5 AM"))
    print(convert("12 AM to 5:00 AM"))
    print(convert("12:60 AM to 5:00 AM"))
    print(convert("13:00 PM to 12:00 AM"))

def convert(s):
    # Check on format 9:00 AM to 5:00 PM
    if time := re.search(r"^(?P<firstTime>([1-9]|1[0-2]):[0-5]\d [AP]M) to (?P<secondTime>([1-9]|1[0-2]):[0-5]\d [AP]M)$", s):
        return timeCheck(time.group("firstTime"), time.group("secondTime"))
    # Check on format 9 AM to 5 PM
    elif time := re.search(r"^(?P<firstTime>([1-9]|1[0-2]) [AP]M) to (?P<secondTime>([1-9]|1[0-2]) [AP]M)$", s):
        #statement
        return f"{time.group("firstTime")} {time.group("secondTime")}"
    # Check on format 9:00 AM to 5 PM
    elif time := re.search(r"^(?P<firstTime>([1-9]|1[0-2]):[0-5]\d [AP]M) to (?P<secondTime>([1-9]|1[0-2]) [AP]M)$", s):
        #statement
        return f"{time.group("firstTime")} {time.group("secondTime")}"
    # Check on format 9 AM to 5:00 PM
    elif time := re.search(r"^(?P<firstTime>([1-9]|1[0-2]) [AP]M) to (?P<secondTime>([1-9]|1[0-2]):[0-5]\d [AP]M)$", s):
        #statement
        return f"{time.group("firstTime")} {time.group("secondTime")}"
    else:
        return ValueError


def timeCheck(firstTime, secondTime):


    return f"{firstTime} to {secondTime}"

if __name__ == "__main__":
    main()



