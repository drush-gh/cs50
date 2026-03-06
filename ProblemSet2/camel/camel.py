def main():
    camelCase = input("camelCase: ")
    camelCase = snakeConverter(camelCase)
    print("snake_case:", camelCase)

def snakeConverter(variable):
    for letter in variable:
        if letter.isupper():
            l, r = variable.split(letter)
            variable = l + "_" + letter.lower() + r
    return variable

main()
