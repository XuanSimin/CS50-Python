import sys
import random
import pyfiglet

def main():
    figlet = pyfiglet.Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")

        figlet.setFont(font=sys.argv[2])

    else:
        sys.exit("Invalid usage")

    text = input("Input: ")

    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
