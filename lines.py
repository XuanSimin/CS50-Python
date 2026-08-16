import sys

if len(sys.argv) != 2:
    sys.exit("Too few or too many command line argument")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    count = 0
    with open(filename, "r") as file:
        for line in file:
            stripped = line.strip()
            if stripped == "" or stripped.startswith("#"):
                continue
            count += 1

    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")
