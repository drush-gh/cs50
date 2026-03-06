from sys import argv, exit
from csv import DictReader, writer

def main():
    checkFile()
    before = argv[1]
    after = argv[2]
    students = []
    with open(before) as file1:
        reader = DictReader(file1)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})
        with open(after, "w") as file2:
            write = writer(file2)
            write.writerow(["first","last","house"])
            for student in students:
                lastName, firstName = student["name"].split(", ")
                write.writerow([firstName,lastName,student["house"]])

def checkFile():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    else:
        try:
            if extension(argv[1]) != "csv":
                exit("Not a CSV file")
            file = open(argv[1])
            file.close()
            if extension(argv[2]) != "csv":
                exit("Not a CSV file")
        except FileNotFoundError:
            exit(f"Could not read {argv[1]}")

def extension(filename):
    if filename.count(".") == 0:
        return None
    else:
        _, ext = filename.rsplit(".", maxsplit=1)
        return f"{ext}"

if __name__ == "__main__":
    main()

