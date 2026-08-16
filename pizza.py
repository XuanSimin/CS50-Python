import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("File must be a CSV")

    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            data = list(reader)

    except FileNotFoundError:
        sys.exit("File does not exist")

    headers = data[0]
    rows = data[1:]

    print(tabulate(rows, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
