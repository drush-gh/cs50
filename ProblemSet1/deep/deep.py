def main():
    sanitized_input = sanitize(input("What is the Answer to the Great Question of Life, the Universe and Everything? "))
    if sanitized_input == "42" or sanitized_input == "forty-two" or sanitized_input == "forty two":
        print("Yes")
    else:
        print("No")

def sanitize(user_input):
    user_input = str(user_input.lower().lstrip(" ").rstrip(" "))
    return user_input

main()
