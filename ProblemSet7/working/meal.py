def main():
    user_time = input("What time is it? ")
    t = convert(user_time)
    print(t)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    # execute when time is in 24 hr format
    if time.count(" ") == 0:
        l, r = time.split(":")
        r = float(r) / 60
        time = float(l) + r
        return time
    # execute when time is in 12 hr format
    else:
        time, meridiem = time.split()
        l, r = time.split(":")
        l = float(l)
        r = float(r) / 60
        # Account for 12 a.m. and 12 p.m.
        if l == 12:
            if meridiem == "a.m.":
                l = 0
            # Account for erroneous 12:60 p.m. input
            if r == 1:
                r = 1.1
            time = l + r
            return time
        # Add 12 if p.m. to convert to 24 hr format
        elif meridiem == "p.m.":
            l = l + 12
            time = l + r
            return time
        # Pass along stripped a.m. time as this is effectively 24 hr format
        else:
            return convert(time)



if __name__ == "__main__":
    main()
