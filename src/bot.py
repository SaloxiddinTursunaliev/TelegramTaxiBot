import datetime
import os
import telebot
import logging
import sys
import urllib
import re
import redis
import time as tm
import MySQLdb
import time

from shutil import copyfile
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

db = MySQLdb.connect(host="localhost",
user="root",
passwd="9963",
db="Eseyel",
charset='utf8',
use_unicode=True)
cur = db.cursor()

### CONFIG AND LOCALE CHECK
if not os.path.exists("config.py"):
  copyfile("config.py.new", "config.py")
if not os.path.exists("locale.py"):
  copyfile("locale.new.py", "locale.py")
  
# REDIS SERVER. IF ITS DIFFRENT, CONFIG IT!
#redisserver = redis.StrictRedis(host='localhost', port=6379, db=0)

try:
    reload(sys) # Python 2.7
except NameError:
    try:
        from importlib import reload  # Python 3.4+
    except ImportError:
        from imp import reload
    reload(sys)

sys.setdefaultencoding("utf-8")

execfile("locale.py")
execfile("config.py")
# execfile("locale.new.py")

############################################################################
# START OF CODES. DO NOT EDIT ANYTHING IF YOU DONT KNOW WHAT ARE YOU DOING!#
############################################################################

bot = telebot.TeleBot(TOKEN)
# LOGFILE
logfile = open("bot.log", "a")
time = datetime.datetime.now()
for plugin in enabled_plugins:
  try:
    execfile("plugins/" + plugin + ".py")
    print("Enabled plugin " + plugin)
  except:
    print("Error enabling " + plugin)
#    print Exception
logfile.write("Bot Started: " + str(time) + ". Enabled plugins:" + str(enabled_plugins) + ". ")
print("Bot started: " + str(time))
messanger_list = []
contacter_list = []
logger = telebot.logger
if DEEP_LOGGING:
  print("Debugging enabled.")
  logfile.write("Debugging enabled. \n")
  telebot.logger.setLevel(logging.DEBUG)
else:
  logfile.write("Debugging disabled. \n")
  print("Debugging disabled.")
#bot.set_update_listener(message_replier)
logfile.close()
bot.polling(none_stop=True, interval=0, timeout=3)
