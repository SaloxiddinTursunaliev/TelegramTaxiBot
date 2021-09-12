# -*- coding: utf-8 -*-

@bot.message_handler(commands=['setlang' , 'Setlang'])
def setlang_message(message):
    cur.execute('SELECT * from language where id = %s', [str(message.from_user.id)])
    record = cur.fetchall()
    for row in record:
        userid = row[0]
        userlang = row[1]
        
    if len(message.text.split()) < 2:
      bot.reply_to(message, "Please choose a language! En/Fa \nلطفا زبان مورد نظر خود را وارد کنید! فارسی/انگلیسی", parse_mode="Markdown")
      return
    if True:
      langz = message.text.replace("/setlang ","",1).replace("/Setlang ","",1)
    if langz == "en":
      cur.execute('INSERT INTO `language` (`id`, `language`) VALUES (%s, %s)', [str(message.from_user.id), "en"])
      db.commit()
      bot.send_message(message.chat.id, "Success!")
    elif langz == "fa":
      cur.execute('INSERT INTO `language` (`id`, `language`) VALUES (%s, %s)', [str(message.from_user.id), "fa"])
      db.commit()
      bot.send_message(message.chat.id, "انجام شد!")
    else:
      bot.reply_to(message, "Language not found \n زبان یافت نشد")
