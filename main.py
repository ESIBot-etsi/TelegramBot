import telebot 
import json
import datetime
import random

BOT_TOKEN = "6171205744:AAGo5xkoB5DJsejFUVYtfWRSekB5Mc8FtBc"

bot = telebot.TeleBot(BOT_TOKEN)

variables = {
    'key_holder': "Luis",
    'key_time' : "Tiempo",
    'key_hour' : "Hora",
    'Presidente': "Luis",
    'Telematica': "Mario"
}

def save_to_json(variables, filename):
    with open(filename, 'w') as archivo:
        json.dump(variables, archivo)

def get_from_json(filename):
    try:
        with open(filename, 'r') as archivo:
            variables = json.load(archivo)
            return variables
    except FileNotFoundError:
        # En caso de que el archivo no exista, retornar None o manejarlo de alguna otra forma
        return None

diccionario_cargos = {
        'Presidente' : "Luis", 
        'Telemática' : "Mario",
        'Secretario' : "César", 
        'RRPP' : "Natalia",
        'Vicepresidente' : "Natalia",
        'Tesorero' : "Miguel Ángel",
        'R2D2' : "BUBIBU"
    }
variables = get_from_json("variables.json")
with open('palabrotas.txt', 'r', encoding='utf-8') as archivo:
        palabras_clave = archivo.read().splitlines()
palabras_muy_clave = ['Alvaro', 'alvaro', 'alvarito', 'juanmanue', 'Alvarito', 'Juanmanue', 'Pagina Web', 'Web', 'web', 'pagina web', 'Álvaro', 'álvaro']
frases_aleatorias = ['¿Hablas de Alvarito, la layenda que salvó esibot innumerables veces?',
                    'Aun recuerdo cuando Alvarito salvó a mi perro de ser atropellado por una vespa',
                    'Amo a Alvarito',
                    'No se que sería de nosotros sin Alvarito', 
                    'Puede que sepas programar paginas web, pero bueno, todos podemos soñar al menos con ser la mitad de buenos que Alvaro',
                    'Solo escuchar su nombre hace que mis ficheros .css tiemblen']

@bot.message_handler(commands=['llave!'])
def new_key(message):
    bot.reply_to(message, f"{message.from_user.first_name} tiene las llaves")
    variables['keys_holder']=message.from_user.first_name
    variables['key_day']=datetime.datetime.now().strftime("%d/%m/%Y")
    variables['key_hour']=datetime.datetime.now().strftime("%H:%M:%S")
    save_to_json(variables, "variables.json")
    
@bot.message_handler(commands=['add'])
def addTarea(message):
    quehaceres = get_from_json("quehaceres.json")
    tarea = message.text.replace('/add ', '')
    quehaceres.append(tarea)
    save_to_json(quehaceres, "quehaceres.json")
    
@bot.message_handler(commands=['tareas'])
def showTarea(message):
    chat_id = message.chat.id
    quehaceres = get_from_json("quehaceres.json")
    mensaje = ""
    j=1
    for i in quehaceres:
        mensaje +=str(j) + " " + i +"\n"
        j+=1
    bot.send_message(chat_id, mensaje)

@bot.message_handler(commands=['remove'])
def removeTarea(message):
    chat_id = message.chat.id
    quehaceres = get_from_json("quehaceres.json")
    tarea = int(message.text.replace('/remove ', ''))
    del quehaceres[tarea-1]
    save_to_json(quehaceres, "quehaceres.json")
    showTarea(message)

@bot.message_handler(commands=['start', 'hola'])
def send_welcome(message):
    with open('saludos.txt', 'r', encoding='utf-8') as archivo:
        saludo = archivo.read().splitlines()
    bot.reply_to(message, random.choice(saludo))
    

@bot.message_handler(commands=['llave?'])
def actual_key_holder(message):
    variables = get_from_json("variables.json")
    bot.reply_to(message, "Las llaves las tiene " + variables['keys_holder'] + " desde las " + variables['key_hour'])

@bot.message_handler(commands=['llavent'])
def no_key(message):
    variables = get_from_json("variables.json")
    bot.reply_to(message, f"{variables['keys_holder']} ha dejado la llave")
    variables['keys_holder']="Consergería"
    variables['key_day']=datetime.datetime.now().strftime("%d/%m/%Y")
    variables['key_hour']=datetime.datetime.now().strftime("%H:%M:%S")
    save_to_json(variables, "variables.json")

@bot.message_handler(commands=['administracion'])
def imprimir_cargo(message):
    chat_id = message.chat.id
    
    comando = message.text.split()
    
    if len(comando) > 1:
        cargo = comando[1]
        
        if cargo in diccionario_cargos:
            nombre = diccionario_cargos[cargo]
            mensaje = f'{cargo}: {nombre}'
            bot.send_message(chat_id, mensaje)
        else:
            bot.send_message(chat_id, f'El cargo "{cargo}" no se encontró.')
    else:
        for cargo, nombre in diccionario_cargos.items():
            mensaje = f'{cargo}: {nombre}'
            bot.send_message(chat_id, mensaje)

@bot.message_handler(func=lambda message: any(palabra in message.text.lower() for palabra in palabras_clave))
def palabrotas(message):
    bot.reply_to(message, 'Has dicho una palabra que puede resultar ofensiva para ciertas personas, por favor modere su lenguaje <3')

@bot.message_handler(func=lambda message: any(palabra in message.text.lower() for palabra in palabras_muy_clave))
def send_message(message):
    chat_id = message.chat.id
    frase = random.choice(frases_aleatorias)
    bot.reply_to(message, frase)

@bot.message_handler(commands=['comandos', 'help'])
def imprimir_ccomandos(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, """Comandos: 
    -/llave! : registra quien y cuando se coje la llave del taller
    -/llave? : muestra por el chat quien tiene la llave y desde cuando
    -/llavent : registra que la llave ha sido dejada en el taller
    -/administracion: muestra por pantalla los cargos de la administracion, tambien se puede filtrar por cargos específicos. Un ejemplo sería :'/administracion Presidente'""")

@bot.message_handler(commands='reunion!')
def nueva_reunion(message):
    chat_id = message.chat.id
    texto = message.text[6:].strip()  # Obtener el texto después del comando "/webo" y eliminar espacios en blanco al principio y al final
    palabras = texto.split()  # Dividir el texto en palabras
    
    if len(palabras) >= 2:
        motivo = palabras[0]
        dia = palabras[1]
        reuniones={
            motivo:dia
        }
        save_to_json(reuniones, "reuniones.json")
        
    else:
        bot.send_message(chat_id, "Has introducido mal el formato")

@bot.message_handler(commands='reuniones?')
def muestra_reuniones(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBJX9fZ3Z3Z3Z3Z3Z3Z3Z3Z3Z3Z3Z3Z3ZAAK6AQACXZQlVU2Z1Z1ZIwQ')
    
bot.infinity_polling()
