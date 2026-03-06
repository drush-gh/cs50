from sys import argv, exit
from tabulate import tabulate
from csv import reader

def main():
    checkFile()
    csvFile = argv[1]
    with open(csvFile) as csv:
        readMenu = reader(csv, delimiter=",")
        menu = []
        for row in readMenu:
            menu.append(row)
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))

def checkFile():
    if len(argv) < 2:
        exit("Too few command-line arguments")
    elif len(argv) > 2:
        exit("Too many command-line arguments")
    else:
        try:
            if extension(argv[1]) != "csv":
                exit("Not a CSV file")
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

