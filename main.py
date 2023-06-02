import os
import telebot 
import json
import datetime

BOT_TOKEN = "6171205744:AAGo5xkoB5DJsejFUVYtfWRSekB5Mc8FtBc"

bot = telebot.TeleBot(BOT_TOKEN)

variables = {
    'key_holder': "Luis",
    'key_time' : "Tiempo",
    'key_hour' : "Hora",
    'Presidente': "Luis",
    'Telematica': "Mario"
}

def save_to_json(variables):
    with open('variables.json', 'w') as archivo:
        json.dump(variables, archivo)

def get_from_json():
    try:
        with open('variables.json', 'r') as archivo:
            variables = json.load(archivo)
            return variables
    except FileNotFoundError:
        # En caso de que el archivo no exista, retornar None o manejarlo de alguna otra forma
        return None


variables = get_from_json()

@bot.message_handler(commands=['newkey'])
def new_key(message):
    # Obtener el texto después de '/newKey'
    #keys_holder = message.text.split('/newKey', 1)[1].strip()
    bot.reply_to(message, f"Se ha establecido la nueva clave: {message.from_user.first_name}")
    variables['keys_holder']=message.from_user.first_name
    variables['key_day']=datetime.datetime.now().strftime("%d/%m/%Y")
    variables['key_hour']=datetime.datetime.now().strftime("%H:%M:%S")
    save_to_json(variables)
    

@bot.message_handler(commands=['start', 'hola'])
def send_welcome(message):
    bot.reply_to(message, "¡Holi, espero que estes teniendo un buen día!")

    
@bot.message_handler(commands=['llaves'])
def actual_key_holder(message):
    variables = get_from_json()
    bot.reply_to(message, "Las llaves las tiene " + variables['keys_holder'] + " el día " + variables['key_day'] + " a las " + variables['key_hour'])




bot.infinity_polling()