source = input("What is in your mind? ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for _ in vowels:
    source = source.replace(_, '')

print(source)
