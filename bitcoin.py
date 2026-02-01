import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

api_key = "56e53d2ad2385135dbf8162be819eb4db060f0e2a713069a8030c4be085e6ccb"

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + api_key)
except requests.RequestException:
    sys.exit("API request failed")

data = response.json()
price = float(data["data"]["priceUsd"])

print(f"${bitcoins * price:,.4f}")
