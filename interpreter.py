expression = input("what do you want to calculate? ")
x, operator, y = expression.split()
x = float(x)
y = float(y)
if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y
else:
    print("invalid")

print(f"{result:.1f}")
