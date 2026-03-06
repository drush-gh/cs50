def main():
    clean_input = sanitize(input("File name: "))
    if extension(clean_input) == ".gif":
        print("image/gif")
    elif extension(clean_input) == ".jpg" or extension(clean_input) == ".jpeg":
        print("image/jpeg")
    elif extension(clean_input) == ".png":
        print("image/png")
    elif extension(clean_input) == ".pdf":
        print("application/pdf")
    elif extension(clean_input) == ".txt":
        print("text/plain")
    elif extension(clean_input) == ".zip":
        print("application/zip")
    else:
        print("application/octet-stream")

def sanitize(user_input):
    user_input = str(user_input.lower().strip()) #this is an inline comment
    return user_input

# return extension in format .ext to match table in https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types
def extension(filename):
    if filename.count(".") == 0:
        return None
    else:
        _, ext = filename.rsplit(".", maxsplit=1)
        return f".{ext}"

main()
