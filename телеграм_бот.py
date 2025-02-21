import telebot

bot = telebot.TeleBot('7380336278:AAGqHmKiTXCQHZ9S9xVx1JTrsbLooYEaTCQ')

@bot.message_handler(commands=['start'])
def mai(message):
    bot.send_message(message.chat.id, f'Привет, {messange.from_user.first_name}')

@bot.message_handler(commands=['command2'])
def info2(message):
    bot.send_message(message.chat.id, f'Наташка - 14 февраля,  Инна - 12 июля/n')
bot.infinity_polling()

# @bot.message_handler()
# def info(messange):
#     if message.text.lower() == 'привет':
#         bot.send_message(messange.chat.id, f'Привет, {messange.from_user.first_name}')





