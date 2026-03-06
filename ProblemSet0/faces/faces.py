def main():
    user_input = input("Please enter your input: ")
    convert(user_input)

def convert(string):
    string = str(string)
    print(string.replace(":)", "🙂").replace(":(", "🙁"))


main()
