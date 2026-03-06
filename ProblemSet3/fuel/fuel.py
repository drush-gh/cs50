def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = negativeInt(int(x))
            y = negativeInt(int(y))
            tank = x / y
            if tank > 1:
                continue
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        
    if tank <= 0.01:
        print("E")
    elif tank >= 0.99:
        print("F")
    else:
        output = round(tank*100)
        print(f"{output}%")

def negativeInt(int):
    if int < 0:
        raise ValueError
    else:
        return int

main()
