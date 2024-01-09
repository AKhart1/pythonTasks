def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)
    return f"{amount} {from_currency} is equal to {result} {to_currency}"