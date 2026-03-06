def main():
    while True:
        try:
            fraction = input("Fraction: ")
            tank = convert(fraction)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    print(gauge(tank))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x < 0 or y < 0:
            raise ValueError
        if x > y:
            raise ValueError
        tank = (x / y) * 100
        return round(tank)
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
