from pyrogram import Client,errors
import utils.controller as uct
import utils.get_config as ugc
import utils.dbfunctions as udb
import random
import time
import os
import datetime


"""
Return messages count total of the current chat
"""
@Client.on_message()
def count_messages(client,message,query):
    totmsg = client.search_messages_count(query)
    return totmsg

def get_date_only():
    return datetime.datetime.now().date()

"""
Return on message the id of the current chat
"""
@Client.on_message()
def id_chat(client,message):
    chat_id = message.chat.id
    return ugc.sendMessage(client,message,chat_id)

"""
Return the user id of the replied message 
"""
def get_id(client,message):
    content = message.reply_to_message.from_user
    result = content.id
    return ugc.sendMessage(client,message,result)

"""
Return json of the user requested
"""
@Client.on_message()
def get_user(client,message,query):
    info_user = client.get_users(query)
    return ugc.sendMessage(client,message,info_user)


"""
check if the app is online
"""
def ping(client,message):
    return ugc.sendMessage(client,message,"pong __TelegramChatInsights is online__")

"""
Restarting app
"""
def restart(client,message):
    ugc.sendMessage(client,message,"__Restarting...\n\nI'll be back in ten seconds.__")
    os.execl(sys.executable,sys.executable,*sys.argv)

"""
documentation of commands directly in Telegram
"""
def help(client,message,query):
    help_file = ugc.get_config_file("help.json")
    if query in help_file:
        help_request = help_file[query][0:]
        help_request = str(help_request).replace("(","").replace(")","").replace('"','').replace(r'\n','\n')
        return ugc.sendMessage(client,message,help_request)
    elif (query not in help_file):
        help_request = "__**Command not found**__\n\n"
        help_request += help_file["default"]
        return ugc.sendMessage(client,message,help_request)
    else:
        help_request = help_file["default"]
        return ugc.sendMessage(client,message,help_request)
