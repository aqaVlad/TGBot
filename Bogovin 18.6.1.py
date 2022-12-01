# QapQapBot
import telebot
import requests
from Bogovin_config import keys, currency, TOKEN
from Bogovin_extensions import APIException, CryptoConverter


bot = telebot.TeleBot(TOKEN)
# или bot = telebot.TeleBot(5824382331:AAF87B5cT-PF3JemEdAK08Dx-xgluSJg_M8)



@bot.message_handler(commands=['start', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Приветствую, @{message.chat.username}! Давно не виделись")
    bot.send_message(message.chat.id, f"{message.chat.username}, нажми на /help и узнаешь, что я могу!")

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Я могу конвертировать валюты в режиме реального времени.\
\n\nЧтобы начать работу, введите команду в следующем формате: \n<имя валюты, которую конвертируем> \
<имя валюты, в которую переводим> \
<количество переводимой валюты (числом)>. \n\nУвидеть список всех доступных валют можно тут===>>> /values'
    print(message.text)
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currency.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    text = message.text.lower()

    try:
        values = text.split(' ')

        if len(values) != 3:
            raise APIException('Какие-то непонятные мне параметры...\nПопробуй еще раз.')

        base, quote, amount = values
        total_sum = CryptoConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base} в {quote} - {total_sum}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)


