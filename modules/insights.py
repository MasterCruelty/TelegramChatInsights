from pyrogram import Client
import time
import sys
sys.path.append(sys.path[0] + "/..")
from utils.get_config import *
import utils.dbfunctions as udb
import utils.sysfunctions as usys
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import io
import tempfile
matplotlib.use('Agg')

#set matplotlib style
plt.style.use('fivethirtyeight')


def count_all_msg(client,message,ids):
    result = []
    for i in range(len(ids)):
        result.append(usys.count_messages(client,message,ids[i]))
    return result

"""
    Plot piechart for personal chats
"""
def piechart(client,message,query):
    #fetch chat id/first name
    ids,first_names = udb.fetch_chat_info()
    message_counts = count_all_msg(client,message,ids)
    
    #prepare piechart as image in RAM
    plt.clf()
    temp = io.BytesIO()
    plt.figure(figsize=(20,15))
    colours = [tuple(np.random.choice(range(256), size=3)/256) + (1,) for n in range(len(first_names))]
    plt.pie(message_counts,labels=first_names,colors = colours)
    plt.savefig(temp,format='png')
    temp.seek(0)
    image_file = temp
    sendPhoto(client,message,image_file,'__Here a piechart of your personal chats.__')
    temp.close()
    image_file.close()

"""
    Update data on db about Personal Chats 
"""
def new_check_data(client,message,query):
    ids,first_names = udb.fetch_chat_info()
    message_counts = count_all_msg(client,message,ids)
    #get and save current message count for every chat in db
    for i in range(len(ids)):
        udb.update_chat_data(client,message,ids[i])
    sendMessage(client,message,"__Nuova analisi eseguita in data " + datetime.datetime.now().strftime('%d-%m-%Y'))
