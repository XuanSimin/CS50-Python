import re

camelcase = input("name ")
snakecase = re.sub(r"([A-Z])", r"_\1", camelcase).lower()

print(snakecase)
