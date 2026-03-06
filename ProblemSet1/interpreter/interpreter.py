user_input = str(input("Expression: "))

x, y, z = user_input.split()

x = float(x)

z = float(z)

match y:
    case "+":
        print(round(x + z, 1))
    case "-":
        print(round(x - z, 1))
    case "*":
        print(round(x * z, 1))
    case "/":
        print(round(x / z, 1))
