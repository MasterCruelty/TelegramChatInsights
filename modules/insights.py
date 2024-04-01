from pyrogram import Client
import time
import sys
sys.path.append(sys.path[0] + "/..")
from utils.get_config import *
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
    #get current message count for every chat

    #save record for every chat in db with current date

    #prepare piechart as image in RAM
    plt.clf()
    temp = io.BytesIO()
    plt.figure(figsize=(20,15))
    colours = [tuple(np.random.choice(range(256), size=3)/256) + (1,) for n in range(len(labels))]
    #plt.pie(values,labels=labels,colors=colours)
    plt.savefig(temp,format='png')
    temp.seek(0)
    image_file = temp
    #sendPhoto(client,message,image_file,'__Ecco il grafico a torta prodotto__')
    temp.close()
    image_file.close()
