# -*- coding: utf-8 -*-

import requests

awaiting_audio = {"981": "hi"}

@bot.message_handler(commands=['mp3tag', 'Mp3tag'])
def mp3tag(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split("||")) < 2:
    bot.send_message(message.chat.id, language[userlang]["MP3TAG_NEA_MSG"], parse_mode="Markdown")
    return
  if awaiting_audio.has_key(str(userid)):
    bot.send_message(message.chat.id, language[userlang]["MP3TAG_SENDAUDIO_MSG"])
    return
  args = message.text.replace("/mp3tag","")
  dictargs = {str(userid): args}
  awaiting_audio.update(dictargs)
  bot.send_message(message.chat.id, language[userlang]["MP3TAG_SENDAUDIO_MSG"])
@bot.message_handler(content_types=['audio'])
def handle_docs_audio(message):
  if awaiting_audio.has_key(str(message.from_user.id)):
    bot.send_chat_action(message.chat.id, "upload_document")
    tm.sleep(2)
    fileid = message.audio.file_id
    fileargs = awaiting_audio[str(message.from_user.id)].split("||")
    file_info = bot.get_file(fileid)
    file = urllib.urlretrieve('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path), 'music.mp3')
    bot.send_audio(message.chat.id, open('music.mp3', 'rb'), duration=message.audio.duration, performer=fileargs[0], title=fileargs[1])
    bot.send_message(message.chat.id, file_info.file_path)
    cur.execute('INSERT INTO `fileid` (`id`) VALUES (%s)', [fileid])
    db.commit()
    file_url1 = 'https://api.telegram.org/file/bot1129139030:AAGSofcul85yI9d5DyAtBG_vR-AVS9dZY6s/music/file_17.m4a'
    bot.send_audio(message.chat.id, audio=file_url1)
    del awaiting_audio[str(message.from_user.id)]
#

#@bot.message_handler(content_types=['photo'])
#def photo(message):
#    file_id = message.photo[-1].file_id
#    file = bot.get_file(file_id)
#    file_path = file.file_path
#    file_url = 'https://api.telegram.org/file/bot1129139030:AAGSofcul85yI9d5DyAtBG_vR-AVS9dZY6s/{file_path}'
#    print(file_id)
    '''
    bot.send_message(message.chat.id, "description")
    @bot.message_handler(content_types=['text'])
    def send_text_description(message):
        description = message.text
    '''
#    bot.send_message(message.chat.id, "What is it's price?")
#    @bot.message_handler(content_types=['text'])
#    def send_text_price(message):
#        price = message.text
#        print(price)
#        cur.execute('INSERT INTO `file_info` (`price`, `fileid`) VALUES (%s, %s)', [price, file_id])
#        db.commit()

@bot.message_handler(content_types=['photo'])
def photo(message):
    file_id = message.photo[-1].file_id
    file = bot.get_file(file_id)
    file_path = file.file_path
    file_url = 'https://api.telegram.org/file/bot1129139030:AAGSofcul85yI9d5DyAtBG_vR-AVS9dZY6s/{file_path}'
    print(file_id)
    '''
    bot.send_message(message.chat.id, "description")
    @bot.message_handler(content_types=['text'])
    def send_text_description(message):
        description = message.text
    '''
    bot.send_message(message.chat.id, "What is it's price?")
    price = 12
    cur.execute('INSERT INTO `file_info` (`price`, `fileid`) VALUES (%s, %s)', [price, file_id])
    db.commit()
