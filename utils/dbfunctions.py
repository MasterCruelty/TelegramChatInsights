import sys
sys.path.append(sys.path[0] + "/..")
from utils.dbtables import *
from pyrogram import Client
from utils.get_config import *

#Inizio della connessione con il db
db.connect()


##WIP
#def function to save new id chat
#def function to delete id chat 
#def function to show saved chats



"""
questa funzione fa una select dalla tabella User e restituisce gli id di tutti gli utenti registratii dentro una lista di int
"""

def fetch_chat_info():
    result_id = []
    result_name = []
    result_message_count = []
    query = PersonalChats.select()
    for chat in query:
        result_id.append(chat.id_user)
        result_name.append(chat.first_name)
        result_message_count.append(chat.message_count)
    return result_id,result_name,result_message_count

"""
Questa funzione controlla se un certo utente Telegram è SuperAdmin
"""

def isSuper(id_utente):
    check = User.select().where((User.id_user == id_utente) 
    for superadmin in check:
        return True
    return False

#chiusura della connessione con il db
db.close()
