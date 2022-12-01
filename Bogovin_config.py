TOKEN = "5824382331:AAF87B5cT-PF3JemEdAK08Dx-xgluSJg_M8"

# Словарь валют представлен 2 вариантами: на вывод валют для пользователя и на обработку без вывода
# 1
currency = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB',
    'фунт': 'GBP',
    'юань': 'CNY',
    'иена': 'JPY',
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'лайткоин': 'LTC',
}

# 2
# Решение не самое удачное, поскольку в выводе результатов показывает именно то, как вводился запрос
keys = {
    'доллар': 'USD',
    'usd': 'USD',
    'dollar': 'USD',
    'евро': 'EUR',
    'euro': 'EUR',
    'eur': 'EUR',
    'evro': 'EUR',
    'рубль': 'RUB',
    'руб': 'RUB',
    'rouble': 'RUB',
    'rub': 'RUB',
    'фунт': 'GBP',
    'gbp': 'GBP',
    'pound': 'GBP',
    'юань': 'CNY',
    'cny': 'CNY',
    'yuan': 'CNY',
    'иена': 'JPY',
    'jpy': 'JPY',
    'йена': 'JPY',
    'yen': 'JPY',
    'биткоин': 'BTC',
    'btc': 'BTC',
    'bitcoin': 'BTC',
    'эфириум': 'ETH',
    'eth': 'ETH',
    'ethereum': 'ETH',
    'лайткоин': 'LTC',
    'ltc': 'LTC',
    'litecoin': 'LTC',
}