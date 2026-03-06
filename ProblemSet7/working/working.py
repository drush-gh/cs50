import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if time := re.search(r"^(?P<firstTime>((([1-9]|1[0-2]):[0-5]\d [AP]M)|(([1-9]|1[0-2]) [AP]M))) to (?P<secondTime>((([1-9]|1[0-2]):[0-5]\d [AP]M)|(([1-9]|1[0-2]) [AP]M)))$", s):
        firstTime = time.group("firstTime")
        secondTime = time.group("secondTime")
        firstTime = military(firstTime)
        secondTime = military(secondTime)
        return f"{firstTime} to {secondTime}"
    else:
        raise ValueError

def military(time):
    time, meridiem = time.split()
    if time.count(":") == 1:
        l, r = time.split(":")
        if 1 <= int(l) <= 9:
            if meridiem == "PM":
                l = str(int(l) + 12)
                return f"{l}:{r}"
            return f"0{l}:{r}"
        if l == "12" and meridiem == "AM":
            l = "00"
        elif l != "12" and meridiem == "PM":
            l = str(int(l) + 12)
        return f"{l}:{r}"
    elif time == "12" and meridiem == "AM":
        return "00:00"
    elif time == "12" and meridiem == "PM":
        return f"{time}:00"
    elif time != "12" and meridiem == "PM":
        time = str(int(time) + 12)
        return f"{time}:00"
    elif 1 <= int(time) <= 9:
        return f"0{time}:00"
    else:
        return None

if __name__ == "__main__":
    main()
