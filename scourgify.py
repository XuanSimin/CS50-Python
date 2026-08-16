import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, "r", newline="") as input:
        reader = csv.DictReader(input)

        with open(output_file, "w", newline="") as output:
            writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")

                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")
