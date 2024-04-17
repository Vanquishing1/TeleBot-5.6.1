import requests
import json
from config import keys




class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote.lower()]
            base_ticker = keys[base.lower()]
        except KeyError as e:
            raise ConvertionException(f'Не удалось обработать валюту {e.args[0]}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        if r.status_code != 200:
            raise ConvertionException('Ошибка при получении данных о курсе.')

        data = r.json()
        if base_ticker not in data:
            raise ConvertionException('Отсутствуют данные для конвертации.')

        total_base = amount * data[base_ticker]
        return total_base
