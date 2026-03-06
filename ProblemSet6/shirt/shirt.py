from sys import argv, exit
from PIL import Image, ImageOps

def main():
    checkFile()
    with Image.open(argv[1]) as img:
        with Image.open("shirt.png") as shirt:
            img = ImageOps.fit(img, shirt.size)
            img.paste(shirt, mask=shirt)
            img.save(argv[2])

def checkFile():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    elif extension(argv[1]).lower() not in ["jpg", "jpeg", "png"]:
        exit("Invalid input")
    elif extension(argv[2]).lower() not in ["jpg", "jpeg", "png"]:
        exit("Invalid input")
    else:
        try:
            if extension(argv[1]) != extension(argv[2]):
                exit("Input and output have different extensions")
            file = open(argv[1])
            file.close()
        except FileNotFoundError:
            exit("File does not exist")

def extension(filename):
    if filename.count(".") == 0:
        return ""
    else:
        _, ext = filename.rsplit(".", maxsplit=1)
        return f"{ext}"

if __name__ == "__main__":
    main()

