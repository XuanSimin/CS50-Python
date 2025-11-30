def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False

    for i, ch in enumerate(s):
        if ch.isdigit():
            if ch == "0":
                return False
            after = s[i:]
            if not after.isdigit():
                return False
            break

    return True


main()
