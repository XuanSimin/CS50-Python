import random

while True:
    try:
        l = int(input("Level: "))
        if l > 0:
            break
    except ValueError:
        continue

i = random.randint(1, l)

while True:
        try:
            guess = int(input("Guess: "))

            if guess <= 0:
                continue

            if guess < i:
                print("Too small!")

            elif guess > i:
                print("Too large!")

            else:
                print("Just right!")
                break

        except ValueError:
            continue





