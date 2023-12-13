import requests

def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    data = response.json()
    
    if data:
        return data[0]['rate']
    else:
        return None

def convert_currency(amount, from_currency, to_currency):
    rate_from = get_exchange_rate(from_currency)
    rate_to = get_exchange_rate(to_currency)

    if rate_from is not None and rate_to is not None:
        converted_amount = amount * rate_from / rate_to
        return converted_amount
    else:
        return None

def main():
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency code (e.g., EUR, USD, PLN): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR, USD, PLN): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Error fetching exchange rates. Please try again later.")

if __name__ == "__main__":
    main()
