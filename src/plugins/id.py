@bot.message_handler(commands=['id', 'Id'])
def send_id(message):
  cur.execute('SELECT * from language where id = %s', [str(message.from_user.id)])
  record = cur.fetchall()
  for row in record:
      userid = row[0]
      userlang = row[1]
  username = message.from_user.first_name.encode("utf-8")
  userid = message.from_user.id
  reply_msg = language[userlang]["ID_MSG"]
  gpid = message.chat.id
  if message.chat.type == "supergroup" or message.chat.type == "group": 
    reply_msg = reply_msg + language[userlang]["INGP_ID_MSG"]
  if message.reply_to_message:
    repliedid = message.reply_to_message.from_user.id
    reply_msg = reply_msg + language[userlang]["REPLIED_ID_MSG"].format(repliedid)
    if message.reply_to_message.forward_from:
      reply_msg = reply_msg + language[userlang]["FORWARDED_ID_MSG"].format(message.reply_to_message.forward_from.id)
      try:
        reply_msg = reply_msg + language[userlang]["CHATID_ID_MSG"].format(message.reply_to_message.forward_from_chat.id)
      except:
        pass
  bot.reply_to(message, reply_msg.format(username, userid, gpid), parse_mode="Markdown")
