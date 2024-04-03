import sys
sys.path.append(sys.path[0] + "/..")
from utils.dbtables import *
from pyrogram import Client
from utils.get_config import *
from utils.sysfunctions as usys import count_messages 

#Inizio della connessione con il db
db.connect()


@Client.on_message()
def set_chat(client,message,query):
    json_user = client.get_users(query)
    userid = json_user.id
    name = json_user.first_name
    username_chat = "@" + str(json_user.username)
    chat = PersonalChats(id_chat = userid,first_name = name,username = username_chat)
    messages = count_messages(client,message,userid)
    chat_data = DataChats(id_chat = userid, Date = datetime.datetime.now(), message_count = messages)  
    try:
        chat.save()
    except:
        return sendMessage(client,message,"Chat already saved!")
    query = PersonalChats.select().where(PersonalChats.id_chat == userid)
    for chat in query:
        result = "Chat " + str(PersonalChats.id_chat) + " saved!"
    return sendMessage(client,message,result)

"""
    Delete a personal chat from db
""" 
def del_chat(client,message,query):
    json_user = client.get_users(query)
    userid = json_user.id
    query = PersonalChats.delete().where(PersonalChats.id_chat == userid).execute()
    query2 = DataChats.delete().where(DataChats.id_chat == userid).execute()
    result = "__Chat " + str(userid) + " deleted.__"
    return sendMessage(client,message,result)

"""
    Update of message count for a specific saved chat by insert a new record in db
"""
def update_chat_data(client,message,query):
    updated_messages = count_messages(client,message,query)
    chat_data = DataChats(id_chat = query,Date = datetime.datetime.now(),message_count= updated_messages)
    chat_data.save()

"""
    Manually force update of message count for a specific chat
""" 
def force_update_chat_data(client,message,query):
    splitted = query.split(" ")
    userid = int(splitted[0])
    msg_count = splitted[1]
    old_msg_count = splitted[2]
    (DataChats
     .update({DataChats.message_count : msg_count})
     .where((DataChats.id_chat == userid) &
            (DataChats.message_count == old_msg_count))).execute()
     return sendMessage(client,message,"__Updated message count for " + str(userid) +"__")

"""
    Return list of all saved chats (id,name,username)
""" 
def list_chat(client,message):
    result = "List of saved chats:\n\n"
    query = PersonalChats.select()
    for user in query:
        result += str(PersonalChats.id_chat) + ";" + PersonalChats.first_name + ";" + PersonalChats.username + "\n"
    return sendMessage(client,message,result)

"""
    Return total number of saved chats
"""
def all_chat(client,message):
    result = "Saved chats: "
    count = 0
    query = PersonalChats.select()
    for user in query:
        count += 1
    result +="__" + str(count) + "__"
    return sendMessage(client,message,result)
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
