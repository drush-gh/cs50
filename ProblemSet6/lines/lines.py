from sys import argv, exit

def main():
    checkFile()
    pythonFile = argv[1]
    with open(pythonFile) as file:
        lines = file.readlines()
        whitespace = 0
        commented = 0
        for line in lines:
            if line.lstrip() == "":
                whitespace += 1
            if line.lstrip().startswith("#"):
                commented += 1
        print(len(lines) - whitespace - commented)

def checkFile():
    if len(argv) < 2:
        exit("Too few command-line arguments")
    elif len(argv) > 2:
        exit("Too many command-line arguments")
    else:
        try:
            if extension(argv[1]) != "py":
                exit("Not a Python file")
            file = open(argv[1])
            file.close()
        except FileNotFoundError:
            exit("File does not exist")

def extension(filename):
    if filename.count(".") == 0:
        return None
    else:
        _, ext = filename.rsplit(".", maxsplit=1)
        return f"{ext}"

if __name__ == "__main__":
    main()
