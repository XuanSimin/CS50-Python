import inflect

names = []
p = inflect.engine()

while True:
    try:
        name = input("name: ").capitalize()
        names.append(name)

    except EOFError:
            break

update = p.join(names)

print(f"Adieu, adieu, to " + update)
