import requests


def get_rate(currency):
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=" + currency + "&json"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data[0]["rate"]


currencies = ["EUR", "USD", "PLN"]

currency = input("Enter currency (EUR, USD, PLN): ").upper()

if currency not in currencies:
    print("Unknown currency")
else:
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Error: enter a number")
    else:
        if amount <= 0:
            print("Error: amount must be greater than 0")
        else:
            try:
                rate = get_rate(currency)
            except (requests.RequestException, IndexError, KeyError, ValueError):
                print("Error: cannot get the rate from NBU")
            else:
                result = amount * rate
                print("Rate:", rate)
                print(amount, currency, "=", round(result, 2), "UAH")