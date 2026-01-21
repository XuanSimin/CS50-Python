def get_groceries():
    items = {}
    while True:
        try:
            item = input("What is on the list?\n").upper()
            items[item] = items.get(item, 0) + 1
        except EOFError:
            break

    for item in sorted(items):
        print(items[item], item)

get_groceries()
