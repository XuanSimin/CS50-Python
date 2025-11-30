def main():
    text = input("How are you? ")
    convert(text)


def convert(n):
    n = n.replace(":)", "🙂").replace(":(", "🙁")
    print(n)


main()


