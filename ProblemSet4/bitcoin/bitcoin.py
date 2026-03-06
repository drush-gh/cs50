import requests
from sys import argv, exit

try:
    if len(argv) == 1:
        exit("Missing command-line argument")
    bitcoin = float(argv[1])
except ValueError:
    exit("Command-line argument is not a number")

try:
    coincap_price = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=6b6c668c221e02d725e00cacdcd8b8ed47c5f9c2810b0ee57f2269f0f6442a7d"
    response = requests.get(coincap_price)
    #print(f"1 BTC is currently ${response.json()["data"]["priceUsd"]} USD")
    usd_conversion = float(response.json()["data"]["priceUsd"])
    usd = usd_conversion * bitcoin
    print(f"${usd:,.4f}")
except requests.RequestException:
    print("There was an error with the request. Please try again later")

