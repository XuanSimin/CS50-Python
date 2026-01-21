months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            M, D, Y = date.split("/")
            month = int(M)
            day = int(D)
            year = int(Y)

        elif "," in date:
            month_str, year = date.split(",")
            month_name, day = month_str.split()

            month = months.index(month_name) + 1
            day = int(day)
            year = int(year)

        else:
            raise ValueError

        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break

    except (ValueError, IndexError):
        continue
