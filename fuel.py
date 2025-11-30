while True:
    f = input("fraction: ")

    try:
        parts = f.split("/")
        x = int(parts[0])
        y = int(parts[1])
        percent = (x/y) * 100

        if percent < 0 or percent >100:
            raise ValueError

        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{round(percent)}%")

        break

    except(IndexError,ValueError, ZeroDivisionError):
        pass






