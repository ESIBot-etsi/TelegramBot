import os
import telebot 

BOT_TOKEN = "6171205744:AAGo5xkoB5DJsejFUVYtfWRSekB5Mc8FtBc"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hola'])
def send_welcome(message):
    bot.reply_to(message, "¡Holi, espero que estes teniendo un buen día!")


bot.infinity_polling()