# -*- coding: utf-8 -*-
import time
from datetime import datetime

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  cur.execute('SELECT * from language where id = %s', [str(call.from_user.id)])
  record = cur.fetchall()
  for row in record:
      userid = row[0]
      userlang = row[1]
  if call.message:
    
    ###################
    #  USER SIDE
    ###################
    
    if call.data == "Startstopsms":
        
      msgid = call.inline_message_id
      
      def startsms(call):
          
          cur.execute('SELECT id from bot_test')
          record = cur.fetchall()
          for row in record:
              testid = row[0]
              
          test_id = testid
          
          if test_id == "1":
              
              cur.execute('UPDATE bot_test SET id=%s where id=%s', [0, 1])
              db.commit()
             
          if test_id == "0":
              cur.execute('UPDATE bot_test SET id=%s where id=%s', [1, 0])
              db.commit()
                  
              for y in range(1, 99999):
                  y = y
                  cur.execute('SELECT * from bot_test')
                  record223 = cur.fetchall()
                  for row223 in record223:
                      testid223 = row223[0]
                          
                  test_id223 = testid223
                  
                  if test_id223 == "1":
                      
                      for x in range(1, 99999):
                          
                          cur.execute('SELECT * from bot_test')
                          record224 = cur.fetchall()
                          for row224 in record224:
                              testid224 = row224[0]
                          
                          test_id224 = testid224
                      
                          if test_id224 == "0":
                              break
                      
                          else:
                              x = 99999 - x
                              z = str(y) + " - " + str(x)
                              bot.send_message(1012254767, z)
                              time.sleep(40)
          
                  else:
                      break
                  
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Finished", parse_mode="Markdown", reply_markup=startsms(call))

    
    if call.data == "help":
      msgid = call.inline_message_id
      markup = types.InlineKeyboardMarkup()
      markup.row_width = 1
      #markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
      markupij = types.InlineKeyboardButton("🏠", callback_data='main')
      markup.add(markupij)
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Help_message_user"], parse_mode="Markdown", reply_markup=markup)
      #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Here you are!")
      
    if call.data == "main":
      msgid = call.inline_message_id
      markup = types.InlineKeyboardMarkup()
      markup.row_width = 1
      cur.execute('SELECT * from main_menu where language=%s and status=%s', [userlang, 1])
      record13 = cur.fetchall()
      for row13 in record13:
          markup1 = types.InlineKeyboardButton(row13[0], callback_data = row13[0])
          markup.add(markup1)
            
      markup.row_width = 3
      markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
      markupij = types.InlineKeyboardButton("❔", callback_data='help')
      markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
      markup.add(markupii, markupij, markupik)
      
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Main_user"], parse_mode="Markdown", reply_markup=markup)
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
      
    if call.data == "settingsmain":
      markup = types.InlineKeyboardMarkup()
      markupib = types.InlineKeyboardButton("Til - Язык", callback_data='settingslang')
      markupic = types.InlineKeyboardButton("🏠", callback_data='main')
      markup.add(markupib,markupic)
      msgid = call.inline_message_id
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Settings_user"], parse_mode="Markdown", reply_markup=markup)
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
      
    if call.data == "settingslang":
      msgid = call.inline_message_id
      markup = types.InlineKeyboardMarkup()
      markup.row_width = 1
      cur.execute('SELECT * from language_list where status=%s', [1])
      recordlanglist = cur.fetchall()
      for rowlanglist in recordlanglist:
          markup1 = types.InlineKeyboardButton(rowlanglist[0], callback_data = rowlanglist[1])
          markup.add(markup1)
          
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Tilni tanlang!🇺🇿\nВыберите язык!🇷🇺", parse_mode="Markdown", reply_markup=markup)
      
    cur.execute('SELECT * from language_list')
    recordlanglistset = cur.fetchall()
    for rowlanglistset in recordlanglistset:
        if call.data == rowlanglistset[1]:
            cur.execute('DELETE FROM `language` WHERE id=%s', [str(call.from_user.id)])
            cur.execute('INSERT INTO `language` (`id`, `language`) VALUES (%s, %s)', [str(call.from_user.id), rowlanglistset[1]])
            db.commit()
            msgid = call.inline_message_id
            
            cur.execute('SELECT id from user_registration_info where id = %s', [str(call.from_user.id)])
            recorduserreg = cur.fetchall()
            if not recorduserreg:
                
                cur.execute('SELECT language from language where id = %s', [str(call.from_user.id)])
                record = cur.fetchall()
                for row in record:
                    userlang = row[0]
                    
                markup = types.InlineKeyboardMarkup()
                markup.row_width = 1
                cur.execute('SELECT * from province_address where language=%s and status=%s', [userlang, 1])
                record13 = cur.fetchall()
                for row13 in record13:
                    markup1 = types.InlineKeyboardButton(row13[0], callback_data = row13[0])
                    markup.add(markup1)
                
                markup.row_width = 3
                markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
                markupij = types.InlineKeyboardButton("❔", callback_data='help')
                markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
                markup.add(markupii, markupij, markupik)
                
                bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Assalomu_alaykum_user"], reply_markup=markup, parse_mode="Markdown")
            
            for rowuserreg in recorduserreg:
                user_reg_id = rowuserreg[0]
                    
                markup = types.InlineKeyboardMarkup()
                markup.row_width = 1
                cur.execute('SELECT * from main_menu where language=%s and status=%s', [rowlanglistset[1], 1])
                record13 = cur.fetchall()
                for row13 in record13:
                    markup1 = types.InlineKeyboardButton(row13[0], callback_data = row13[0])
                    markup.add(markup1)
        
                bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Assalomu_alaykum_user"], parse_mode="Markdown", reply_markup=markup)

    cur.execute('SELECT * from province_address where status=%s', [1])
    recordpradrs = cur.fetchall()
    for rowpradrs in recordpradrs:
        if call.data == rowpradrs[0]:
            
            categories = rowpradrs[0]
            orde = rowpradrs[1]
            userlang = rowpradrs[2]
            
            msgid = call.inline_message_id
            
            cur.execute('DELETE FROM `province_address_abstract` WHERE id=%s', [str(call.from_user.id)])
            cur.execute('INSERT INTO `province_address_abstract` (`id`, `categories`, `language`) VALUES (%s, %s, %s)', [str(call.from_user.id), categories, userlang])
            db.commit()
            
            markup = types.InlineKeyboardMarkup()
            markup.row_width = 1
            
            cur.execute('SELECT * from region_address where categories=%s and language=%s and status=%s', [categories, userlang, 1])
            record13 = cur.fetchall()
            for row13 in record13:
                markup1 = types.InlineKeyboardButton(row13[2], callback_data = row13[2])
                markup.add(markup1)
            
            markup.row_width = 3
            markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
            markupij = types.InlineKeyboardButton("❔", callback_data='help')
            markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
            markup.add(markupii, markupij, markupik)
            
            bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Assalomu_alaykum_user"], parse_mode="Markdown", reply_markup=markup)
            
    cur.execute('SELECT * from region_address where status=%s', [1])
    recordpradrs = cur.fetchall()
    for rowpradrs in recordpradrs:
        if call.data == rowpradrs[2]:
            
            userlang = rowpradrs[3]
            
            msgid = call.inline_message_id
            
            cur.execute('UPDATE province_address_abstract SET region=%s WHERE id=%s', [rowpradrs[2], str(call.from_user.id)])
            db.commit()
            
            markup = types.InlineKeyboardMarkup()
            markup.row_width = 1
            cur.execute('SELECT * from main_menu where language=%s and status=%s', [userlang, 1])
            record13 = cur.fetchall()
            for row13 in record13:
                markup1 = types.InlineKeyboardButton(row13[0], callback_data = row13[0])
                markup.add(markup1)
            
            markup.row_width = 3
            markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
            markupij = types.InlineKeyboardButton("❔", callback_data='help')
            markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
            markup.add(markupii, markupij, markupik)
            
            bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Assalomu_alaykum_user"], parse_mode="Markdown", reply_markup=markup)
            
