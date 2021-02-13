import datetime
from datetime import time
import telebot


Token = '1177583422:AAFcAFbzKPgjQ358nJcHToTvM8wt2Ewrg3E'
bot = telebot.TeleBot(Token)  # Connect to Telegram


@bot.message_handler(content_types=['text'])
def _main(message):
    print(message.from_user)
    to = datetime.datetime.today()
    q = to.combine(to + datetime.timedelta(days=- to.weekday() + 2, weeks=1), time(15, 0))
    r = q - to
    other, mes = f'{(r.seconds // 60) // 60} ч, {r.seconds // 60 % 60} м. ', ''
    if r.days == 1:
        mes = f'Осталось: 1 день, {other}'
    elif r.days in [2, 3, 4]:
        mes = f'Осталось: {r.days} дня, {other}'
    else:
        mes = f'Осталось: {r.days} дней, {other}'
    bot.send_message(message.from_user.id, mes)


bot.polling(none_stop=True, interval=0, timeout=120)