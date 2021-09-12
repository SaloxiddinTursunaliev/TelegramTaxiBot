# -*- coding: utf-8 -*-
# -*- coding: cp1251_general_ci -*-
    ###################
    #  USER SIDE
    ###################
from telebot import types
@bot.message_handler(commands=['contact'])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="number", request_contact=True)
    button_geo = types.KeyboardButton(text="location", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "send number", reply_markup=keyboard)
    
@bot.message_handler (content_types = ['contact'])
def contact (message):
    if message.contact is not None:
        print(message.contact)
        print(message.contact.phone_number)
        print(message.contact.first_name)
        print(message.contact.last_name)
        print(message.contact.user_id)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    cur.execute('SELECT id from ishchi_registration_info where id = %s', [str(message.from_user.id)])
    recorduserreg = cur.fetchall()
    if not recorduserreg:
        cur.execute('SELECT * from language where id = %s', [str(message.from_user.id)])
        recordlang = cur.fetchall()
        if not recordlang:
            cur.execute('INSERT INTO `message_id` (`user_id`, `orde`, `id`) VALUES (%s, %s, %s)', [str(message.from_user.id), 0, "0"])
            db.commit()
            cur.execute('INSERT INTO `buyurtma` (`id`, `orde`, `car`) VALUES (%s, %s, %s)', [str(message.from_user.id), 0, "0"])
            db.commit()
            cur.execute('INSERT INTO `callback_message_id` (`userid`, `orde`, `messageid`) VALUES (%s, %s, %s)', [str(message.from_user.id), 0, "0"])
            db.commit()
            
            markup = types.InlineKeyboardMarkup()
            markup.row_width = 1
            cur.execute('SELECT * from language_list where status=%s', [1])
            recordlanglist = cur.fetchall()
            for rowlanglist in recordlanglist:
                markup1 = types.InlineKeyboardButton(rowlanglist[0], callback_data = rowlanglist[1])
                markup.add(markup1)
            
            if message.chat.type == "private":
                bot.reply_to(message, "Tilni tanlang!🇺🇿\nВыберите язык!🇷🇺", reply_markup=markup, parse_mode="Markdown")
            else:
                bot.reply_to(message, "Tilni tanlang!🇺🇿\nВыберите язык!🇷🇺", parse_mode="Markdown")
            
        for row in recordlang:
            userid = row[0]
            userlang = row[1]
                
            Register_user = language[userlang]["Register_user"]
                
            markup = types.InlineKeyboardMarkup()
            markup.row_width = 1
            markupia = types.InlineKeyboardButton(Register_user, callback_data='registration_user')
            markupib = types.InlineKeyboardButton("⚙️", callback_data='settingsmainuser')
            markup.add(markupia, markupib)
            
            if message.chat.type == "private":
                bot.reply_to(message, language[userlang]["Not_in_list_ishchi"], reply_markup=markup, parse_mode="Markdown")
            else:
                bot.reply_to(message, language[userlang]["Not_in_list_ishchi"], parse_mode="Markdown")
                    
                    
    for row1 in recorduserreg:
        user_reg_id = row1[0]
            
        cur.execute('SELECT * from language where id = %s', [str(message.from_user.id)])
        record = cur.fetchall()
        for row in record:
            userid = row[0]
            userlang = row[1]
            
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
            
        if len(message.text.split()) > 1:
            if message.text.replace("/start ","",1) == "inlinem":
                bot.send_message(message.chat.id, language[userlang]["INLINE_HELP_MSG"], parse_mode="Markdown")
                return
            







