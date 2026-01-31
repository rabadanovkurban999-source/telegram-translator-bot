import telebot
from googletrans import Translator

TOKEN = "8499452535:AAHaZMeIvDySg9p0kGaU7w29X_oc3PtzZ8o"

bot = telebot.TeleBot(TOKEN)
translator = Translator()

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        translated = translator.translate(message.text, dest='ru')
        bot.reply_to(message, translated.text)
    except Exception as e:
        bot.reply_to(message, "Ошибка перевода")

bot.polling()
