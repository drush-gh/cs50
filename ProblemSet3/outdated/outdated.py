def main():
    months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }
    while True:
        try:
            date = input("Date: ")
            # middle-endian input
            if date.count("/") == 2:
                m, d, y = date.split("/")
                output(m, d, y)
            # text-based input
            elif date.split(" ", maxsplit = 1)[0] in list(months):
                m, d, y = date.split(" ", maxsplit = 2)
                if d.count(",") != 1:
                    raise ValueError
                d = d.split(",")[0]
                m = months[m]
                output(m, d, y)
            else:
                raise ValueError
            break
        except ValueError:
            pass
        except KeyError:
            pass
        except EOFError:
            print(end = "\n")
            break

def output(m, d, y):
    m, d, y = int(m), int(d), int(y)
    # Account for February incl leap years for fun
    if m == 2 and 1 <= d <= 29:
        if ((y % 4) == 0) and d == 29:
            print(f"{y:04}-{m:02}-{d:02}")
        elif d != 29:
            print(f"{y:04}-{m:02}-{d:02}")
        else:
            raise ValueError
    # Account for 30 day months for fun
    elif m in [4, 6, 9, 11]:
        if 1 <= d <= 30:
            print(f"{y:04}-{m:02}-{d:02}")
        else:
            raise ValueError
    # Account for 31 day months
    elif (m in [1, 3, 5, 7, 8, 10, 12]) and 1 <= d <= 31:
        print(f"{y:04}-{m:02}-{d:02}")
    else:
        raise ValueError

main()
