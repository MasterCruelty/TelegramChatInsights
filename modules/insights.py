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
import datetime
import io
import tempfile
matplotlib.use('Agg')

#set matplotlib style
plt.style.use('fivethirtyeight')

"""
    Given a list of ids it returns total msg
"""
def count_all_msg(client,message,ids):
    result = []
    for i in range(len(ids)):
        result.append(usys.count_messages(client,message,ids[i]))
    return result

"""
    Return a leaderboard for saved chats
"""
def leadboard(client,message,query=""):
    check,all_msg,all_names = udb.fetch_chat_data()
    result = ""
    for i in range(len(all_msg)):
        result += str(i+1) + ". " + all_names[i] + ": " + str(all_msg[i]) + "\n"
    return sendMessage(client,message,result)

"""
    Plot piechart for personal chats
"""
def piechart(client,message,query):
    #fetch chat id/first name
    ids,first_names = udb.fetch_chat_info()
    check,all_msg,all_names = udb.fetch_chat_data()
    if check == True:
        message_counts = all_msg
        first_names = all_names
    else:
        message_counts = count_all_msg(client,message,ids)
    
    #prepare piechart as image in RAM
    plt.clf()
    temp = io.BytesIO()
    plt.figure(figsize=(20,15))

    #old palette: colours = [tuple(np.random.choice(range(256), size=3)/256) + (1,) for n in range(len(first_names))]
    
    #I prepare a palette of colours
    base_colors = ['#0033A0', '#0057D9', '#007BFF', '#60AFFF']
    colours = base_colors * ((len(first_names) // len(base_colors)) + 1)
    patches,texts, autotexts= plt.pie(message_counts,labels=first_names,colors = colours,autopct='%1.0f%%')

    #I populate labels with actual value if slice worth more than 2%
    total_messages = sum(message_counts)
    for label, count in zip(texts, message_counts):
        percentage = count / total_messages * 100
        if percentage >= 2:
            label.set_text(label.get_text() + f'\n{count}')

    #saving image in ram and sending
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
    # I get array of all id and first names of saved chats
    ids,first_names = udb.fetch_chat_info()
    # I gett array of all message count for every saved chat.
    message_counts = count_all_msg(client,message,ids)
    #get and save current message count for every chat in db
    for i in range(len(ids)):
        val = udb.update_chat_data(client,message,ids[i])
        if val == False:
            return sendMessage(client,message,"__At least 1 week between two records.__")
    if val == True:
        sendMessage(client,message,"__New check data executed today " + datetime.datetime.now().strftime('%d-%m-%Y'))