#@bot.message_handler(commands=['start', 'help'])
#def send_welcome(message):
    #cur.execute('SELECT * from language where id = %s', [str(message.from_user.id)])
    #record = cur.fetchall()
    #if not record:
        #cur.execute('INSERT INTO `message_id` (`user_id`, `orde`, `id`) VALUES (%s, %s, %s)', [str(message.from_user.id), 0, "0"])
        #db.commit()
        #cur.execute('INSERT INTO `buyurtma` (`id`, `orde`, `car`) VALUES (%s, %s, %s)', [str(message.from_user.id), 0, "0"])
        #db.commit()
        #cur.execute('INSERT INTO `callback_message_id` (`userid`, `orde`, `messageid`) VALUES (%s, %s, %s)', [str(message.from_user.id), 0, "0"])
        #db.commit()
        #markup = types.InlineKeyboardMarkup()
        #markupib = types.InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data='settingslangen')
        #markupic = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='settingslangfa')
        #markup.add(markupib,markupic)
        
        #if message.chat.type == "private":
            #bot.reply_to(message, "Tilni tanlang!🇺🇿\nВыберите язык!🇷🇺", reply_markup=markup, parse_mode="Markdown")
        #else:
            #bot.reply_to(message, "Tilni tanlang!🇺🇿\nВыберите язык!🇷🇺", parse_mode="Markdown")
        
        
    #for row in record:
        #userid = row[0]
        #userlang = row[1]
            
        #if len(message.text.split()) > 1:
            #if message.text.replace("/start ","",1) == "inlinem":
                #bot.send_message(message.chat.id, language[userlang]["INLINE_HELP_MSG"], parse_mode="Markdown")
                #return
        #'''
        #markup = types.InlineKeyboardMarkup()
        #markupib = types.InlineKeyboardButton(language[userlang]["HELP"], callback_data='rasm')
        #markupic = types.InlineKeyboardButton(language[userlang]["CHANNEL"], url=CHANNEL_LINK)
        #markup.add(markupib,markupic)
        #markupif = types.InlineKeyboardButton(language[userlang]["SETTINGS"], callback_data='settingsmain')
        #markup.add(markupif)
        #markupid = types.InlineKeyboardButton(language[userlang]["SHOW_ALL"], callback_data='showit')
        #markup.add(markupid)
        #markupie = types.InlineKeyboardButton(language[userlang]["INLINE_HELP"], callback_data='inlinehelp')
        #markup.add(markupie)
        #'''
        
        #'''
        #markup = types.InlineKeyboardMarkup()
        #markup.row_width = 1
        #markupi0 = types.InlineKeyboardButton("Taxi", callback_data='Taxi')
        #markupia = types.InlineKeyboardButton("Labo", callback_data='Labo')
        #markupib = types.InlineKeyboardButton("Motoroller", callback_data='Motoroller')
        #markupic = types.InlineKeyboardButton("Munis", callback_data='Munis')
        #markupid = types.InlineKeyboardButton("Kamaz", callback_data='Kamaz')
        #markupie = types.InlineKeyboardButton("Zil", callback_data='Zil')
        #markupif = types.InlineKeyboardButton("Traktor", callback_data='Traktor')
        #markupig = types.InlineKeyboardButton("Moskvich", callback_data='Moskvich')
        #markupih = types.InlineKeyboardButton("Jiguli", callback_data='Jiguli')
        #markup.add(markupi0, markupia, markupib, markupic, markupid, markupie, markupif, markupig, markupih)
        #markup.row_width = 3
        #markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
        #markupij = types.InlineKeyboardButton("❔", callback_data='help')
        #markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
        #markup.add(markupii, markupij, markupik)
        
        
        #markup = types.InlineKeyboardMarkup()
        #markup.row_width = 1
        #cur.execute('SELECT * from main where status=%s', [1])
        #record13 = cur.fetchall()
        #for row13 in record13:
            #if userlang == "en":
                #markup1 = types.InlineKeyboardButton(row13[0], callback_data = row13[0])
                #markup.add(markup1)
            #if userlang == "fa":
                #markup1 = types.InlineKeyboardButton(row13[1], callback_data = row13[1])
                #markup.add(markup1)
        #'''
        
        #markup = types.InlineKeyboardMarkup()
        #markup.row_width = 1
        #cur.execute('SELECT * from main_menu where language=%s and status=%s', [userlang, 1])
        #record13 = cur.fetchall()
        #for row13 in record13:
            #markup1 = types.InlineKeyboardButton(row13[0], callback_data = row13[0])
            #markup.add(markup1)
            
        #markup.row_width = 3
        #markupii = types.InlineKeyboardButton("⚙️", callback_data='settingsmain')
        #markupij = types.InlineKeyboardButton("❔", callback_data='help')
        #markupik = types.InlineKeyboardButton("🌦", callback_data='weather')
        #markup.add(markupii, markupij, markupik)
        
        
        #if message.chat.type == "private":
            #bot.send_message(message.chat.id, language[userlang]["Assalomu_alaykum_user"], reply_markup=markup, parse_mode="Markdown")
        #else:
            #bot.reply_to(message, language[userlang]["Assalomu_alaykum_user"], parse_mode="Markdown")
    
    ###################
    #  END USER SIDE
    ###################
            
    ###################
    #  ISHCHI SIDE
    ###################

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'ishchi' or message.text.lower() == 'Ishchi':
        cur.execute('SELECT id from ishchi_registration_info where id = %s', [str(message.from_user.id)])
        record1 = cur.fetchall()
        if not record1:
            cur.execute('SELECT * from language where id = %s', [str(message.from_user.id)])
            record = cur.fetchall()
            if not record:
                cur.execute('INSERT INTO `message_id` (`user_id`, `orde`, `id`) VALUES (%s, %s, %s)', [str(message.from_user.id), 0, "0"])
                db.commit()
                cur.execute('INSERT INTO `buyurtma` (`id`, `orde`, `car`) VALUES (%s, %s, %s)', [str(message.from_user.id), 0, "0"])
                db.commit()
                cur.execute('INSERT INTO `callback_message_id` (`userid`, `orde`, `messageid`) VALUES (%s, %s, %s)', [str(message.from_user.id), 0, "0"])
                db.commit()
                markup = types.InlineKeyboardMarkup()
                markupib = types.InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data='settingslangenishchi')
                markupic = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='settingslangfaishchi')
                markup.add(markupib,markupic)
        
                if message.chat.type == "private":
                    bot.reply_to(message, "Tilni tanlang!🇺🇿\nВыберите язык!🇷🇺", reply_markup=markup, parse_mode="Markdown")
                else:
                    bot.reply_to(message, "Tilni tanlang!🇺🇿\nВыберите язык!🇷🇺", parse_mode="Markdown")
            
            for row in record:
                userid = row[0]
                userlang = row[1]
                
                Register_ishchi = language[userlang]["Register_ishchi"]
                
                markup = types.InlineKeyboardMarkup()
                markup.row_width = 1
                markupia = types.InlineKeyboardButton(Register_ishchi, callback_data='registration')
                markupib = types.InlineKeyboardButton("⚙️", callback_data='settingsmainishchi')
                markup.add(markupia, markupib)
            
                if message.chat.type == "private":
                    bot.reply_to(message, language[userlang]["Not_in_list_ishchi"], reply_markup=markup, parse_mode="Markdown")
                else:
                    bot.reply_to(message, language[userlang]["Not_in_list_ishchi"], parse_mode="Markdown")
                    
                    
        for row1 in record1:
            user_reg_id = row1[0]
            
            cur.execute('SELECT * from language where id = %s', [str(message.from_user.id)])
            record = cur.fetchall()
            for row in record:
                userid = row[0]
                userlang = row[1]
            
            if len(message.text.split()) > 1:
                if message.text.replace("/start ","",1) == "inlinem":
                    bot.send_message(message.chat.id, language[userlang]["INLINE_HELP_MSG"], parse_mode="Markdown")
                    return
            
            cur.execute('select status from ishchi_registration_info where id = %s', [str(message.from_user.id)])
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
                    bot.send_message(message.chat.id, reply_text, parse_mode="Markdown", reply_markup=markup)
                
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
            
                    bot.send_message(message.chat.id, reply_text, parse_mode="Markdown", reply_markup=markup)
                
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
            
                    bot.send_message(message.chat.id, reply_text, parse_mode="Markdown", reply_markup=markup)
                    
                
    elif message.text.lower() == 'milelc1997':
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        markupi0 = types.InlineKeyboardButton("Start/Stop", callback_data='Startstopsms')
        markup.add(markupi0)
        bot.send_message(message.from_user.id, 'Choose:', parse_mode="Markdown", reply_markup=markup)




    
    ###################
    #  END ISHCHI SIDE
    ###################
    
