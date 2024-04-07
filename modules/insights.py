from pyrogram import Client
import time
import sys
sys.path.append(sys.path[0] + "/..")
from utils.get_config import *
import utils.dbfunctions as udb
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import io
import tempfile
matplotlib.use('Agg')

#set matplotlib style
plt.style.use('fivethirtyeight')

"""
    Plot piechart for personal chats
"""
def piechart(client,message,query):
    #fetch chat id/first name
    ids,first_names,message_counts = udb.fetch_chat_info()
    
    #get and save current message count for every chat in db
    for i in range(len(ids)):
        udb.update_chat_data(client,message,ids[i])
    
    #prepare piechart as image in RAM
    plt.clf()
    temp = io.BytesIO()
    plt.figure(figsize=(20,15))
    colours = [tuple(np.random.choice(range(256), size=3)/256) + (1,) for n in range(len(ids))]
    plt.pie(message_counts,labels=first_name,colors=colours)
    plt.savefig(temp,format='png')
    temp.seek(0)
    image_file = temp
    sendPhoto(client,message,image_file,'__Here a piechart of your personal chats.__')
    temp.close()
    image_file.close()
