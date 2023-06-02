import os
import telebot 
import json
import datetime

BOT_TOKEN = "6171205744:AAGo5xkoB5DJsejFUVYtfWRSekB5Mc8FtBc"

bot = telebot.TeleBot(BOT_TOKEN)

variables = {
    'key_holder': "Luis",
    'key_time' : "Tiempo",
    'key_hour' : "Hora"
}

administracion = {
    'Presidente' : "Luis", 
    'Telemática' : "Mario",
    'Secretario' : "César", 
    'RRPP' : "Natalia",
    'Vicepresidente' : "Natalia",
    'Tesorero' : "Miguel Ángel",
    'R2D2' : "BUBIBU"
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


@bot.message_handler(commands=['llave!'])
def new_key(message):
    bot.reply_to(message, f"Se ha establecido la nueva clave: {message.from_user.first_name}")
    variables['keys_holder']=message.from_user.first_name
    variables['key_day']=datetime.datetime.now().strftime("%d/%m/%Y")
    variables['key_hour']=datetime.datetime.now().strftime("%H:%M:%S")
    save_to_json(variables)

@bot.message_handler(commands=['llavent'])
def no_key(message):
    variables = get_from_json()
    bot.reply_to(message, f"{variables['keys_holder']} ha dejado la llave")
    variables['keys_holder']="Consergería"
    variables['key_day']=datetime.datetime.now().strftime("%d/%m/%Y")
    variables['key_hour']=datetime.datetime.now().strftime("%H:%M:%S")
    save_to_json(variables)

@bot.message_handler(commands=['llave?'])
def actual_key_holder(message):
    variables = get_from_json()
    bot.reply_to(message, "Las llaves las tiene " + variables['keys_holder'] + " el día " + variables['key_day'] + " a las " + variables['key_hour'])




bot.infinity_polling()