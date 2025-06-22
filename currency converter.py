def currency_converter():
    # Example fixed exchange rates
    rates = {
        'USD': 1.0,        # Base currency
        'INR': 83.0,       # 1 USD = 83 INR
        'EUR': 0.93,       # 1 USD = 0.93 EUR
        'GBP': 0.79,       # 1 USD = 0.79 GBP
        'JPY': 157.23      # 1 USD = 157.23 JPY
    }

    print("Available currencies:", ', '.join(rates.keys()))
    from_currency = input("Convert from (e.g., USD): ").upper()
    to_currency = input("Convert to (e.g., INR): ").upper()

    if from_currency not in rates or to_currency not in rates:
        print("Invalid currency code.")
        return

    try:
        amount = float(input(f"Enter amount in {from_currency}: "))
    except ValueError:
        print("Invalid amount entered.")
        return

    # Convert amount to USD, then to target currency
    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]

    print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")

# Run the converter
currency_converter()
