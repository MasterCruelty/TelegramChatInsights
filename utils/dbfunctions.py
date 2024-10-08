import sys
sys.path.append(sys.path[0] + "/..")
from utils.dbtables import *
from pyrogram import Client
from utils.get_config import *
import utils.sysfunctions as usys  
import datetime
import time

#Starting connection with db
db.connect()

"""
    This function save a new chat on db
"""
@Client.on_message()
def set_chat(client,message,query):
    json_user = client.get_users(query)
    userid = json_user.id
    name = json_user.first_name
    username_chat = "@" + str(json_user.username)
    chat = PersonalChats(id_chat = userid,first_name = name,username = username_chat)
    messages = usys.count_messages(client,message,userid)
    try:
        chat.save()
    except:
        return sendMessage(client,message,"Chat already saved!")
    query = PersonalChats.select().where(PersonalChats.id_chat == userid)
    for chat in query:
        result = "Chat " + str(PersonalChats.id_chat) + " saved!"
    return sendMessage(client,message,result)


#date = datetime.datetime.now().strftime('%d-%m-%Y')
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
    updated_messages = usys.count_messages(client,message,query)
    date = datetime.datetime.now().date()
    #select record for the id chat in function's argument. I take the most recent one to check timedelta then
    existing_record = DataChats.select().where(DataChats.id_chat == query).order_by(DataChats.date.desc()).first()
    try:
        delta = abs(date - existing_record.date.date()) 
    except AttributeError:
        chat_data = DataChats(id_chat = query,date = date,message_count= updated_messages)
        chat_data.save()
        return True
    #check timedelta at least 1 week between records
    if delta >= datetime.timedelta(weeks=1):
        chat_data = DataChats(id_chat = query,date = date,message_count= updated_messages)
        chat_data.save()
        return True
    else:
        return False

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
def list_chat(client,message,query=""):
    result = "List of saved chats:\n\n"
    query_sql = PersonalChats.select()
    for user in query_sql:
        result += str(user.id_chat) + ";" + str(user.first_name) + ";" + str(user.username) + "\n"
    return sendMessage(client,message,result)

"""
    Return total number of saved chats
"""
def all_chat(client,message,query=""):
    result = "Saved chats: "
    count = 0
    query_sql = PersonalChats.select()
    for user in query_sql:
        count += 1
    result +="__" + str(count) + "__"
    return sendMessage(client,message,result)

"""
    This function fetch all ids and first_names of saved chats
"""
def fetch_chat_info():
    result_id = []
    result_name = []
    query_sql = PersonalChats.select()
    for chat in query_sql:
        result_id.append(chat.id_chat)
        result_name.append(chat.first_name)
    return result_id,result_name

"""
    Return data about message counts from DataChats
"""
def fetch_chat_data():
    result_msg = []
    result_names = []
    check = False
    query_sql = (PersonalChats
                 .select(PersonalChats.first_name,DataChats.message_count)
                 .join(DataChats, on=(DataChats.id_chat == PersonalChats.id_chat))
                 .order_by(DataChats.message_count.desc())
                 .group_by(DataChats.id_chat)
                 .having(DataChats.date == fn.MAX(DataChats.date)))
    for item in query_sql:
        result_names.append(item.first_name)
        result_msg.append(item.datachats.message_count)
    if len(result_msg) <= 1:
        return check,result_msg,result_names
    else:
        check = True
        return check,result_msg,result_names

"""
    Return all data saved about a specific chat
"""
def fetch_chat_data_by_id(client,message,query):
    query_sql = (PersonalChats
                 .select(PersonalChats.first_name,DataChats.date,DataChats.message_count)
                 .join(DataChats, on=(DataChats.id_chat == PersonalChats.id_chat))
                 .where(PersonalChats.id_chat == query)
                 .order_by(DataChats.date.desc()))
    result = "Saved data for the requested chat:\n\n" 
    for item in query_sql:
        result += "__" + (item.datachats.date).strftime('%d-%m-%Y') + ":__ **" + str(item.datachats.message_count) + "**\n"
    return sendMessage(client,message,result)

        

"""
    check if the user is SuperAdmin
"""
def isSuper(id_utente):
    check = User.select().where((User.id_user == id_utente)) 
    for superadmin in check:
        return True
    return False

#chiusura della connessione con il db
db.close()
