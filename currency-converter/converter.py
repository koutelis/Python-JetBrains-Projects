import requests


class CurrencyConverter:
    """
    A class that calculates the amount of money you get by converting one currency to another.
    :ivar source_currency: a currency to be converted to other currencies.
    :cvar cache: a dictionary of currencies and their rates.
    """

    cache = {}

    def __init__(self, currency):
        self.source_currency = currency.lower()

    def get_float_rates(self):
        """
        Request source currency's current rates in json
        :return: json object
        """
        url = f'http://www.floatrates.com/daily/{self.source_currency}.json'
        r = requests.get(url)
        return r.json()

    def cache_currency(self, currency):
        """ Store a currency's rates to the cache."""
        currency = currency.lower()
        if not self.source_currency == currency:
            CurrencyConverter.cache[currency] = self.get_float_rates().get(currency).get('rate')

    @classmethod
    def is_cached(cls, currency):
        """Check if a currency is saved in the cache"""
        if CurrencyConverter.cache.get(currency):
            return True
        else:
            return False

    def convert(self, source_amount, target_currency):
        """
        Convert a specified amount of source currency to a target currency.
        :param source_amount: the amount of source currency to be converted.
        :param target_currency: the currency to convert to.
        """
        target_currency = target_currency.lower()
        if not CurrencyConverter.is_cached(target_currency):
            self.cache_currency(target_currency)

        rate = CurrencyConverter.cache.get(target_currency)
        conv_amount = round(source_amount * rate, 2)

        print(f'{source_amount} {self.source_currency} = {conv_amount} {target_currency}.')


def run():
    """Run this function to start the currency converter"""

    print('Input currency to convert from (abbreviated): ')
    source_currency = input()
    cc = CurrencyConverter(source_currency)

    # cache a few common currencies
    cc.cache_currency('usd')
    cc.cache_currency('eur')
    cc.cache_currency('gbp')

    print('Input currency to convert to (abbreviated): ')
    to_currency = input()

    while to_currency != '':
        print('Input amount to convert: ')
        amount = float(input())
        cc.convert(amount, to_currency)
        print('Input currency to convert to (abbreviated), or press enter to exit: ')
        to_currency = input()

