def main():
    x = input("what time is it? ")
    x = convert(x)
    if 7.0 <= x <= 8.0:
        print("breakfast time ")
    elif 12.0 <= x <= 13.0:
        print("lunch time ")
    elif 18.0 <= x <= 19.0:
        print("dinner time ")
    else:
        pass


def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60


if __name__ == "__main__":
    main()
