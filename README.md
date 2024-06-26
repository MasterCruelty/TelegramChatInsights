![License](https://img.shields.io/github/license/MasterCruelty/telegramchatinsights)
[![image](https://img.shields.io/github/stars/MasterCruelty/telegramchatinsights)](https://github.com/MasterCruelty/telegramchatinsights/stargazers)
[![image](https://img.shields.io/github/forks/MasterCruelty/telegramchatinsights)](https://github.com/MasterCruelty/telegramchatinsights/network/members)
![CodeSize](https://img.shields.io/github/languages/code-size/MasterCruelty/telegramchatinsights)
[![image](https://img.shields.io/github/issues/MasterCruelty/telegramchatinsights)](https://github.com/MasterCruelty/telegramchatinsights/issues)
![image](https://img.shields.io/github/languages/top/MasterCruelty/telegramchatinsights)
![image](https://img.shields.io/github/commit-activity/w/MasterCruelty/telegramchatinsights)
![image](https://img.shields.io/github/contributors/MasterCruelty/telegramchatinsights)

# Telegram Chat Insights

# What is it
This project is about a Telegram app made by creating a userbot based on Pyrogram.<br>
The main feature is to show your data about personal chat by plotting charts. It's still in development and more features could be implemented.

### Contribute
Feel free to contribute and improve the project. You can read the guidelines to contribute [here](https://github.com/MasterCruelty/TelegramChatInsights/blob/main/CONTRIBUTING.md)

# How to setup

The correct way to setup this bot is to compile the file  ```config.json```. So it's necessary to have these data:

* Telegram api keys: ```api_id``` e ```api_hash```. You can generate them [here](https://my.telegram.org/apps)
* Telegram data of the owner of the bot: ```id_super_admin```.
* The path where is the .db file: ```path_db```.
* The session name: ```session_name```.
* Name of super admin commands: ```super_admin_commands```.

Name of commands to put inside ```config.json``` can be copied from source code or renamed inside source code and then copied in json file.	

### How the userbot's commands works

The features of the commands are explained inside ```help.json```. It is the file which is used by the userbot to reply at ```/help <command name>```.

### How the admin/super commands works

* register a new chat: ```/setchat``` <id_user>
* delete a chat: ```/delchat``` <id_user>
* How to list all user registered: ```/listchat``` 
* How to show ho many chats are registered: ```/allchat```
* How to get all saved data about a specific chat: ```/getchatdata``` <id_chat> 
* How to update a record value of a chat: ```/updatechat``` <id_chat> <new_value> <old_value>
* check if the bot is online: ```/ping```

### Example of execution
This is an example of piechart plotted. It shows the weight of every chat saved.
![image](https://github.com/MasterCruelty/TelegramChatInsights/assets/72561502/1b833ebb-6a47-4a92-8d25-bb994475348c)

### How data is collected
There's a dedicated command to do that: ```/newcheck``` <br>
By launching it, it starts calculating all the amount of messages for every saved chat using Telegram API and save those data with the current date.<br>
The next time you decide to launch this command, you can view the difference between the last check and the new one.<br>
At the moment this command is launched manually by the user, thought initially as userbot not running 24/7.<br>
In the near future it could be instead an automatic check made daily or weekly and then a 24/7 running app.


### Dependencies

* Pyrogram
* peewee
* tempfile
* matplotlib
* numpy

### External projects used

* [Pyrogram](https://github.com/pyrogram/pyrogram)
* [Peewee](https://github.com/coleifer/peewee)

