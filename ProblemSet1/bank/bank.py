def main():
    greeting = sanitize(input("Greeting: "))
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

def sanitize(user_input):
    user_input = str(user_input.lower().lstrip(" ").rstrip(" "))
    return user_input

main()
