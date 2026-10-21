import sys
import requests

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Paste your full key between these quotation marks:
    api_key = "04ed9ace9ede7a645cca884ae769a7b9172d43184027c88f6472f2a096a0e618"

    try:
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        price = float(data["data"]["priceUsd"])
        total = bitcoins * price

        print(f"${total:,.4f}")

    except Exception as e:
        sys.exit(f"Error fetching Bitcoin price: {e}")

if __name__ == "__main__":
    main()
