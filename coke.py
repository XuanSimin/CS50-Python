print("amount due: 50 ")
x = 50
while x > 0:
    y = int(input("coin insert: "))
    if y in [25, 10, 5]:
        x = x - y
        if x > 0:
            print(f"amount due: {x}")

print(f"change owed: {abs(x)}")




