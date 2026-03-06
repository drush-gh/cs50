import validators

emailCheck = input("What's your email address? ")

if validators.email(emailCheck):
    print("Valid")
else:
    print("Invalid")
