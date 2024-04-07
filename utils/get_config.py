import utils_config
from pyrogram import Client

"""
Load configuration file
"""
def get_config_file(json_file):
    config = utils_config.load_config(json_file)
    return utils_config.serialize_config(config)

"""
Support function to send message 
"""
@Client.on_message()
def sendMessage(client,message,result):
    client.send_message(get_chat(message),result,disable_web_page_preview=True,reply_to_message_id=get_id_msg(message))
    return

"""
Support function to send images
"""
@Client.on_message()
def sendPhoto(client,message,result,caption):
    client.send_photo(get_chat(message),result,caption=caption,reply_to_message_id=get_id_msg(message))

"""
Return user id
"""
def get_id_user(message):
    try:
        return message.from_user.id
    except:
        return "user is not found"
"""
Return current id chat
"""
def get_chat(message):
    return message.chat.id

"""
Return first name of the message
"""
def get_first_name(message):
    try:
        return message.from_user.first_name
    except:
        return "first name not found"
"""
Return username of the message
"""
def get_username(message):
    try:
        return "@" + message.from_user.username
    except:
        return "Not set username"

"""
Return text message
"""
def get_text_message(message):
    if message.text is None:
        return "Media file"
    else:
        return message.text
"""
Return id message
"""
def get_id_msg(message):
    return message.id