########################################
########################################
########################################
########################################
    
    
    if call.data == "Main_menu":
        
        msgid = call.inline_message_id
        
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        cur.execute('SELECT * from main_menu where language=%s and status=%s', [userlang, 1])
        record13 = cur.fetchall()
        for row13 in record13:
            markup1 = types.InlineKeyboardButton(row13[0], callback_data = row13[0])
            markup.add(markup1)
            
        markup.row_width = 3
        markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
        markupij = types.InlineKeyboardButton("❔", callback_data='help')
        markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
        markup.add(markupii, markupij, markupik)
        
        
        bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Assalomu_alaykum_user"], reply_markup=markup, parse_mode="Markdown")
            
            
    cur.execute('SELECT * from main_menu')
    recordmenu = cur.fetchall()
    for rowmenu in recordmenu:
        if call.data == rowmenu[0]:
            msgid = call.inline_message_id
            if rowmenu[1] == 1:
                
                #Taxi
                cur.execute('SELECT language from language where id = %s', [str(call.from_user.id)])
                record = cur.fetchall()
                for row in record:
                    userlang_for_taxi = row[0]
                
                dont_care = language[userlang_for_taxi]["Dont_care"]
                
                markup = types.InlineKeyboardMarkup()
                markup.row_width = 1
                markupii = types.InlineKeyboardButton(dont_care, callback_data='settingsmain')
                markup.add(markupii)
                
                markup.row_width = 1
                cur.execute('SELECT * from taxi where language=%s and status=%s', [userlang_for_taxi, 1])
                record_for_taxi = cur.fetchall()
                for row_for_taxi in record_for_taxi:
                    markup_for_taxi = types.InlineKeyboardButton(row_for_taxi[0], callback_data = row_for_taxi[0])
                    markup.add(markup_for_taxi)
            
                markup.row_width = 3
                markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
                markupij = types.InlineKeyboardButton("❔", callback_data='help')
                markupik = types.InlineKeyboardButton("⬅️", callback_data='Main_menu')
                markup.add(markupii, markupij, markupik)
            
                bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Assalomu_alaykum_user"], parse_mode="Markdown", reply_markup=markup)
                
            if rowmenu[1] == 2:
                print("2")
                #Mini Markets
                
                
                
                
            if rowmenu[1] == 3:
                print("3")
                
                
                
            if rowmenu[1] == 4:
                print("4")

                
                
                
                
                
                
                
                
