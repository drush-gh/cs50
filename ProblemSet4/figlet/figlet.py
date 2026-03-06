from pyfiglet import figlet_format
from sys import argv, exit

if len(argv) == 1:
    input = input("Input: ")
    output = figlet_format(input)
elif len(argv) == 3:
    if argv[1] in ["-f", "--format"]:
        input = input("Input: ")
        output = figlet_format(input, font=argv[2])
else:
    exit("Use -f or --format to specify your font")

print(output)
