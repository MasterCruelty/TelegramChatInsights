import time
from pyrogram import Client 
from utils.controller import *
from utils.dbfunctions import *
from utils.get_config import get_config_file,get_username,get_text_message,get_chat,get_id_msg,get_id_user,get_first_name
from utils.sysfunctions import *

config = get_config_file("config.json")
api_id = config["api_id"]
api_hash = config["api_hash"]
session = config["session_name"]
comandi_super = config["commands"][0]
app = Client(session, api_id, api_hash)
print("The app is running...")

@app.on_message()
def print_updates(client,message):
    #getting info from incoming message
    chat = get_chat(message)
    id_messaggio = get_id_msg(message)
    utente = get_id_user(message)
    nome_chat = message.chat.title
    nome_utente = get_first_name(message)
    time_message = time.strftime("%H:%M:%S")
    file_id = "Nullo"
    username = get_username(message) 
    messaggio = get_text_message(message)

    #super admin detect commands
    cmd_super = comandi_super.split(";")
    match = messaggio.split(" ")
    if match[0] in cmd_super and isSuper(utente):
    #log incoming commands
        visualizza(chat,nome_chat,utente,nome_utente,username,messaggio,client)
        query = parser(messaggio)
        fetch_super_command(match[0],query,client,message)
        return

app.run()