#########################################
#########################################
#########################################
#########################################                
                
                
    cur.execute('SELECT car from trucks')
    record22 = cur.fetchall()
    for row22 in record22:
        if call.data == row22[0]:
            car=row22[0]
            carname=car
            msgid = call.inline_message_id
            def step1(call):
                
                textmessage1 = carname + language[userlang]["Where"]
                sent = bot.send_message(call.message.chat.id, textmessage1)
                bot.register_next_step_handler(sent, step2)
      
            def step2(call):
                
                address = call.text
          
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d")
                current_time = now.strftime("%H:%M:%S")
          
                cur.execute('SELECT MAX(orde) from buyurtma where id = %s', [str(call.from_user.id)])
                record1 = cur.fetchall()
                for row1 in record1:
                    row2 = row1[0]
                row2 = row2 + 1              
                cur.execute('INSERT INTO `buyurtma` (`id`, `orde`, `car`, `cDate`, `cTime`, `address`) VALUES (%s, %s, %s, %s, %s, %s)', [str(call.from_user.id), row2, carname, dt_string, current_time, address])
                db.commit()
                
                #if userlang == "en":
                textmessage2 = carname + language[userlang]["What"]
                #if userlang == "fa":
                #    textmessage2 = language[userlang]["What"] + carname
                sent1 = bot.send_message(call.chat.id, textmessage2)
                bot.register_next_step_handler(sent1, step3)
          
            def step3(call):
                
                vazifa = call.text
          
                cur.execute('SELECT MAX(orde) from buyurtma where id = %s', [str(call.from_user.id)])
                record1 = cur.fetchall()
                for row1 in record1:
                    row2 = row1[0]
          
                cur.execute('UPDATE buyurtma SET narxi=%s, vazifa=%s WHERE id=%s and orde=%s', [0, vazifa, str(call.from_user.id), row2])
                db.commit()
                
                send = str(call.from_user.id) + str(call.message_id)
                cur.execute('INSERT INTO `callback_message_id` (`userid`, `orde`, `messageid`) VALUES (%s, %s, %s)', [str(call.from_user.id), row2, send])
                db.commit()
                
                markup = types.InlineKeyboardMarkup()
                markup.row_width = 1
                markupia = types.InlineKeyboardButton(text=language[userlang]["Yes_send_it"], callback_data = send)
                markupib = types.InlineKeyboardButton(text=language[userlang]["No_cancel_it"], callback_data = 'buyurtmanibekorqilish')
                markup.add(markupia, markupib)
                if userlang == "en":
                    textmessage3 = carname + language[userlang]["Yuborish"]
                if userlang == "fa":
                    textmessage3 = language[userlang]["Yuborish"]
                bot.send_message(call.chat.id, textmessage3, reply_markup=markup)
                

            bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Enter_all"], parse_mode="Markdown", reply_markup=step1(call))   
    
    
    if call.data == "buyurtmanibekorqilish":
        msgid = call.inline_message_id
        cur.execute('SELECT MAX(orde) from buyurtma where id = %s', [str(call.from_user.id)])
        record10 = cur.fetchall()
        for row10 in record10:
            row0 = row10[0]
        cur.execute('DELETE FROM `buyurtma` WHERE id = %s and orde = %s', [str(call.from_user.id), row0])
        db.commit()
        
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        cur.execute('SELECT car from trucks')
        record13 = cur.fetchall()
        for row13 in record13:
            markup1 = types.InlineKeyboardButton(row13[0], callback_data = row13[0])
            markup.add(markup1)
        markup.row_width = 3
        markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
        markupij = types.InlineKeyboardButton("❔s", callback_data='help')
        markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
        markup.add(markupii, markupij, markupik)
        bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Bekor_qilish_user"], parse_mode="Markdown", reply_markup=markup)
   
   
    if call.data == "buyurtmanibekorqilish2":
        msgid = call.inline_message_id
        cur.execute('SELECT MAX(orde) from buyurtma where id = %s', [str(call.from_user.id)])
        record10 = cur.fetchall()
        for row10 in record10:
            row0 = row10[0]
        cur.execute('DELETE FROM `buyurtma` WHERE id = %s and orde = %s', [str(call.from_user.id), row0])
        db.commit()
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        markupi0 = types.InlineKeyboardButton("Taxi", callback_data='Taxi')
        markupia = types.InlineKeyboardButton("Labo", callback_data='Labo')
        markupib = types.InlineKeyboardButton("Motoroller", callback_data='Motoroller')
        markupic = types.InlineKeyboardButton("Munis", callback_data='Munis')
        markupid = types.InlineKeyboardButton("Kamaz", callback_data='Kamaz')
        markupie = types.InlineKeyboardButton("Zil", callback_data='Zil')
        markupif = types.InlineKeyboardButton("Traktor", callback_data='Traktor')
        markupig = types.InlineKeyboardButton("Moskvich", callback_data='Moskvich')
        markupih = types.InlineKeyboardButton("Jiguli", callback_data='Jiguli')
        markup.add(markupi0, markupia, markupib, markupic, markupid, markupie, markupif, markupig, markupih)
        markup.row_width = 3
        markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
        markupij = types.InlineKeyboardButton("❔", callback_data='help')
        markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
        markup.add(markupii, markupij, markupik)
        bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Bekor_qilish_user"], parse_mode="Markdown", reply_markup=markup)
        
    # user sub-side

    cur.execute('SELECT * from callback_message_id where userid = %s', [str(call.from_user.id)])
    record00 = cur.fetchall()
    for row00 in record00:
        if call.data == row00[2]:
            row0 = row00[0]
            row1 = row00[1]
            row2 = row00[2]
            
            msgid = call.inline_message_id
      
            orde1 = str(row1)
            row21 = row1
      
            cur.execute('SELECT address, vazifa, car from buyurtma where id=%s and orde=%s', [str(call.from_user.id), row1])
            record = cur.fetchall()
            for row in record:
                useraddress = row[0]
                uservazifa = row[1]
                cartype = row[2]
          
            #xabar = language[userlang]["Manzili"] + useraddress + language[userlang]["Buyurtma"] + uservazifa
            sms0 = language[userlang]["Wait_user"]

      
            def step4(call):
                cur.execute('SELECT * from ishchi_registration_info where status = %s and car = %s and id!=%s', [1, cartype, str(call.from_user.id)])
                record = cur.fetchall()
                for row in record:
                    ishchiid = row[0]
                    
                    ikkip = "+2000" + str(call.from_user.id) + orde1
                    cur.execute('INSERT INTO `addsub` (`addsubname`, `addsub`, `ishchiid0`, `userid0`, `umumiyid0`, `addsuborde`) VALUES (%s, %s, %s, %s, %s, %s)', ["+2000", ikkip, ishchiid, str(call.from_user.id), ishchiid, row21])
                    db.commit()
              
                    beshp = "+5000" + str(call.from_user.id) + orde1
                    cur.execute('INSERT INTO `addsub` (`addsubname`, `addsub`, `ishchiid0`, `userid0`, `umumiyid0`, `addsuborde`) VALUES (%s, %s, %s, %s, %s, %s)', ["+5000", beshp, ishchiid, str(call.from_user.id), ishchiid, row21])
                    db.commit()
              
                    onp = "+10000" + str(call.from_user.id) + orde1
                    cur.execute('INSERT INTO `addsub` (`addsubname`, `addsub`, `ishchiid0`, `userid0`, `umumiyid0`, `addsuborde`) VALUES (%s, %s, %s, %s, %s, %s)', ["+10000", onp, ishchiid, str(call.from_user.id), ishchiid, row21])
                    db.commit()
              
                    ikkim = "-2000" + str(call.from_user.id) + orde1
                    cur.execute('INSERT INTO `addsub` (`addsubname`, `addsub`, `ishchiid0`, `userid0`, `umumiyid0`, `addsuborde`) VALUES (%s, %s, %s, %s, %s, %s)', ["-2000", ikkim, ishchiid, str(call.from_user.id), ishchiid, row21])
                    db.commit()
              
                    beshm = "-5000" + str(call.from_user.id) + orde1
                    cur.execute('INSERT INTO `addsub` (`addsubname`, `addsub`, `ishchiid0`, `userid0`, `umumiyid0`, `addsuborde`) VALUES (%s, %s, %s, %s, %s, %s)', ["-5000", beshm, ishchiid, str(call.from_user.id), ishchiid, row21])
                    db.commit()
              
                    onm = "-10000" + str(call.from_user.id) + orde1
                    cur.execute('INSERT INTO `addsub` (`addsubname`, `addsub`, `ishchiid0`, `userid0`, `umumiyid0`, `addsuborde`) VALUES (%s, %s, %s, %s, %s, %s)', ["-10000", onm, ishchiid, str(call.from_user.id), ishchiid, row21])
                    db.commit()
              
                    cur.execute('INSERT INTO `bargain` (`user_id`, `ishchi_id`, `umumiy_id`, `narxi`, `orde`) VALUES (%s, %s, %s, %s, %s)', [str(call.from_user.id), ishchiid, 0, 0, row21])
                    db.commit()
              
                    # ishchi sub-side
                    ikkim2 = "~"
                    beshm2 = "~"
                    onm2 = "~"
                    
                    cur.execute('SELECT * from language where id = %s', [ishchiid])
                    record = cur.fetchall()
                    for row in record:
                        userid = row[0]
                        userlang1 = row[1]  
            
                    manzil = language[userlang1]["Manzili"]
                    buyurtma = language[userlang1]["Buyurtma"]
                    xabar = manzil + useraddress + buyurtma + uservazifa
            
                    narx_button = language[userlang1]["Price_user"]
                    som = language[userlang1]["Currency_user"]
                    Narx = narx_button + "0" + som
            
                    a2 = "+2000" + language[userlang1]["Currency_user"]
                    a5 = "+5000" + language[userlang1]["Currency_user"]
                    a10 = "+10000" + language[userlang1]["Currency_user"]
                    
                    markup = types.InlineKeyboardMarkup()
                    markup.row_width = 1
                    markupib = types.InlineKeyboardButton(Narx, callback_data='narxni_kiritib_korish1')
                    markup.add(markupib)
                    markup.row_width = 3
                    markupia = types.InlineKeyboardButton(a2, callback_data = ikkip)
                    markupib = types.InlineKeyboardButton(a5, callback_data = beshp)
                    markupic = types.InlineKeyboardButton(a10, callback_data = onp)
                    markupid = types.InlineKeyboardButton("~", callback_data = '~')
                    markupie = types.InlineKeyboardButton("~", callback_data = '~')
                    markupif = types.InlineKeyboardButton("~", callback_data = '~')
                    markup.add(markupia, markupib, markupic, markupid, markupie, markupif)
                    #markup.row_width = 1
                    #markupib = types.InlineKeyboardButton("Send", callback_data = send2)
                    #markup.add(markupib)
                    markup.row_width = 2
                    markupic = types.InlineKeyboardButton("❌", callback_data = 'delete_message')
                    markupid = types.InlineKeyboardButton("🏠", callback_data = 'ishni_boshladik')
                    markup.add(markupic, markupid)
              
                    # end ishchi sub-side
              
                    bot.send_message(ishchiid, xabar, parse_mode="Markdown", reply_markup=markup)
                    
                resend = language[userlang]["Resend_user"] 
                resend_button = language[userlang]["Resend_button_user"]
                markup = types.InlineKeyboardMarkup()
                markup.row_width = 1
                markupia = types.InlineKeyboardButton(resend_button, callback_data = 'resend_order')
                markup.add(markupia)
            
                bot.send_message(call.message.chat.id, resend, parse_mode="Markdown", reply_markup=markup)
                
            bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=sms0, parse_mode="Markdown", reply_markup=step4(call))



    if call.data == "resend_order":
        msgid = call.inline_message_id
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        markupi0 = types.InlineKeyboardButton("Taxi", callback_data='Taxi')
        markupia = types.InlineKeyboardButton("Labo", callback_data='Labo')
        markupib = types.InlineKeyboardButton("Motoroller", callback_data='Motoroller')
        markupic = types.InlineKeyboardButton("Munis", callback_data='Munis')
        markupid = types.InlineKeyboardButton("Kamaz", callback_data='Kamaz')
        markupie = types.InlineKeyboardButton("Zil", callback_data='Zil')
        markupif = types.InlineKeyboardButton("Traktor", callback_data='Traktor')
        markupig = types.InlineKeyboardButton("Moskvich", callback_data='Moskvich')
        markupih = types.InlineKeyboardButton("Jiguli", callback_data='Jiguli')
        markup.add(markupi0, markupia, markupib, markupic, markupid, markupie, markupif, markupig, markupih)
        markup.row_width = 3
        markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
        markupij = types.InlineKeyboardButton("❔", callback_data='help')
        markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
        markup.add(markupii, markupij, markupik)
        bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Bekor_qilish_user"], parse_mode="Markdown", reply_markup=markup)

    
    cur.execute('SELECT * from addsub where umumiyid0 = %s', [str(call.from_user.id)])
    record44 = cur.fetchall()
    for row44 in record44:
        if call.data == row44[1]:
            addsubname=row44[0]
            addsub=row44[1]
            addsubishchiid=row44[2]
            addsubuserid=row44[3]
            addsubumumiyid=row44[4]
            addsuborde=row44[5]
            
            orde2 = str(addsuborde)
            msgid = call.inline_message_id
            
            cur.execute('UPDATE bargain SET umumiy_id=%s WHERE ishchi_id=%s and orde=%s and user_id=%s', [str(call.from_user.id), addsubishchiid, addsuborde, addsubuserid])
            db.commit()
            
            cur.execute('SELECT narxi from bargain where ishchi_id = %s and user_id=%s and orde=%s', [addsubishchiid, addsubuserid, addsuborde])
            record0 = cur.fetchall()
            for row0 in record0:
                row01 = row0[0]
            
            som = language[userlang]["Currency_user"]
            
            addsubname1 = "+2000"
            addsubname2 = "+5000"
            addsubname3 = "+10000"
            addsubname4 = "-2000"
            addsubname5 = "-5000"
            addsubname6 = "-10000"
            addsubname11 = "+2000" + som
            addsubname22 = "+5000" + som
            addsubname33 = "+10000" + som
            addsubname44 = "-2000" + som
            addsubname55 = "-5000" + som
            addsubname66 = "-10000" + som
            
            x = int(addsubname)
            y = x + row01
            
            if y < 10000:
                addsubname6 = "~"
                addsubname66 = "~"
                
            if y < 5000:
                addsubname5 = "~"
                addsubname55 = "~"
                
            if y < 2000:
                addsubname4 = "~"
                addsubname44 = "~"
                
            addsub = orde2 + "addsub" + addsubuserid
            
            if y >= 0:
                cur.execute('UPDATE bargain SET narxi=%s, addsub=%s WHERE ishchi_id=%s and orde=%s and user_id=%s', [y, addsub, addsubishchiid, addsuborde, addsubuserid])
                db.commit()
            
            cur.execute('SELECT address, vazifa from buyurtma where id=%s and orde=%s', [addsubuserid, addsuborde])
            record = cur.fetchall()
            for row in record:
                useraddress = row[0]
                uservazifa = row[1]
                
            #cur.execute('SELECT * from language where id = %s', [str(call.from_user.id)])
            #record = cur.fetchall()
            #for row in record:
            #    userid = row[0]
            #    userlang1 = row[1]  
            
            manzil = language[userlang]["Manzili"]
            buyurtma = language[userlang]["Buyurtma"]
            xabar = manzil + useraddress + buyurtma + uservazifa
            
            ikkip = addsubname1 + addsubuserid + orde2
            beshp = addsubname2 + addsubuserid + orde2
            onp = addsubname3 + addsubuserid + orde2
            ikkim = addsubname4 + addsubuserid + orde2
            beshm = addsubname5 + addsubuserid + orde2
            onm = addsubname6 + addsubuserid + orde2
            
            if y < 0:
                y = row01
            
            narx_button = language[userlang]["Price_user"]
            som = language[userlang]["Currency_user"]
            Narx = narx_button + str(y) + som
            send_button = language[userlang]["Send_button"]
            
            if addsubumumiyid == addsubishchiid:
                markup = types.InlineKeyboardMarkup()
                markup.row_width = 1
                markupib = types.InlineKeyboardButton(Narx, callback_data='narxni_kiritib_korish1')
                markup.add(markupib)
                markup.row_width = 3
                markupia = types.InlineKeyboardButton(addsubname11, callback_data = ikkip)
                markupib = types.InlineKeyboardButton(addsubname22, callback_data = beshp)
                markupic = types.InlineKeyboardButton(addsubname33, callback_data = onp)
                markupid = types.InlineKeyboardButton(addsubname44, callback_data = ikkim)
                markupie = types.InlineKeyboardButton(addsubname55, callback_data = beshm)
                markupif = types.InlineKeyboardButton(addsubname66, callback_data = onm)
                markup.add(markupia, markupib, markupic, markupid, markupie, markupif)
                markup.row_width = 1
                markupib = types.InlineKeyboardButton(send_button, callback_data = addsub)
                markup.add(markupib)
                markup.row_width = 2
                markupic = types.InlineKeyboardButton("❌", callback_data = 'delete_message')
                markupid = types.InlineKeyboardButton("🏠", callback_data = 'ishni_boshladik')
                markup.add(markupic, markupid)
                
                bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=xabar, parse_mode="Markdown", reply_markup=markup)
                
            if addsubumumiyid == addsubuserid:
                markup = types.InlineKeyboardMarkup()
                markup.row_width = 1
                markupib = types.InlineKeyboardButton(Narx, callback_data='narxni_kiritib_korish1')
                markup.add(markupib)
                markup.row_width = 3
                markupia = types.InlineKeyboardButton(addsubname11, callback_data = ikkip)
                markupib = types.InlineKeyboardButton(addsubname22, callback_data = beshp)
                markupic = types.InlineKeyboardButton(addsubname33, callback_data = onp)
                markupid = types.InlineKeyboardButton(addsubname44, callback_data = ikkim)
                markupie = types.InlineKeyboardButton(addsubname55, callback_data = beshm)
                markupif = types.InlineKeyboardButton(addsubname66, callback_data = onm)
                markup.add(markupia, markupib, markupic, markupid, markupie, markupif)
                markup.row_width = 1
                markupib = types.InlineKeyboardButton(send_button, callback_data = addsub)
                markup.add(markupib)
                markup.row_width = 2
                markupic = types.InlineKeyboardButton("❌", callback_data = 'delete_message')
                markupid = types.InlineKeyboardButton("🏠", callback_data = 'main')
                markup.add(markupic, markupid)
            
                bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=xabar, parse_mode="Markdown", reply_markup=markup)
            
            
    if call.data == "delete_message":
      msgid = call.inline_message_id
      message_is_deleted = language[userlang]["Message_is_deleted"]
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text = message_is_deleted)
              


    cur.execute('SELECT * from bargain where umumiy_id = %s', [str(call.from_user.id)])
    recordsend2 = cur.fetchall()
    for rowsend2 in recordsend2:
        if call.data == rowsend2[5]:
            rowsend2userid = rowsend2[0]
            rowsend2ishchiid = rowsend2[1]
            rowsend2umumiyid = rowsend2[2]
            rowsend2narxi = rowsend2[3]
            rowsend2orde = rowsend2[4]
            rowsend2send2orde = rowsend2[5]
            
            msgid = call.inline_message_id
            
            rowsend2userid2 = rowsend2userid
            rowsend2ishchiid2 = rowsend2ishchiid
            rowsend2umumiyid2 = rowsend2umumiyid
            
            if rowsend2ishchiid == str(call.from_user.id):
                cur.execute('UPDATE addsub SET umumiyid0=%s WHERE ishchiid0=%s and addsuborde=%s and userid0=%s', [rowsend2userid, rowsend2ishchiid, rowsend2orde, rowsend2userid])
                db.commit()
                
                cur.execute('SELECT * from language where id = %s', [rowsend2userid])
                record = cur.fetchall()
                for row in record:
                    userid = row[0]
                    userlang1 = row[1]
                
            if rowsend2userid == str(call.from_user.id):
                cur.execute('UPDATE addsub SET umumiyid0=%s WHERE ishchiid0=%s and addsuborde=%s and userid0=%s', [rowsend2ishchiid, rowsend2ishchiid, rowsend2orde, rowsend2userid])
                db.commit()
                
                cur.execute('SELECT * from language where id = %s', [rowsend2ishchiid])
                record = cur.fetchall()
                for row in record:
                    userid = row[0]
                    userlang1 = row[1]
                
            cur.execute('SELECT address, vazifa from buyurtma where id=%s and orde=%s', [rowsend2userid, rowsend2orde])
            record = cur.fetchall()
            for row in record:
                useraddress = row[0]
                uservazifa = row[1]
                
            som = language[userlang1]["Currency_user"]
            
            #xabar = useraddress + "\n" + uservazifa
            
            addsubname1 = "+2000"
            addsubname2 = "+5000"
            addsubname3 = "+10000"
            addsubname4 = "-2000"
            addsubname5 = "-5000"
            addsubname6 = "-10000"
            addsubname11 = "+2000" + som
            addsubname22 = "+5000" + som
            addsubname33 = "+10000" + som
            addsubname44 = "-2000" + som
            addsubname55 = "-5000" + som
            addsubname66 = "-10000" + som
            
            y = rowsend2narxi
            
            if y < 10000:
                addsubname6 = "~"
                addsubname66 = "~"
                
            if y < 5000:
                addsubname5 = "~"
                addsubname55 = "~"
                
            if y < 2000:
                addsubname4 = "~"
                addsubname44 = "~"
                
            addsub = str(rowsend2orde) + "addsub" + rowsend2userid
            callok = str(rowsend2orde) + "callok" + rowsend2userid
            
            cur.execute('UPDATE bargain SET callok=%s WHERE ishchi_id=%s and orde=%s and user_id=%s', [callok, rowsend2ishchiid, rowsend2orde, rowsend2userid])
            db.commit()
            
            def step4(call):
                
                orde3 = str(rowsend2orde)
            
                ikkipl = "+2000" + rowsend2userid + orde3
                beshpl = "+5000" + rowsend2userid + orde3
                onpl = "+10000" + rowsend2userid + orde3
                ikkimi = "-2000" + rowsend2userid + orde3
                beshmi = "-5000" + rowsend2userid + orde3
                onmi = "-10000" + rowsend2userid + orde3
                
                manzil = language[userlang1]["Manzili"]
                buyurtma = language[userlang1]["Buyurtma"]
                xabar = manzil + useraddress + buyurtma + uservazifa
            
                narx_button = language[userlang1]["Price_user"]
                som = language[userlang1]["Currency_user"]
                Narx = narx_button + str(y) + som
                send_button = language[userlang1]["Send_button"]
                
                if rowsend2umumiyid == rowsend2userid:
                    markup = types.InlineKeyboardMarkup()
                    markup.row_width = 1
                    markupib = types.InlineKeyboardButton(Narx, callback_data='narxni_kiritib_korish1')
                    markup.add(markupib)
                    markup.row_width = 3
                    markupia = types.InlineKeyboardButton(addsubname11, callback_data = ikkipl)
                    markupib = types.InlineKeyboardButton(addsubname22, callback_data = beshpl)
                    markupic = types.InlineKeyboardButton(addsubname33, callback_data = onpl)
                    markupid = types.InlineKeyboardButton(addsubname44, callback_data = ikkimi)
                    markupie = types.InlineKeyboardButton(addsubname55, callback_data = beshmi)
                    markupif = types.InlineKeyboardButton(addsubname66, callback_data = onmi)
                    markup.add(markupia, markupib, markupic, markupid, markupie, markupif)
                    markup.row_width = 1
                    markupib = types.InlineKeyboardButton("OK", callback_data = callok)
                    markup.add(markupib)
                    markup.row_width = 2
                    markupic = types.InlineKeyboardButton("❌", callback_data = 'delete_message')
                    markupid = types.InlineKeyboardButton("🏠", callback_data = 'main')
                    markup.add(markupic, markupid)
                    
                    bot.send_message(rowsend2ishchiid, xabar, parse_mode="Markdown", reply_markup=markup)
                    
                elif rowsend2umumiyid == rowsend2ishchiid:
                    markup = types.InlineKeyboardMarkup()
                    markup.row_width = 1
                    markupib = types.InlineKeyboardButton(Narx, callback_data='narxni_kiritib_korish1')
                    markup.add(markupib)
                    markup.row_width = 3
                    markupia = types.InlineKeyboardButton(addsubname11, callback_data = ikkipl)
                    markupib = types.InlineKeyboardButton(addsubname22, callback_data = beshpl)
                    markupic = types.InlineKeyboardButton(addsubname33, callback_data = onpl)
                    markupid = types.InlineKeyboardButton(addsubname44, callback_data = ikkimi)
                    markupie = types.InlineKeyboardButton(addsubname55, callback_data = beshmi)
                    markupif = types.InlineKeyboardButton(addsubname66, callback_data = onmi)
                    markup.add(markupia, markupib, markupic, markupid, markupie, markupif)
                    markup.row_width = 1
                    markupib = types.InlineKeyboardButton("OK", callback_data = callok)
                    markup.add(markupib)
                    markup.row_width = 2
                    markupic = types.InlineKeyboardButton("❌", callback_data = 'delete_message')
                    markupid = types.InlineKeyboardButton("🏠", callback_data = 'ishni_boshladik')
                    markup.add(markupic, markupid)
                    #markup.row_width = 1
                    #markupib = types.InlineKeyboardButton(send_button, callback_data=addsub)
                    #markup.add(markupib)
                    bot.send_message(rowsend2userid, xabar, parse_mode="Markdown", reply_markup=markup)
          
            bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Please choose:", parse_mode="Markdown", reply_markup=step4(call))
            


    cur.execute('SELECT * from bargain')
    recordcalldata = cur.fetchall()
    for rowcalldata in recordcalldata:
        if call.data == rowcalldata[6]:
            callokuserid = rowcalldata[0]
            callokishchiid = rowcalldata[1]
            callokumumiyid = rowcalldata[2]
            calloknarxi = rowcalldata[3]
            callokorde = rowcalldata[4]
            callokaddsub = rowcalldata[5]
            callokcallok = rowcalldata[6]
            
            msgid = call.inline_message_id
            
            current_id = str(call.from_user.id)
            
            def accept(call):
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d")
                current_time = now.strftime("%H:%M:%S")
                
                cur.execute('UPDATE buyurtma SET narxi=%s, phone=%s, bajarilgan_ishlari=%s, ishchi_qabul_qilgan_kun=%s, ishchi_qabul_qilgan_soat=%s WHERE id=%s and orde=%s', [calloknarxi, "+998934493649", callokishchiid, dt_string, current_time, callokuserid, callokorde])
                db.commit()
            
                cur.execute('SELECT id, car, raqam, name from ishchi_registration_info where id = %s', [callokishchiid])
                record = cur.fetchall()
                for row in record:
                    ishchiid = row[0]
                    ishchicar = row[1]
                    ishchicarnum = row[2]
                    ishchiname = row[3]
                
                cur.execute('SELECT id, phone, narxi, bajarilgan_ishlari, ishchi_qabul_qilgan_kun, ishchi_qabul_qilgan_soat, vazifa, address from buyurtma where id = %s and bajarilgan_ishlari = %s and orde = %s', [callokuserid, callokishchiid, callokorde])
                record = cur.fetchall()
                for row in record:
                    buyurtmauserid = row[0]
                    buyurtmauserphone = row[1]
                    buyurtmanarxi = row[2]
                    buyurtmaishchiid = row[3]
                    buyurtmaacceptday = row[4]
                    buyurtmaaccepttime = row[5]
                    buyurtmajob = row[6]
                    buyurtmaaddress = row[7]
                    
                    
                cur.execute('SELECT language from language where id = %s', [buyurtmaishchiid])
                recordi = cur.fetchall()
                for rowi in recordi:
                    userlangishchi = rowi[0] 
                    
                xabarishchi = language[userlangishchi]["Narxi"] + buyurtmauserphone + language[userlangishchi]["Narxi"] + str(buyurtmanarxi) + "\n" + language[userlangishchi]["Manzili"] + buyurtmaaddress + "\n" + language[userlangishchi]["Buyurtma"] + buyurtmajob + "\n\n" + language[userlangishchi]["Sana"] + str(buyurtmaacceptday) + language[userlangishchi]["Vaqti"] + str(buyurtmaaccepttime)
                
                bot.send_message(buyurtmaishchiid, xabarishchi)
                
                markupi = types.InlineKeyboardMarkup()
                markupi.row_width = 1
                markupiid = types.InlineKeyboardButton("🏠", callback_data = 'ishni_boshladik')
                markupi.add(markupiid)
                bot.send_message(buyurtmaishchiid, "Main menu", parse_mode="Markdown", reply_markup=markupi)
                
                #######
                
                cur.execute('SELECT language from language where id = %s', [buyurtmauserid])
                recordu = cur.fetchall()
                for rowu in recordu:
                    userlanguser = rowu[0]
                
                xabaruser = ishchiname + "\n\n" + ishchicar + "\n" + ishchicarnum
                bot.send_message(buyurtmauserid, xabaruser)
                
                markupu = types.InlineKeyboardMarkup()
                markupu.row_width = 1
                markupuid = types.InlineKeyboardButton("🏠", callback_data = 'main')
                markupu.add(markupuid)
                bot.send_message(buyurtmauserid, "Main menu", parse_mode="Markdown", reply_markup=markupu)
          
            bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Buyurtma qabul qilindi", parse_mode="Markdown", reply_markup=accept(call))
            
    ###################
    #  END USER SIDE
    ###################
    
      
    ###################
    #  ISHCHI SIDE
    ###################
      
    if call.data == "settingsmainishchi":
      reg = language[userlang]["Register_ishchi"]
      markup = types.InlineKeyboardMarkup()
      markupib = types.InlineKeyboardButton("Til - Язык", callback_data='settingslangishchi')
      markupic = types.InlineKeyboardButton(reg, callback_data='registration')
      markupid = types.InlineKeyboardButton("🏠", callback_data='main')
      markup.add(markupib, markupic, markupid)
      msgid = call.inline_message_id
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Settings_ishchi"], parse_mode="Markdown", reply_markup=markup)
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
      
    if call.data == "settingslangishchi":
      msgid = call.inline_message_id
      markup = types.InlineKeyboardMarkup()
      markupib = types.InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data='settingslangenishchi')
      markupic = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='settingslangfaishchi')
      markup.add(markupib,markupic)
      markupif = types.InlineKeyboardButton("Ortga - Назад", callback_data='settingsmain')
      markup.add(markupif)
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Tilni tanlang!🇺🇿\nВыберите язык!🇷🇺", parse_mode="Markdown", reply_markup=markup)
      
    if call.data == "settingslangenishchi":
      cur.execute('DELETE FROM `language` WHERE id=%s', [str(call.from_user.id)])
      cur.execute('INSERT INTO `language` (`id`, `language`) VALUES (%s, %s)', [str(call.from_user.id), "en"])
      db.commit()
      msgid = call.inline_message_id
      cur.execute('SELECT * from language where id = %s', [str(call.from_user.id)])
      record = cur.fetchall()
      for row in record:
          userid = row[0]
          userlang = row[1]
          
      cur.execute('select status from ishchi_registration_info where id = %s', [str(call.from_user.id)])
      recordstatus = cur.fetchall()
      if not recordstatus:
          
          reply_text = language[userlang]["Assalomu_alaykum_ishchi"]
          Register_ishchi = language[userlang]["Register_ishchi"]
          markup = types.InlineKeyboardMarkup()
          markup.row_width = 1
          markupia = types.InlineKeyboardButton(Register_ishchi, callback_data='registration')
          markupib = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
          markup.add(markupia, markupib)
          #bot.send_message(call.message.chat.id, reply_text, parse_mode="Markdown", reply_markup=markup)
          
      for rowstatus in recordstatus:
          status = rowstatus[0]
          if status == "0":
              
              display_text = "🔔 " + language[userlang]["Ishni_boshlash"]
              call_data = "ishni_boshladik"
              display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
              reply_text = language[userlang]["Tanaffus_ishchi"]
              
              markup = types.InlineKeyboardMarkup()
              markup.row_width = 1
              markupib = types.InlineKeyboardButton(display_text, callback_data=call_data)
              markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
              markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
              markup.add(markupib, markupid, markupie)
              
          if status == "1":
              
              display_text = "🔕 " + language[userlang]["Tanaffus_qilish"]
              call_data = "bandman"
              display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
              reply_text = language[userlang]["Ishda_ishchi"]
            
              markup = types.InlineKeyboardMarkup()
              markup.row_width = 1
              markupib = types.InlineKeyboardButton(display_text, callback_data=call_data)
              markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
              markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
              markup.add(markupib, markupid, markupie)
              
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=reply_text, reply_markup=markup)
    if call.data == "settingslangfaishchi":
      cur.execute('DELETE FROM `language` WHERE id=%s', [str(call.from_user.id)])
      cur.execute('INSERT INTO `language` (`id`, `language`) VALUES (%s, %s)', [str(call.from_user.id), "fa"])
      db.commit()
      msgid = call.inline_message_id
      cur.execute('SELECT * from language where id = %s', [str(call.from_user.id)])
      record = cur.fetchall()
      for row in record:
          userid = row[0]
          userlang = row[1]
          
      cur.execute('select status from ishchi_registration_info where id = %s', [str(call.from_user.id)])
      recordstatus = cur.fetchall()
      if not recordstatus:
          
          reply_text = language[userlang]["Assalomu_alaykum_ishchi"]
          Register_ishchi = language[userlang]["Register_ishchi"]
          markup = types.InlineKeyboardMarkup()
          markup.row_width = 1
          markupia = types.InlineKeyboardButton(Register_ishchi, callback_data='registration')
          markupib = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
          markup.add(markupia, markupib)
          #bot.send_message(call.message.chat.id, reply_text, parse_mode="Markdown", reply_markup=markup)
          
      for rowstatus in recordstatus:
          status = rowstatus[0]
          if status == "0":
              
              display_text = "🔔 " + language[userlang]["Ishni_boshlash"]
              call_data = "ishni_boshladik"
              display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
              reply_text = language[userlang]["Tanaffus_ishchi"]
              
              markup = types.InlineKeyboardMarkup()
              markup.row_width = 1
              markupib = types.InlineKeyboardButton(display_text, callback_data=call_data)
              markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
              markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
              markup.add(markupib, markupid, markupie)
              
          if status == "1":
              
              display_text = "🔕 " + language[userlang]["Tanaffus_qilish"]
              call_data = "bandman"
              display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
              reply_text = language[userlang]["Ishda_ishchi"]
            
              markup = types.InlineKeyboardMarkup()
              markup.row_width = 1
              markupib = types.InlineKeyboardButton(display_text, callback_data=call_data)
              markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
              markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
              markup.add(markupib, markupid, markupie)
              
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=reply_text, reply_markup=markup)
      
      
    if call.data == "registration":
      msgid = call.inline_message_id
      markup = types.InlineKeyboardMarkup()
      markup.row_width = 1
      markupia = types.InlineKeyboardButton("Taxi", callback_data='Taxi_reg')
      markupib = types.InlineKeyboardButton("Labo", callback_data='Labo_reg')
      markupic = types.InlineKeyboardButton("Motoroller", callback_data='Motoroller_reg')
      markupid = types.InlineKeyboardButton("Munis", callback_data='Munis_reg')
      markupie = types.InlineKeyboardButton("Kamaz", callback_data='Kamaz_reg')
      markupif = types.InlineKeyboardButton("Zil", callback_data='Zil_reg')
      markupig = types.InlineKeyboardButton("Traktor", callback_data='Traktor_reg')
      markupid1 = types.InlineKeyboardButton("Moskvich", callback_data='Moskvich_reg')
      markupie1 = types.InlineKeyboardButton("Jiguli", callback_data='Jiguli_reg')
      markup.add(markupia, markupib, markupic, markupid, markupie, markupif, markupig, markupid1, markupie1)
      markup.row_width = 3
      markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
      markupij = types.InlineKeyboardButton("❔", callback_data='help')
      markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
      markup.add(markupii, markupij, markupik)
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Registration_car_ishchi"], parse_mode="Markdown", reply_markup=markup)
      
            
    cur.execute('SELECT * from trucks')
    recordcarreg = cur.fetchall()
    for rowcarreg in recordcarreg:
        
        if call.data == rowcarreg[1]:
            cartypes = rowcarreg[0]
            carreg = rowcarreg[1]
            msgid = call.inline_message_id
      
            def step1(call):
                Car_number_order_ishchi = language[userlang]["Car_number_order_ishchi"]
                sent = bot.send_message(call.message.chat.id, Car_number_order_ishchi)
                bot.register_next_step_handler(sent, step2)
      
            def step2(call):
                
                raqam = call.text
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d")
                current_time = now.strftime("%H:%M:%S")
                
                cur.execute('SELECT * from ishchi_registration_info where id = %s', [str(call.from_user.id)])
                record10 = cur.fetchall()
                if not record10:
                    
                    cur.execute('INSERT INTO `ishchi_registration_info` (`id`, `car`, `raqam`, `reg_date`, `reg_time`) VALUES (%s, %s, %s, %s, %s)', [str(call.from_user.id), cartypes, raqam, dt_string, current_time])
                    db.commit()
                    
                else:
                    for row in record10:
                        rowid10 = row[0]
                        
                        cur.execute('SELECT status from ishchi_registration_info where id = %s', [str(call.from_user.id)])
                        record11 = cur.fetchall()
                        if not record11:
                            cur.execute('UPDATE ishchi_registration_info SET car=%s, raqam=%s WHERE id=%s', [cartypes, raqam, str(call.from_user.id)])
                            db.commit()
                        
                        else:
                            for row11 in record11:
                                status11 = row11
                                cur.execute('UPDATE ishchi_registration_info SET car=%s, raqam=%s, status=%s WHERE id=%s', [cartypes, raqam, status11, str(call.from_user.id)])
                                db.commit()
                        
                Enter_name_ishchi = language[userlang]["Enter_name_ishchi"]
                sent1 = bot.send_message(call.chat.id, Enter_name_ishchi)
                bot.register_next_step_handler(sent1, step3)
          
            def step3(call):
                
                ism = call.text
              
                cur.execute('UPDATE ishchi_registration_info SET name=%s WHERE id=%s', [ism, str(call.from_user.id)])
                db.commit()
                
                display_text_ish = "🔔 " + language[userlang]["Ishni_boshlash"]
                display_text_break = "🔕 " + language[userlang]["Tanaffus_qilish"]
                display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
                
                markup = types.InlineKeyboardMarkup()
                markup.row_width = 1
                markupib = types.InlineKeyboardButton(display_text_ish, callback_data='ishni_boshladik')
                markupic = types.InlineKeyboardButton(display_text_break, callback_data='bandman')
                markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
                markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
                markup.add(markupib, markupic, markupid, markupie)
                bot.send_message(call.chat.id, language[userlang]["Assalomu_alaykum_ishchi"], parse_mode="Markdown", reply_markup=markup)
          
            bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Registration_car_number_ishchi"], parse_mode="Markdown", reply_markup=step1(call))
      
      
    if call.data == "ishni_boshladik":
      msgid = call.inline_message_id
      now = datetime.now()
      dt_string = now.strftime("%Y-%m-%d")
      current_time = now.strftime("%H:%M:%S")
                       
      cur.execute('UPDATE ishchi_registration_info SET status=%s WHERE id=%s', [1, str(call.from_user.id)])
      db.commit()
      
      Tanaffus_qilish = "🔕 " + language[userlang]["Tanaffus_qilish"]
      display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
      
      markup = types.InlineKeyboardMarkup()
      markup.row_width = 1
      #markupib = types.InlineKeyboardButton("🔔 Ishdaman", callback_data='ishni_boshladik')
      markupic = types.InlineKeyboardButton(Tanaffus_qilish, callback_data='bandman')
      markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
      markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
      markup.add(markupic, markupid, markupie)
          
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Ishda_ishchi"], parse_mode="Markdown", reply_markup=markup)
    
    
    
    if call.data == "bandman":
      msgid = call.inline_message_id
      now = datetime.now()
      dt_string = now.strftime("%Y-%m-%d")
      current_time = now.strftime("%H:%M:%S")
                       
      cur.execute('UPDATE ishchi_registration_info SET status=%s WHERE id=%s', [0, str(call.from_user.id)])
      db.commit()
      
      Ishni_boshlash = "🔔 " + language[userlang]["Ishni_boshlash"]
      display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
      
      markup = types.InlineKeyboardMarkup()
      markup.row_width = 1
      markupib = types.InlineKeyboardButton(Ishni_boshlash, callback_data='ishni_boshladik')
      #markupic = types.InlineKeyboardButton("🔕 Tanaffusdaman", callback_data='bandman')
      markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
      markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
      markup.add(markupib, markupid, markupie)
          
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Tanaffus_ishchi"], parse_mode="Markdown", reply_markup=markup)
    
    
    
    if call.data == "bajargan_ishlari":
      msgid = call.inline_message_id
      
      def bajargan_ishlari(call):
          number = 0
          #cur.execute('SELECT ishchi_qabul_qilgan_kun, ishchi_qabul_qilgan_soat, narxi, vazifa, address from buyurtma where bajarilgan_ishlari=%s and orde!=%s', [str(call.from_user.id), 0])
          cur.execute('SELECT ishchi_qabul_qilgan_kun, ishchi_qabul_qilgan_soat, narxi, vazifa, address from buyurtma where id=%s and orde!=%s', ["1051015468", 0])
          record2 = cur.fetchall()
          if not record2:
              allinone = language[userlang]["Bajarilgan_ishlar_not"]
              bot.send_message(call.message.chat.id, text=allinone)
          for row in record2:
              useracceptday= row[0]
              useraccepttime= row[1]
              useracceptprice = row[2]
              useracceptorderjob= row[3]
              useracceptorderaddress= row[4]
              
              number = number + 1
              
              allinone = str(number) + ".\n" + language[userlang]["Sana"] + str(row[0]) + language[userlang]["Vaqti"] + str(row[1]) + language[userlang]["Narxi"] + str(row[2]) + language[userlang]["Buyurtma"] + row[3] + language[userlang]["Manzili"] + row[4]
              
              bot.send_message(call.message.chat.id, text=allinone)
          
          cur.execute('select status from ishchi_registration_info where id = %s', [str(call.from_user.id)])
          recordstatus = cur.fetchall()
          for rowstatus in recordstatus:
              status = rowstatus[0]
                
              if not status:
                  display_text_ish = "🔔 " + language[userlang]["Ishni_boshlash"]
                  display_text_break = "🔕 " + language[userlang]["Tanaffus_qilish"]
                  display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
                  reply_text = language[userlang]["Assalomu_alaykum_ishchi"]
                    
                  markup = types.InlineKeyboardMarkup()
                  markup.row_width = 1
                  markupib = types.InlineKeyboardButton(display_text_ish, callback_data='ishni_boshladik')
                  markupic = types.InlineKeyboardButton(display_text_break, callback_data='bandman')
                  markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
                  markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
                  markup.add(markupib, markupic, markupid, markupie)
                  bot.send_message(call.message.chat.id, reply_text, parse_mode="Markdown", reply_markup=markup)
                
              if status == "0":
                  display_text = "🔔 " + language[userlang]["Ishni_boshlash"]
                  call_data = "ishni_boshladik"
                  display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
                  reply_text = language[userlang]["Tanaffus_ishchi"]
                    
                  markup = types.InlineKeyboardMarkup()
                  markup.row_width = 1
                  markupib = types.InlineKeyboardButton(display_text, callback_data=call_data)
                  markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
                  markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
                  markup.add(markupib, markupid, markupie)
            
                  bot.send_message(call.message.chat.id, reply_text, parse_mode="Markdown", reply_markup=markup)
                
              if status == "1":
                  display_text = "🔕 " + language[userlang]["Tanaffus_qilish"]
                  call_data = "bandman"
                  display_bajargan_ishlarim = language[userlang]["Bajargan_ishlarim"]
                  reply_text = language[userlang]["Ishda_ishchi"]
              
                  markup = types.InlineKeyboardMarkup()
                  markup.row_width = 1
                  markupib = types.InlineKeyboardButton(display_text, callback_data=call_data)
                  markupid = types.InlineKeyboardButton(display_bajargan_ishlarim, callback_data='bajargan_ishlari')
                  markupie = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
                  markup.add(markupib, markupid, markupie)
        
                  bot.send_message(call.message.chat.id, reply_text, parse_mode="Markdown", reply_markup=markup)
                  
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Bajarilgan_ishlar"], parse_mode="Markdown", reply_markup=bajargan_ishlari(call))
      
    ###################
    #  END ISHCHI SIDE
    ###################
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ###################

    
    
      
    if call.data == "a":
      msgid = call.inline_message_id
      
      #cur.execute('SELECT COUNT(price) from file_info') #SELECT COUNT(column_name) FROM table_name WHERE condition;
      #record_num = cur.fetchall()
      #for num in record_num:
      #    number_of_rows = num[0] 
      
      #a = [number_of_rows]
      cur.execute('SELECT * from `file_info`')
      record = cur.fetchall()
      for row in record:
          markup = types.InlineKeyboardMarkup()
          markupib = types.InlineKeyboardButton(row[0],  callback_data='rrrrs', resize_keyboard=True)
          markupic = types.InlineKeyboardButton("🇱🇷 Products3", callback_data='rrrr')
          markup.add(markupic)
          message = bot.send_photo(chat_id=call.message.chat.id, photo=row[1], reply_markup=markup)
          #a[0] = message.message_id
          #cur.execute('SELECT MAX(orde) from message_id where user_id = %s', [str(call.from_user.id)])
          #record1 = cur.fetchall()
          #for row1 in record1:
          #    row2 = row1[0]
          #row2 = row2 + 1
          #cur.execute('INSERT INTO `message_id` (`user_id`, `orde`, `id`) VALUES (%s, %s, %s)', [str(call.from_user.id), row2, a[0]])
          #db.commit()
              

      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Please choose:", parse_mode="Markdown")
      
      
    if call.data == "rrrr":
      msgid = call.inline_message_id
      
      markup = types.InlineKeyboardMarkup()
      markup.row_width = 1
      markupii = types.InlineKeyboardButton("⚙️", callback_data='buyurtmanibekorqilish')
      markupij = types.InlineKeyboardButton("❔s", callback_data='help')
      markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
      markup.add(markupii, markupij, markupik)
      
      #bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=language[userlang]["Bekor_qilish_user"], parse_mode="Markdown", reply_markup=markup)
      image = open('qrcode.png', 'rb')
      bot.edit_message_media(media=types.InputMedia(type='photo', media=image), inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
      
    
    
    if call.data == "b":
      msgid = call.inline_message_id
      
      def pho(call):
          
          #cur.execute('SELECT COUNT(price) from file_info') #SELECT COUNT(column_name) FROM table_name WHERE condition;
          #record_num = cur.fetchall()
          #for num in record_num:
          #    number_of_rows = num[0] 
          
          #a = [number_of_rows]
          cur.execute('SELECT * from `file_info`')
          record = cur.fetchall()
          for row in record:
              markup = types.InlineKeyboardMarkup()
              markupib = types.InlineKeyboardButton(row[0],  callback_data='rasm5')
              markupic = types.InlineKeyboardButton("🇱🇷 Products3", callback_data='rasm5')
              markup.add(markupib, markupic)
              message = bot.send_photo(chat_id=call.message.chat.id, photo=row[1], reply_markup=markup)
              #a[0] = message.message_id
              #cur.execute('SELECT MAX(orde) from message_id where user_id = %s', [str(call.from_user.id)])
              #record1 = cur.fetchall()
              #for row1 in record1:
              #    row2 = row1[0]
              #row2 = row2 + 1
              #cur.execute('INSERT INTO `message_id` (`user_id`, `orde`, `id`) VALUES (%s, %s, %s)', [str(call.from_user.id), row2, a[0]])
              #db.commit()
              
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Please choose:", parse_mode="Markdown", reply_markup=pho(call))

      
    if call.data == "c":
      msgid = call.inline_message_id
      
      def pho2(call):
          bot.send_photo(chat_id=call.message.chat.id, photo='AgACAgEAAxkBAAID6F6pZ3yHy0z6fp3ZESiqrv_X8qIFAAJfqDEb3MpQReqdTBR8Yc9HdqUSMAAEAQADAgADdwADnEQAAhkE')
          bot.send_photo(chat_id=call.message.chat.id, photo='AgACAgEAAxkBAAID6F6pZ3yHy0z6fp3ZESiqrv_X8qIFAAJfqDEb3MpQReqdTBR8Yc9HdqUSMAAEAQADAgADdwADnEQAAhkE')
          bot.send_photo(chat_id=call.message.chat.id, photo='AgACAgEAAxkBAAIEF16pgoWuo4ScpanG5j7hvSPowxw7AAJ1qDEb0EdRRSuijHdh0tCg75sSMAAEAQADAgADdwADlkMAAhkE')
          bot.send_photo(chat_id=call.message.chat.id, photo='AgACAgEAAxkBAAIEGF6pgrd5E4lEiB6FNNL2YuFFR5DjAAJ1qDEb0EdRRSuijHdh0tCg75sSMAAEAQADAgADdwADlkMAAhkE')

      '''

      cur.execute('SELECT * from message_ id where orde = %s', [1])
      record = cur.fetchall()
        
      for row in record:
          orde = row[0]
      
      markup = types.InlineKeyboardMarkup()
      markupib = types.InlineKeyboardButton("🇱🇷 Products12", callback_data='rasm2')
      markup.add(markupib)
      '''
      
      image = open('qrcode.png', 'rb')
      bot.edit_message_media(media=types.InputMedia(type='photo', media=image), inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=pho2(call))
      
      
      
    ###################
    
    if call.data == "inlinehelp":
      bot.send_message(call.message.chat.id, language[userlang]["INLINE_HELP_MSG"], parse_mode="Markdown")
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
    if call.data == "showit":
      markup = types.ReplyKeyboardMarkup()
      numbers = list(range(3, 3000, 3))
      numbers = [0] + numbers
      cline = 0
      linelength = len(START_BUTTONS)
      try:
        while (cline < linelength):
          itembtn = []
          cfrom = numbers[cline]
          cto = numbers[cline + 1]
          cline = cline + 1
          while (cfrom < cto):
            itembtn.append(START_BUTTONS[cfrom])
            cfrom = cfrom + 1
            if len(itembtn) == 3:
              markup.row(*itembtn)
      except:
        lolalola = 0
      bot.send_message(call.message.chat.id, language[userlang]["SHOWED_BUTTONS_MSG"], reply_markup=markup, parse_mode="Markdown")
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
    if call.data.split("-")[0] == "sil":
      print("OMG")
      markup = types.ReplyKeyboardMarkup()
      inlineid = call.data.split("-")[1][-5:]
      if inlineid in querymessages:
        inline_text = querymessages(inlineid)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=inline_text)
        print("OMG1")
      else:
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Timeout exceeded.")
        print("OMG2")
  try:
    if call.data.split("|")[0] == "sil":
      markup = types.ReplyKeyboardMarkup()
      inlineid = call.data.split("|")[1]
      if inlineid in querymessages:
        inline_text = querymessages[inlineid]
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=inline_text)
      else:
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Timeout exceeded.")
        print("OMG2")
  except:
    print("EXC")
    pass
