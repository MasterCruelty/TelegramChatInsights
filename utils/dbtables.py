from peewee import *
import sys
sys.path.append(sys.path[0] + "/..")
from utils.get_config import get_config_file

config = get_config_file("config.json")
id_super_admin = config["id_super_admin"].split(";")
path_db = config["path_db"]

global db
db = SqliteDatabase(path_db)

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id_user = IntegerField(unique = True)
    name = CharField()
    username = CharField()

class PersonalChats(BaseModel):
    id_chat = IntegerField(unique = True)
    first_name = CharField()
    username = CharField()
    date = DateTimeField()
    message_count = IntegerField()

db.connect()
db.create_tables([User])

#inizializzo il valore di stopmsg a valore di default False
stop = Stopmsg(value = False)
stop.save()
#Inizializzo il super admin da file di configurazione
overlord = User(id_user = id_super_admin[0], name = id_super_admin[1], username = id_super_admin[2])
try:
    overlord.save()
except:
    db.close()
db.close()
