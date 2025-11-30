greet = input("What is your greeting word? ")
if greet.lower().strip() == "hello":
    print("$0")
elif greet.lower().strip().startswith("h"):
    print("$20")
else:
    print("$100")
