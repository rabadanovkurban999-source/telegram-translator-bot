import telebot
from googletrans import Translator

TOKEN = "8499.....Z8o"

bot = telebot.TeleBot(TOKEN)
translator = Translator()

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        translated = translator.translate(message.text, dest='ru')
        bot.reply_to(message, translated.text)
    except:
        bot.reply_to(message, "Ошибка перевода")

bot.polling()
