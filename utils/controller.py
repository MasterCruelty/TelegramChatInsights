from pyrogram import Client
import utils_config
import modules.insights 
import utils.dbfunctions as udb
import utils.sysfunctions as usys
import utils.get_config as ugc



dictionary_super = {'/setchat'    : udb.set_chat,
                    '/delchat'    : udb.del_chat,
                    '/listchat'   : udb.list_chat,
                    '/allchat'    : udb.all_chat,
                    '/restart'    : usys.restart,
                    '/piechart'   : modules.insights.piechart}

"""
Super Admin fetch command and execute
"""
def fetch_super_command(match,query,client,message):
    try:
        return dictionary_super[match](client,message,query)
    except:
        return dictionary_super[match](client,message)

"""
Parsing messages
"""
def parser(message):
    temp = message.split(" ",1)
    try:
        result = temp[1]
    except:
        result = temp[0]
    return result


"""
	function which log messages
"""
config = ugc.get_config_file("config.json")
id_super_admin = config["id_super_admin"].split(";")[0]

@Client.on_message()
def visualizza(chat,nome_chat,utente,nome_utente,username,messaggio):
    result = "id utente: " + str(utente) + "\nnome utente: " + nome_utente + "\nusername: " + username
    print("id_utente: " + str(utente) + "\nnome_utente: " + nome_utente + "\nusername: " + username)
    if str(chat):
        result += "\nchat id: " + str(chat) + "\nnome chat: " + str(nome_chat) + "\nmessaggio: " + messaggio
        print("chat_id: " + str(chat) + "\nnome_chat: " + str(nome_chat))
        print("messaggio: " + messaggio)
        print("**************************************************************************************")
    client.send_message(id_super_admin,result)
