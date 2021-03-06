# -*- coding: utf-8 -*-


START_BUTTONS = ("ā Id", "ā± Time", "š Memes", "š­ Send feedback", "š¤ Weather", "š„ Support", "š Link shortner", "āļø Calculate", "š§ Mp3Tag", "š” IP Geolocation", "ā»ļø QR Code", "šµ Exchange rate") # SPLITS 3 PER LINE

language = { "en" : {
"START_MSG" : "Hey! š \n \nWelcome to the *ZigZagBot*! š±š \nDeveloped by @WebShark25! \n \nAll bot commands: \nš¢ _/help_ - Get help message \nš¢ _/time <city>_ - Gets current time in any timezone! \nš¢ _/calc_ - Lets do some maths \nš¢ _/support_ - Chat with us! \nš¢ _/sendcontact_ - Forward contact to admin \nš¢ _Send feedback_ - Send feedback! \nš¢ _/echo <msg>_ - Echoes the message \nš¢ _/short <link>_ - Shorts the link! \nš¢ _/weather <city>_ - Gets weather! \nš¢ _/mp3tag <artist>||<title>_ - Edits audios tags! \nš¢ _/tocontact <phone>||<name>_ - Turns string to Telegram contact! \nš¢ _/qrcode <text>_ - QR Code creator!! \nš¢ _/ip <IP/Hostname>_ - Get IP location & more! \nš¢ _/rate <currency>_ - Get latest exchange rates! \nš¢ _/addcounter add_ - Add seen counter to your message! \nš¢ _/lmgtfy <text>_ - Let me google that for you! \nš¢ _/download <link>_ - Download a file and send it using telegram! \nš¢ _/addreply <syntax>_ - Learn the bot how to respond! \nš¢ _/id_ - Get your ID & Group's ID \n \n_More commands comming soon!_ \n \nI Hope you enjoy it! ",
"START_BUTTONS" : ("ā Id", "ā± Time", "š Memes", "š­ Send feedback", "š¤ Weather", "š„ Support", "š Link shortner", "āļø Calculate", "š§ Mp3Tag", "š” IP Geolocation", "ā»ļø QR Code", "šµ Exchange rate"),
"SHOWED_BUTTONS_MSG" : "Here you are ;)",
"TEST_MSG" : "This is a test message.",
"HELP" : "Help",
"CHANNEL" : "Channel",
"SETTINGS" : "Settings (Beta)",
"SHOW_ALL" : "Show all commands below keyboard",
"INLINE_HELP" : "Inline mode help",
"SHARE_CONTACT_MSG" : "Please share your contact to the bot (in a private message).",
"NO_ECHO_IN_SUPERGP_MSG" : "Unfortunately I wont reply to messages sent in a supergroup to prevent spamming.",
"ECHO_REPLY_MSG" : "Please enter a text so I reply to it!",
"ERROR_MSG" : "Error occured.",
"CONTACT_RECIEVED_MSG" : "New contact recieved:",
"CONTACT_FORWARDED_MSG" : "Contact successfully forwarded!",
"GP_GREETING_MSG" : "Hey *{0}*! \n \nWelcome to the group *{1}* š \n \n_Have fun & Enjoy!_",
"GP_FAREWELL_MSG" : "Oh no š \n*{0} left the group ā¹ļø",
"ID_MSG" : "š¢ Your name: *{0}* \nš¢ Your ID: *{1}* \n",
"INGP_ID_MSG" : "š¢ Group ID: *{2}* \n",
"CHATID_ID_MSG" : "š¢ Forwarded chat ID: *{}* \n",
"REPLIED_ID_MSG" : "š¢ Users ID: *{}* \n",
"FORWARDED_ID_MSG" : "š¢ Forwarded message sender's ID: *{}* \n",
"NON_ADMIN_ADDED_BOT_MSG" : "Im sorry ā¹ļø \nIm not authorized to join groups by normal members. \nOnly *admins* can add me to groups.",
"BOT_JOINED_MSG" : "Heyš§! I am here, At your service.",
"MESSANGER_JOIN_MSG" : "Now sending feedback. \nPlease enter your message!",
"MESSANGER_SUBMIT_MSG" : "OK. I got your message. Are you sure you want to send it?",
"MESSANGER_CANCEL_MSG" : "Canceled!",
"MESSANGER_LEAVE_MSG" : "Thanks for your feedback! Exiting.",
"WEBSHOT_CAPTION_MSG": "By the ZigZag bot",
"COMMAND_NOT_FOUND" : "Im sorry š¢ But the command you entered does not exists.",
"BANNED_MSG" : ":O You got banned from the bot!",
"UNBANNED_MSG" : "Welcome back! You are unbanned now ;)",
"GP_STATUS_MSG" : "ā”ļø All group messages: {0}",
"TIME_MSG" : "ā”ļø Date & Time: {0}",
"WAITING_APPROVAL_MESSENGER_MSG" : "ā”ļø Your request has been submitted! Please wait for manual approval.",
"ACCEPTED_MESSENGER_MSG" : "ā”ļø Your request has been approved! Now chatting with support.",
"DENIED_MESSENGER_MSG" : "ā”ļø Im sorry, But your request has been denied.",
"MESSAGE_SENT_MESSENGER_MSG" : "Message sent! Please wait for response",
"KICKED_MESSENGER_MSG" : "You got auto-kicked from the messenger because you spammed alot.",
"ALREADY_IN_MESSENGER_MSG" : "You are already chatting with support! to exit, type '/leave'",
"NOT_IN_MESSENGER_MSG" : "You are not chatting with support! to start, type '/support'",
"LEFT_MESSENGER_MSG" : "ā”ļø We hope you enjoyed ;) Leaving the messenger.",
"MEME_NEA_MSG" : "To use this command, you need to follow this format: \n`/meme <type>||<top>||<bottom>` \nFor example: `/meme Gangnam Style||Oppa||Gangnam style!`\n_Remember: No spaces within words and ||s!_ \n\nRemember, this bot supports more than a thousand of memes! Some examples: \n\nš¢ Good Guy Greg\nš¢ First World Problems\nš¢ Scumbag Steve\nš¢ Hipster Barista\nš¢ Bad Luck Brian\nš¢ Success Kid\nš¢ Ridiculously Photogenic Guy\nš¢ Sudden Clarity Clarence\nš¢ College Freshman\nš¢ Skeptical Baby\nš¢ Gangnam Style\nš¢ Talk To Spongebob\nš¢ Suspicious Cat",
"CALC_NEA_MSG" : "How can i calculate null? \nYour command should be like this: \n`/calc 5+5*2`",
"CHATTER_NEA_MSG" : "Hey! š± \n \nI think you don't know how to work with this. \n \nYou can actually learn me how to respond to some messages š \n \nSimply do: /addreply <Text>||<Response> \n \nFor example, if you want to enter 'hi' and then you want me to say 'hello', you need to execute this: \n /addreply Hi||Hello \n \nIts simple š And also fun š",
"CHATTER_INCORRECT_MSG" : "String recieved in an incorrect format..",
"CHATTER_ALREADYDEFINED_MSG" : "Im sorry, this message had already been defined!",
"CHATTER_DONE_MSG" : "Ooo yeah! Now I know if you say `{}`, I Should Answer `{}` :) \nCan you teach me *more*? šš",
"IP_ERROR_MSG" : "Error: \n\n`Invalid IP/Hostname`",
"IP_NEA_MSG" : "Please, enter an IP address or hostname. \n\nExample: `/ip 4.2.2.4`",
"IP_DONE_MSG" : "IP Information for *{}*: \n\nš Country: *{}* \nš« City: *{}* \nš” ISP: *{}* \nā± TimeZone: *{}*",
"MP3TAG_NEA_MSG" : "Please use correct syntax: \n`/mp3tag Artist||Title`\nAnd then, send the audio file.",
"MP3TAG_SENDAUDIO_MSG" : "Please send the audio now!",
"MP3COVER_NEA_MSG" : "Please reply to a photo to set it as an audios cover!",
"MP3COVER_REPLYTOPHOTO_MSG" : "Please reply to a photo, nothing else!",
"QRCODE_NEA_MSG" : "Please, enter a text so I can convert it to QR code. \n\nFor example: `/qrcode http://sadeco.ir`",
"SHORTNER_NEA_MSG" : "Please enter a link so I can short it. \nLike: `/short http://google.com`",
"TIME_NEA_MSG" : "Enter a time zone/city/region/etc. please! \n\nExample: `/time Tehran`",
"WWEATHER_NEA_MSG" : "Enter a city so I can tell its weather! :P \n\nExample: `/weather Tehran`",
"INLINE_HELP_MSG" : "*Inline mode help!:* \n \nTo use inline mode, first mention the bots ID (@TheZigZagBot) in your message, then use one of theese syntaxes: \n \nš¢echo <message> (_Echoes the message using HTML markup_) \nš¢cal <ex> (_Calculator.. Easy as a pie_) \nš¢time <city> (_Get time for anywhere! even nowhere!_) \nš¢lmgtfy <query> (_Let me google that for you!_) \nš¢weather <city> (_Current weather in <city>!_) \nš¢hideit <message> (_Hides the message you enter! :D So its un-forwardable._) \n \nExample: `@TheZigZagBot time tehran` \n\nMore options comming *soon*!",
"ADDCOUNTER_NEA_MSG" : "Do you want to know how many people saw your message? Yeah! Now its possible! \nJust type `/addcounter add` and then forward/send your message!",
"LMGTFY_NEA_MSG" : "Let me *Google* that for you! \n\nJust do `/lmgtfy <search>`",
"DOWNLOADER_NEA_MSG" : "Welcome to *ZigZag* downloader! \n\nYou can enter a *link* with a file size below *30MB*, and recieve that file in Telegram! \n\nPlease use this syntax: `/download http://example.com/file.zip` \n\nWarning: You have a limit of *3 files per minute*. Please dont exceed it.",
"DOWNLOADER_WAIT_MSG" : "Im sorry, but you can only have *1 concurrent download*.",
"DOWNLOADER_DL_MSG" : "Retrieving the file from server. Please wait...",
"DOWNLOADER_UP_MSG" : "Uploading the file for you. Please wait...",
"DOWNLOADER_OVERSIZE_MSG" : "The file was too *big*! Maximum file size should be *below 30MB*.",
"DOWNLOADER_ERROR_MSG" : "Im sorry, but an unknown error occured. \nPlease check the *file name* & *file size*, then try again.",
"SETTINGS_WLC_MSG" : "TheZigZag *Settings*! \nPlease, choose a _value_ to edit. \nć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°",
"SETTINGS_LANGUAGE_CHANGED_MSG" : "Success! Language has been updated. \nć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°",
"ADDCOUNTER_SENDNOW_MSG" : "Send your message now!",
"EXCHANGE_NEA_MSG" : "Enter a base currency! \n\nExample: `/rate USD` \n\nAvailable base currencies: `USD, EUR, RUB, AUD, CAD, GBP`",
"CHATBOT_IDK_MSG" : "I don't know how to reply to this š Teach me by executing /addreply š¶š",
"INLINE_ENTERTEXT_MSG" : "Please enter a text!",
"INLINE_SUCCESSECHO_MSG" : "Echo your message using HTML parse mode ;)",
"INLINE_ERRORECHO_MSG" : 'Error occured. One of your tags arent closed!',
"INLINE_CALC_MSG" : 'Please enter what you need I calculate.',
"INLINE_HIDEIT_MSG" : 'Please enter a text so I can hide it!',
"INLINE_WEATHER_MSG" : 'Please enter a city!',
"INLINE_SENDWEATHER_MSG" : 'Send current weather of ',
"INLINE_SENDTIME_MSG" : 'Please enter timezone/city/region/etc!',
"INLINE_TIMETIME_MSG" : 'Send current time in ',
"INLINE_LMGTFY_MSG": "Enter a text please!",
"INLINE_LMGTFYSEND_MSG" : "Send it!",
"GP_STATS_MSG" : "Group statistics by the *ZigZag Bot*! \n\nš¶ All messages: *{}*\nšø\nš¶ Sent voices: *{}*\nšø\nš¶ Sent audios: *{}*\nšø\nš¶ Sent photos: *{}*\nšø\nš¶ Sent files: *{}*\nšø\nš¶ Sent videos: *{}*\nšø\n",
"GP_NOTINGP_MSG" : "This statistics only works in groups & supergroups.",
"GP_RULES_NEA_MSG" : "Rules set to null! Please enter something :)",
"GP_RULESSET_MSG" : "Success! Group rules updated.",
"CAPTION_REPLYTOMSG_MSG" : "Please reply to a file!",
"CAPTION_NOCAPTION_MSG" : "Please enter a caption! \n/caption lablablab",
}, "fa" : {
"START_MSG" : "Ų³ŁŲ§Ł! š \n \nŲØŁ ŲØŲ§ŲŖ *Ų²ŪŚÆ Ų²Ų§ŚÆ* Ų®ŁŲ“ Ų¢ŁŲÆŪŲÆ š±š \nŲ³Ų§Ų®ŲŖŁ Ų“ŲÆŁ ŲŖŁŲ³Ų· @WebShark25! \n \nŚ©Ų§ŁŁŲÆ ŁŲ§Ū ŲØŲ§ŲŖ: \nš¢ _/help_ - ŲÆŲ±ŪŲ§ŁŲŖ Ų±Ų§ŁŁŁŲ§ \nš¢ _/time <city>_ - ŲÆŲ±ŪŲ§ŁŲŖ Ų²ŁŲ§Ł ŲØŁ ŁŁŲŖ ŁŲ±Ų¬Ų§ŪŪ! \nš¢ _/calc_ - ŁŲ§Ų“ŪŁ Ų­Ų³Ų§ŲØ! \nš¢ _/support_ - ŲØŲ§ ŁŲ§ ŲµŲ­ŲØŲŖ Ś©ŁŪŲÆ! \nš¢ _/sendcontact_ - ŁŁŲ±ŁŲ§Ų±ŲÆ Ś©Ų±ŲÆŁ Ś©Ų§ŁŲŖŚ©ŲŖ ŲØŁ Ų§ŲÆŁŪŁ \nš¢ _Send feedback_ - Ų§Ų±Ų³Ų§Ł ŁŲøŲ±! \nš¢ _/echo <msg>_ - ŲØŲ§Ų²ŚÆŲ±ŲÆŲ§ŁŲÆŁ Ł¾ŪŲ§Ł \nš¢ _/short <link>_ - Ś©ŁŲŖŲ§Ł Ś©Ų±ŲÆŁ ŁŪŁŚ©! \nš¢ _/weather <city>_ - ŲÆŲ±ŪŲ§ŁŲŖ Ų¢ŲØ Ł ŁŁŲ§! \nš¢ _/mp3tag <artist>||<title>_ - Ų§ŲÆŪŲŖ Ś©Ų±ŲÆŁ ŲŖŚÆ ŁŲ§Ū ŪŚ© Ų¢ŁŁŚÆ \nš¢ _/tocontact <phone>||<name>_ - ŲŖŲØŲÆŪŁ ŁŁŲ“ŲŖŁ ŲØŁ Ś©Ų§ŁŲŖŚ©ŲŖ ŲŖŁŚÆŲ±Ų§Ł \nš¢ _/qrcode <text>_ - Ų³Ų§Ų®ŲŖ Ś©ŲÆ Ś©ŪŁ Ų¢Ų±!! \nš¢ _/ip <IP/Hostname>_ - ŲÆŲ±ŪŲ§ŁŲŖ ŁŁŁŲ¹ŪŲŖ ŁŚ©Ų§ŁŪ ŪŚ© Ų¢ŪŁ¾Ū! \nš¢ _/rate <currency>_ - ŲÆŲ±ŪŲ§ŁŲŖ Ų¢Ų®Ų±ŪŁ ŁŲ±Ų® Ų§Ų±Ų² ŲÆŁŪŲ§! \nš¢ _/addcounter add_ - Ų§ŁŲ²ŁŲÆŁ ŲŖŲ¹ŲÆŲ§ŲÆ ŁŲ“Ų§ŁŲÆŁ ŲØŁ Ł¾ŪŲ§Ł Ų“ŁŲ§! \nš¢ _/lmgtfy <text>_ - ŲØŁ ŁŁ Ų§Ų¬Ų§Ų²Ł ŲØŲÆŁ Ų¢Ł Ų±Ų§ ŲØŲ±Ų§Ū ŲŖŁ ŚÆŁŚÆŁ Ś©ŁŁ! \nš¢ _/download <link>_ - ŁŪŁŚ© ŲÆŁŪŲÆ, ŁŲ§ŪŁ ŲÆŲ± ŲŖŁŚÆŲ±Ų§Ł ŲŖŲ­ŁŪŁ ŲØŚÆŪŲ±ŪŲÆ! \nš¢ _/addreply <syntax>_ - ŲØŁ ŲØŲ§ŲŖ Ų¢ŁŁŲ²Ų“ ŚŲŖ Ś©Ų±ŲÆŁ ŲÆŁŪŲÆ! \nš¢ _/id_ - ŲÆŲ±ŪŲ§ŁŲŖ Ų¢ŪŲÆŪ \n \n_ŁŲ±Ų±ŁŲ² ŲØŲ§ Ų¢Ł¾ŲÆŪŲŖ ŁŲ§Ū ŲØŪŲ“ŲŖŲ± ŲÆŲ± Ų®ŲÆŁŲŖ Ų“ŁŲ§ ŁŲ³ŲŖŪŁ!_ \n \nŲ§ŁŪŲÆŁŲ§Ų±ŪŁ Ś©Ł ŁŲ°ŲŖ ŲØŲØŲ±ŪŲÆ! ",
"START_BUTTONS" : ("ā Id", "ā± Time", "š Memes", "š­ Send feedback", "š¤ Weather", "š„ Support", "š Link shortner", "āļø Calculate", "š§ Mp3Tag", "š” IP Geolocation", "ā»ļø QR Code", "šµ Exchange rate"),
"SHOWED_BUTTONS_MSG" : "Ų®ŲÆŁŲŖ Ų“ŁŲ§ ;)",
"TEST_MSG" : "This is a test message.",
"HELP" : "Ų±Ų§ŁŁŁŲ§",
"CHANNEL" : "Ś©Ų§ŁŲ§Ł",
"SETTINGS" : "ŲŖŁŲøŪŁŲ§ŲŖ",
"SHOW_ALL" : "ŁŲ“Ų§ŁŲÆŁ ŲŖŁŲ§Ł ŲÆŲ³ŲŖŁŲ± ŁŲ§ (Ł¾Ų§ŪŪŁ Ś©ŪŲØŁŲ±ŲÆ)",
"INLINE_HELP" : "Ų±Ų§ŁŁŁŲ§Ū Ų§ŪŁŁŲ§ŪŁ",
"SHARE_CONTACT_MSG" : "ŁŲ·ŁŲ§ Ś©Ų§ŁŲŖŚ©ŲŖ Ų®ŁŲÆ Ų±Ų§ ŲØŲ±Ų§Ū ŲØŲ§ŲŖ Ų“ŪŲ± Ś©ŁŪŲÆ",
"NO_ECHO_IN_SUPERGP_MSG" : "ŁŲŖŲ§Ų³ŁŲ§ŁŁ, ŁŁ ŲÆŲ± Ų³ŁŁ¾Ų± ŚÆŲ±ŁŁ ŁŲ§ ŲØŲÆŁŪŁ Ų¬ŁŁŚÆŪŲ±Ū Ų§Ų² Ų§Ų³Ł¾Ł, Ł¾ŪŲ§Ł Ų±Ų§ ŲØŲ§Ų² ŁŁŪŚÆŲ±ŲÆŲ§ŁŁ",
"ECHO_REPLY_MSG" : "ŁŲ·ŁŲ§ ŪŁ Ł¾ŪŲ§Ł ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ ŲŖŲ§ ŁŁ Ų¢Ł Ų±Ų§ ŲØŲ§Ų²ŚÆŲ±ŲÆŲ§ŁŁ!",
"ERROR_MSG" : "ŁŲ“Ś©ŁŪ Ł¾ŪŲ“ Ų¢ŁŲÆ.",
"CONTACT_RECIEVED_MSG" : "New contact recieved:",
"CONTACT_FORWARDED_MSG" : "Ų“ŁŲ§Ų±Ł ŲŖŁŁŁ ŲØŲ§ ŁŁŁŁŪŲŖ ŁŁŲ±ŁŲ§Ų±ŲÆ Ų“ŲÆ",
"GP_GREETING_MSG" : "Hey *{0}*! \n \nWelcome to the group *{1}* š \n \n_Have fun & Enjoy!_",
"GP_FAREWELL_MSG" : "Oh no š \n*{0} left the group ā¹ļø",
"ID_MSG" : "š¢ ŁŲ§Ł Ų“ŁŲ§: *{0}* \nš¢ Ų¢ŪŲÆŪ Ų“ŁŲ§: *{1}* \n",
"INGP_ID_MSG" : "š¢ Ų¢ŪŲÆŪ ŚÆŲ±ŁŁ: *{2}* \n",
"CHATID_ID_MSG" : "š¢ Ų¢ŪŲÆŪ ŚŲŖŪ Ś©Ł Ł¾ŪŲ§Ł Ų§Ų² Ų¢Ł ŁŲ±ŁŲ§Ų±ŲÆ Ų“ŲÆŁ: *{}* \n",
"REPLIED_ID_MSG" : "š¢ Ų¢ŪŲÆŪ ŪŁŲ²Ų±: *{}* \n",
"FORWARDED_ID_MSG" : "š¢ Ų¢ŪŲÆŪ Ł¾ŪŲ§Ł ŁŁŲ±ŁŲ§Ų±ŲÆŲ“ŲÆŁ: *{}* \n",
"NON_ADMIN_ADDED_BOT_MSG" : "ŁŲŖŲ§Ų³ŁŁ ā¹ļø \nŁŁ Ų§Ų¬Ų§Ų²Ł Ų§ŁŲ²ŁŲÆŁ Ų“ŲÆŁ ŲÆŲ± ŚÆŲ±ŁŁ ŁŲ§Ū ŁŲ§Ų“ŁŲ§Ų®ŲŖŁ Ų±Ų§ ŁŲÆŲ§Ų±Ł \nŲŖŁŁŲ§ *Ų§ŲÆŁŪŁ ŁŁ* ŁŪŲŖŁŲ§ŁŲÆ ŁŁ Ų±Ų§ Ų§ŲÆŲÆ Ś©ŁŲÆ.",
"BOT_JOINED_MSG" : "ŁŪš§! ŁŁ Ų§ŪŁŲ¬Ų§Ł, ŲÆŲ±Ų®ŲÆŁŲŖ Ų“ŁŲ§",
"MESSANGER_JOIN_MSG" : "ŲÆŲ± Ų­Ų§Ł Ų§Ų±Ų³Ų§Ł ŁŲøŲ± \nŁŲ·ŁŲ§ ŁŲøŲ± Ų®ŁŲÆ Ų±Ų§ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ",
"MESSANGER_SUBMIT_MSG" : "Ų®ŪŁŪ Ų®ŲØ, Ł¾ŪŲ§Ł Ų“ŁŲ§ ŲÆŲ±ŪŲ§ŁŲŖ Ų“ŲÆ. \nŲ¢ŪŲ§ Ų§Ų² Ų§Ų±Ų³Ų§Ł Ų¢Ł Ų§Ų·ŁŪŁŲ§Ł ŲÆŲ§Ų±ŪŲÆŲ",
"MESSANGER_CANCEL_MSG" : "Ś©ŁŲ³Ł Ų“ŲÆ!",
"MESSANGER_LEAVE_MSG" : "ŲØŲ§ ŲŖŲ“Ś©Ų±, ŁŲøŲ± Ų§Ų±Ų³Ų§Ł Ų“ŲÆ!",
"WEBSHOT_CAPTION_MSG": "ŲŖŁŲ³Ų· ŲØŲ§ŲŖ Ų²ŪŚÆ Ų²Ų§ŚÆ",
"COMMAND_NOT_FOUND" : "ŁŁ ŁŲŖŲ§Ų³ŁŁ š¢ Ų§ŁŲ§ Ś©Ų§ŁŁŲÆŪ Ś©Ł ŁŲ§Ų±ŲÆ Ś©Ų±ŲÆŪ, ŁŲ¬ŁŲÆ Ų®Ų§Ų±Ų¬Ū ŁŲÆŲ§Ų±ŲÆ",
"BANNED_MSG" : "ŁŲ§Ū! Ų“ŁŲ§ Ų§Ų² ŲØŲ§ŲŖ ŲØŁŲ§Ś© Ų“ŲÆŪŲÆ!",
"UNBANNED_MSG" : "Ų®ŁŲ“ Ų¢ŁŲÆŪŲÆ! Ų¢Ł ŲØŁŲ§Ś© Ų“ŲÆŪŲÆ.",
"GP_STATUS_MSG" : "ā”ļø All group messages: {0}",
"TIME_MSG" : "ā”ļø Ų³Ų§Ų¹ŲŖ Ł ŲŖŲ§Ų±ŪŲ®: {0}",
"WAITING_APPROVAL_MESSENGER_MSG" : "ā”ļø ŲÆŲ±Ų®ŁŲ§Ų³ŲŖŲ“ŁŲ§ Ų«ŲØŲŖ Ų“ŲÆ! ŁŲ·ŁŲ§ ŲŖŲ§ ŲŖŲ§ŪŪŲÆ ŲŖŁŲ³Ų· Ų§ŲÆŁŪŁ ŲµŲØŲØŲ± Ś©ŁŪŲÆ",
"ACCEPTED_MESSENGER_MSG" : "ā”ļø ŲÆŲ±Ų®ŁŲ§Ų³ŲŖ Ų“ŁŲ§ ŁŲØŁŁ Ų“ŲÆ! ŁŁ Ų§Ś©ŁŁŁ Ł¾ŪŲ§Ł ŁŲ§Ū Ų“ŁŲ§ ŲØŲ±Ų§Ū ŲŖŪŁ Ł¾Ų“ŲŖŪŲØŲ§ŁŪ Ų§Ų±Ų³Ų§Ł ŁŪŲ“ŁŲÆ",
"DENIED_MESSENGER_MSG" : "ā”ļø ŁŲŖŲ§Ų³ŁŁ, Ų§ŁŲ§ ŲÆŲ±Ų®ŁŲ§Ų³ŲŖ Ų“ŁŲ§ Ų±ŲÆ Ų“ŲÆ",
"MESSAGE_SENT_MESSENGER_MSG" : "Ł¾ŪŲ§Ł Ų§Ų±Ų³Ų§Ł Ų“ŲÆ! ŁŲ·ŁŲ§ ŲµŲØŁŲ± ŲØŲ§Ų“ŪŲÆ",
"KICKED_MESSENGER_MSG" : "ŲØŲÆŁŪŁ Ų§Ų³Ł¾Ł Ų²ŪŲ§ŲÆ, ŲØŲµŁŲ±ŲŖ Ų®ŁŲÆŚ©Ų§Ų± Ų§Ų² ŚŲŖ Ų§Ų®Ų±Ų§Ų¬ Ų“ŲÆŪŲÆ",
"ALREADY_IN_MESSENGER_MSG" : "Ų“ŁŲ§ ŁŁ Ų§Ś©ŁŁŁ ŲÆŲ± Ų­Ų§Ł ŚŲŖ ŲØŲ§ Ł¾Ų“ŲŖŪŲØŲ§ŁŪ ŁŲ³ŲŖŪŲÆ! \nŲ¬ŁŲŖ Ų®Ų±ŁŲ¬: /leave",
"NOT_IN_MESSENGER_MSG" : "Ų“ŁŲ§ ŲØŲ§ Ł¾Ų“ŲŖŪŲØŲ§ŁŪ ŚŲŖ ŁŁŪŚ©ŁŪŲÆ! Ų¬ŁŲŖ Ų¢ŲŗŲ§Ų²: '/support'",
"LEFT_MESSENGER_MSG" : "ā”ļø Ų§ŁŪŲÆŁŲ§Ų±ŪŁ Ś©Ł ŁŲ°ŲŖ Ś©Ų§ŁŪ Ų±Ų§ ŲØŲ±ŲÆŁ ŲØŲ§Ų“ŪŲÆ :) ŲØŲ§ ŲŖŲ“Ś©Ų± Ų§Ų² ŲŖŁŲ§Ų³ Ų“ŁŲ§",
"MEME_NEA_MSG" : "Ų¬ŁŲŖ Ų§Ų³ŲŖŁŲ§ŲÆŁ Ų§Ų² Ų§ŪŁ Ś©Ų§ŁŁŲÆ, Ų“ŁŲ§ ŲØŲ§ŪŲÆ ŁŲ§ŁŁŲÆ Ų²ŪŲ± Ų¹ŁŁ Ś©ŁŪŲÆ \n`/meme <type>||<top>||<bottom>` \nŲØŲ±Ų§Ū ŁŲ«Ų§Ł: `/meme Gangnam Style||Oppa||Gangnam style!`\n_Ł¾Ū ŁŁŲ“ŲŖ: ŲØŪŁ || ŁŲ§ ŁŲ§ŲµŁŁ ŁŚÆŲ°Ų§Ų±ŲÆ!!_ \n\nŁ¾Ū ŁŁŲ“ŲŖ 2: Ų§ŪŁ ŲØŲ§ŲŖ ŲØŪŲ“ŲŖŲ± Ų§Ų² 1000 ŁŁŲ¹ Ų¹Ś©Ų³ Ų±Ų§ Ł¾Ų“ŲŖŪŲØŲ§ŁŪ ŁŪŚ©ŁŲÆ! ŲØŲ±Ų§Ū ŁŲ«Ų§Ł: \n\nš¢ Good Guy Greg\nš¢ First World Problems\nš¢ Scumbag Steve\nš¢ Hipster Barista\nš¢ Bad Luck Brian\nš¢ Success Kid\nš¢ Ridiculously Photogenic Guy\nš¢ Sudden Clarity Clarence\nš¢ College Freshman\nš¢ Skeptical Baby\nš¢ Gangnam Style\nš¢ Talk To Spongebob\nš¢ Suspicious Cat",
"CALC_NEA_MSG" : "ŁŲ·ŁŲ§ ŪŚ© ŁŁŲÆŲ§Ų± Ų¹ŲÆŲÆŪ ŁŲ§Ų±ŪŲÆ Ś©ŁŪŲÆ. \nŲØŲ±Ų§Ū ŁŲ«Ų§Ł: \n`/calc 5+5*2`",
"CHATTER_NEA_MSG" : "ŁŚ©Ų± Ś©ŁŁ ŁŁŪŲÆŁŁŪ ŚŲ¬ŁŲ±Ū ŲØŲ§ Ų§ŪŁ ŁŲ³ŁŲŖ Ś©Ų§Ų± Ś©ŁŪ, ŲÆŲ±Ų³ŲŖŁŲ \n \nŁŪŲŖŁŁŪ ŲØŁ ŁŁ Ų­Ų±Ł Ų²ŲÆŁ ŪŲ§ŲÆ ŲØŲÆŪ š \n \nŲ®ŪŁŪ Ų±Ų§Ų­ŲŖ: /addreply <Ł¾ŪŲ§Ł>||<Ų¬ŁŲ§ŲØ> \n \nŲØŲ±Ų§Ū ŁŲ«Ų§Ł, Ų§ŚÆŁ ŁŪŲ®ŁŲ§Ū ŲŖŁ ŲØŚÆŪ hi Ł ŁŁ Ų¬ŁŲ§ŲØ ŲØŲÆŁ hello, ŲØŲ§ŪŲÆ ŚŁŪŁ ŚŪŲ²Ū Ų±Ł ŲØŲ²ŁŪ \n /addreply Hi||Hello \n \nŲ®ŪŁŪ Ų¢Ų³ŁŁ š Ł Ś©Ų§Ų±ŲØŲ±ŲÆŪ š",
"CHATTER_INCORRECT_MSG" : "ŚŪŲ²Ū Ś©Ł ŁŁŲ“ŲŖŪ ŲØŲ±Ų§Ū ŁŁ ŁŲ§ ŁŁŁŁŁ ŲØŁŲÆ!",
"CHATTER_ALREADYDEFINED_MSG" : "ŁŲŖŲ§Ų³ŁŲ§ŁŁ, ŚŪŲ²Ū Ś©Ł ŁŲ§Ų±ŲÆ Ś©Ų±ŲÆŪŲÆ ŁŲØŁŲ§ Ų«ŲØŲŖ Ų“ŲÆŁ!",
"CHATTER_DONE_MSG" : "ŁŁŲ±Ų§! Ų­Ų§ŁŲ§ ŁŪŲÆŁŁŁ Ų§ŚÆŁ ŲØŚÆŪ `{}`, ŲØŲ§ŪŲÆ Ų¬ŁŲ§ŲØ ŲØŲÆŁ `{}` Ų§\nŁŪŲŖŁŁŪ ŲØŪŲ“ŲŖŲ± ŪŲ§ŲÆŁ ŲØŲÆŪŲ šš",
"IP_ERROR_MSG" : "ŁŲ“Ś©ŁŪ Ł¾ŪŲ“ Ų¢ŁŲÆ: \n\n`Ų¢ŪŁ¾Ū Ų§Ų“ŲŖŲØŲ§Ł`",
"IP_NEA_MSG" : "ŁŲ·ŁŲ§, ŪŚ© Ų¢ŲÆŲ±Ų³ Ų§ŪŁ¾Ū ŪŲ§ Ų§ŲÆŲ±Ų³ Ų³Ų§ŪŲŖ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ \n\nŁŲ«Ų§Ł: `/ip 4.2.2.4`",
"IP_DONE_MSG" : "ŁŲ“Ų®ŲµŲ§ŲŖ Ų¢ŪŁ¾Ū *{}*: \n\nš Ś©Ų“ŁŲ±: *{}* \nš« Ų“ŁŲ±: *{}* \nš” Ų³Ų±ŁŪŲ³ ŲÆŁŁŲÆŁ: *{}* \nā± ŁŁŁŲ¹ŪŲŖ Ų²ŁŲ§ŁŪ: *{}*",
"MP3TAG_NEA_MSG" : "ŁŲ·ŁŲ§ ŁŁŲÆŲ§Ų± Ų±Ų§ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ: \n`/mp3tag Artist||Title`\nŁ ŲÆŲ± Ł¾ŪŲ§Ł ŲØŲ¹ŲÆ, Ų¢ŁŁŚÆ Ų±Ų§ Ų§Ų±Ų³Ų§Ł Ś©ŁŪŲÆ",
"MP3TAG_SENDAUDIO_MSG" : "Ų®ŲØ, Ų­Ų§ŁŲ§ Ų¢ŁŁŚÆ Ų±Ł Ų§Ų±Ų³Ų§Ł Ś©Ł!",
"MP3COVER_NEA_MSG" : "ŁŲ·ŁŲ§, Ų§ŪŁ ŲÆŲ³ŲŖŁŲ± Ų±Ł ŲÆŲ± Ų±ŪŁ¾ŁŲ§Ū ŲØŁ Ų¹Ś©Ų³Ū Ś©Ł ŁŪŲ®ŁŲ§ŁŪŲÆ ŲØŲ±Ų±ŁŪ ŲŖŲ±Ś© Ų³ŲŖ Ų“ŁŲÆ, Ų§Ų±Ų³Ų§Ł Ś©ŁŪŲÆ",
"MP3COVER_REPLYTOPHOTO_MSG" : "ŁŲ·ŁŲ§ ŲØŁ ŪŚ© Ų¹Ś©Ų³ Ų±ŪŁ¾ŁŲ§Ū Ś©ŁŪŲÆ.",
"QRCODE_NEA_MSG" : "ŁŲ·ŁŲ§, ŪŚ© ŁŪŁŚ© ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ ŲŖŲ§ Ų¢Ł Ų±Ų§ ŲŖŲØŲÆŪŁ ŲØŁ Ś©ŪŁ Ų¢Ų± Ś©ŲÆ ŲØŚ©ŁŁ. \n\nŁŲ«Ų§Ł: `/qrcode http://sadeco.ir`",
"SHORTNER_NEA_MSG" : "ŁŲ·ŁŲ§ ŪŚ© ŁŪŁŚ© ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ ŲŖŲ§ Ų¢Ł Ų±Ų§ Ś©ŁŲŖŲ§Ł Ś©ŁŁ! \nŁŲ«ŁŲ§: `/short http://google.com`",
"TIME_NEA_MSG" : "ŁŲ·ŁŲ§ ŪŚ© ŁŁŁŲ¹ŪŲŖ Ų²ŁŲ§ŁŪ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ! \n\nŁŲ«Ł: `/time Tehran`",
"WWEATHER_NEA_MSG" : "ŁŲ§Ł ŪŚ© Ų“ŁŲ± Ų±Ų§ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ ŲŖŲ§ ŁŲ¶Ų¹ŪŲŖ Ų¢ŲØ Ł ŁŁŲ§Ū Ų¢ŁŲ±Ų§ ŲØŚÆŁŪŁ! :P \n\nŁŲ«Ų§Ł: `/weather Tehran`",
"INLINE_HELP_MSG" : "*Ų±Ų§ŁŁŁŲ§Ū Ų§ŪŁŁŲ§ŪŁ!:* \n \nŲ¬ŁŲŖ Ų§Ų³ŲŖŁŲ§ŲÆŁ Ų§Ų² Ų­Ų§ŁŲŖ Ų§ŪŁ ŁŲ§ŪŁ, Ų§ŲØŲŖŲÆŲ§ Ų¢ŪŲÆŪ ŲØŲ§ŲŖ Ų±Ų§ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ (@TheZigZagBot) Ł Ų³Ł¾Ų³ ŪŚ©Ū Ų§Ų² ŁŁŲ§ŲÆŪŲ± Ų²ŪŲ± Ų±Ų§ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ: \n \nš¢echo <message> (_ŲØŲ§Ų²ŚÆŲ±ŲÆŲ§ŁŲÆŁ Ł¾ŪŲ§Ł_) \nš¢cal <ex> (_ŁŲ§Ų“ŪŁ Ų­Ų³Ų§ŲØ... Ų®ŪŁŪ Ų³Ų§ŲÆŁ_) \nš¢lmgtfy <query> (_ŲØŲ²Ų§Ų± ŁŁ ŲØŲ±Ų§ŲŖ ŚÆŁŚÆŁŲ“ Ś©ŁŁ!_) \nš¢time <city> (_ŲÆŲ±ŪŲ§ŁŲŖ Ų²ŁŲ§Ł ŲØŁ ŁŁŲŖ ŁŲ±Ų¬Ų§!_) \nš¢weather <city> (_ŲÆŲ±ŪŲ§ŁŲŖ Ų¢ŲØ Ł ŁŁŲ§Ū ŁŲ± Ų“ŁŲ±!_) \nš¢hideit <message> (_ŁŲ®ŁŪ Ś©Ų±ŲÆŁ Ł¾ŪŲ§Ł! Ś©Ł ŁŲ§ŲØŁ ŁŁŲ±ŁŲ§Ų±ŲÆ ŁŲØŲ§Ų“ŲÆ._) \n \nŁŲ«Ų§Ł: `@TheZigZagBot time tehran` \n\nŲ¢Ł¾Ų“Ł ŁŲ§Ū ŲØŪŲ“ŲŖŲ±, ŲØŲ²ŁŲÆŪ ŲÆŲ± Ų²ŪŚÆ Ų²Ų§ŚÆ!",
"ADDCOUNTER_NEA_MSG" : "ŲÆŁŲ³ŲŖ ŲÆŲ§Ų±Ū ŲØŲÆŁŁŪ ŚŁŲÆ ŁŁŲ± Ł¾ŪŲ§ŁŲŖŁ ŲÆŪŲÆŁŲ Ų§Ų±Ł! Ų®ŪŁŪ Ų³Ų§ŲÆŲ³ŲŖ!\nŁŁŲ· ŲØŁŁŪŲ³ `/addcounter add` Ł ŲØŲ¹ŲÆ Ł¾ŪŲ§ŁŲŖŁ Ų§Ų±Ų³Ų§Ł Ś©Ł",
"LMGTFY_NEA_MSG" : "ŲØŲ²Ų§Ų± ŁŁ ŲØŲ±Ų§Ū ŲŖŁ ŚÆŁŚÆŁ Ś©ŁŁŲ“! \n\nŲ®ŪŁŪ Ų±Ų§Ų­ŲŖŁ: `/lmgtfy <search>`",
"DOWNLOADER_NEA_MSG" : "ŲØŁ ŲÆŲ§ŁŁŁŁŲÆŲ± Ų²ŪŚÆ Ų²Ų§ŚÆ Ų®ŁŲ“ Ų¢ŁŲÆŪŲÆ \n\nŁŪŲŖŁŁŪ ŪŁ ŁŪŁŚ© ŁŲ§Ų±ŲÆ Ś©ŁŪ, Ł ŁŲ§ŪŁŲ“ Ų±Ł ŲÆŲ± ŲŖŁŚÆŲ±Ų§Ł ŲØŚÆŪŲ±Ū! \n\nŁŲ«Ł Ų§ŪŁ: `/download http://example.com/file.zip` \n\nŲŖŁŲ¬Ł: ŁŁŲ· ŁŪŲŖŁŁŪ 3 ŁŲ§ŪŁ ŲÆŲ± ŲÆŁŪŁŁ ŲÆŲ§ŁŁŁŲÆ Ś©ŁŪ.",
"DOWNLOADER_WAIT_MSG" : "ŁŲŖŲ§Ų³ŁŁ, Ų§ŁŲ§ ŁŁŲ· ŁŪŲŖŁŁŪ ŪŚ© ŲÆŲ§ŁŁŁŲÆ ŁŁŲ²ŁŲ§Ł ŲÆŲ§Ų“ŲŖŁ ŲØŲ§Ų“Ū",
"DOWNLOADER_DL_MSG" : "ŲÆŲ± Ų­Ų§Ł ŲÆŲ±ŪŲ§ŁŲŖ ŁŲ§ŪŁ Ų§Ų² Ų³Ų±ŁŲ±...",
"DOWNLOADER_UP_MSG" : "ŲÆŲ± Ų­Ų§Ł Ų§Ų±Ų³Ų§Ł ŁŲ§ŪŁ ŲØŲ±Ų§Ū Ų“ŁŲ§...",
"DOWNLOADER_OVERSIZE_MSG" : "ŁŲ§ŪŁ Ų®ŪŁŪ ŲØŲ²Ų±ŚÆ ŲØŁŲÆ! Ų­ŲÆŲ§Ś©Ų«Ų± Ų³Ų§ŪŲ² ŁŲ§ŲØŁ ŁŲØŁŁ 30 ŁŚÆŲ§ŲØŲ§ŪŲŖ ŁŲ³ŲŖ",
"DOWNLOADER_ERROR_MSG" : "ŁŲŖŲ§Ų³ŁŁ, Ų§ŁŲ§ ŪŁ ŁŲ“Ś©Ł ŁŲ§Ų“ŁŲ§Ų®ŲŖŁ Ł¾ŪŲ“ Ų§ŁŁŲÆ! \nŲ“Ų§ŪŲÆ Ų³Ų§ŪŲ² ŁŲ§ŪŁ Ų²ŪŲ§ŲÆŪ ŲØŲ²Ų±ŚÆŁ, Ų“Ų§ŪŲÆŁ ŁŲ“Ś©Ł ŁŲ§Ū ŲÆŪŚÆŁ.",
"SETTINGS_WLC_MSG" : "ŲŖŁŲøŪŁŲ§ŲŖ Ų²ŪŚÆ Ų²Ų§ŚÆ! ŁŲ·ŁŲ§ ŪŚ© ŚÆŲ²ŪŁŁ Ų±Ų§ Ų§ŁŲŖŲ®Ų§ŲØ Ś©ŁŪŲÆ \nć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°",
"SETTINGS_LANGUAGE_CHANGED_MSG" : "Ų¹ŁŁŪŲ§ŲŖ ŁŁŁŁŪŲŖ Ų¢ŁŪŲ² ŲØŁŲÆ! Ų²ŲØŲ§Ł ŲØŁ Ų±ŁŲ² Ų“ŲÆ \nć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°",
"ADDCOUNTER_SENDNOW_MSG" : "ŁŲ·ŁŲ§ Ł¾ŪŲ§Ł Ų®ŁŲÆ Ų±Ų§ Ų§Ų±Ų³Ų§Ł Ś©ŁŪŲÆ!",
"EXCHANGE_NEA_MSG" : "ŁŲ·ŁŲ§ ŪŚ© Ų§Ų±Ų² Ų±Ų§ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ! \n\nŲØŲ±Ų§Ū ŁŲ«Ų§Ł: `/rate USD` \n\nŲ§Ų±Ų² ŁŲ§Ū ŁŁŲ¬ŁŲÆ: `USD, EUR, RUB, AUD, CAD, GBP`",
"CHATBOT_IDK_MSG" : "ŁŁ ŲØŁŲÆ ŁŪŲ³ŲŖŁ ŚŲ¬ŁŲ±Ū ŲØŁ Ų§ŪŁ Ų¬ŁŲ§ŲØ ŲØŲÆŁ š ŁŁŪ ŁŪŲŖŁŁŪ ŲØŁŁ ŪŲ§ŲÆ ŲØŲÆŪ!: /addreply š¶š",
"INLINE_ENTERTEXT_MSG" : "ŁŲ·ŁŲ§ ŪŚ© Ł¾ŪŲ§Ł ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ",
"INLINE_SUCCESSECHO_MSG" : "Ų§Ų±Ų³Ų§Ł Ł¾ŪŲ§Ł ŲØŲ§ Ų§Ų³ŲŖŁŲ§ŲÆŁ Ų§Ų² ŲŖŚÆ ŁŲ§Ū Ų§Ś ŲŖŪ Ų§Ł Ų§Ł",
"INLINE_ERRORECHO_MSG" : 'ŁŲ“Ś©ŁŪ Ł¾ŪŲ“ Ų¢ŁŲÆ. ŪŚ©Ū Ų§Ų² ŲŖŚÆ ŁŲ§ ŲØŲ³ŲŖŁ ŁŲ“ŲÆŁ Ų§ŁŲÆ!',
"INLINE_CALC_MSG" : 'ŁŲ·ŁŲ§ ŪŚ© Ų¹ŁŁŪŲ§ŲŖ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ',
"INLINE_HIDEIT_MSG" : 'ŁŲ·ŁŲ§ Ł¾ŪŲ§ŁŪ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ ŲŖŲ§ Ų¢Ł Ų±Ų§ ŁŲ®ŁŪ Ś©ŁŁ!',
"INLINE_WEATHER_MSG" : 'ŁŲ·ŁŲ§ ŁŲ§Ł ŪŚ© Ų“ŁŲ± Ų±Ų§ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ!',
"INLINE_SENDWEATHER_MSG" : 'Ų§Ų±Ų³Ų§Ł ŁŲ¶Ų¹ŪŲŖ Ų¢ŲØ Ł ŁŁŲ§Ū ',
"INLINE_SENDTIME_MSG" : 'ŁŲ·ŁŲ§ ŪŚ© Ų“ŁŲ±/ŁŁŁŲ¹ŪŲŖ Ų²ŁŲ§ŁŪ/ŁŲ­ŁŁ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ!',
"INLINE_TIMETIME_MSG" : 'Ų§Ų±Ų³Ų§Ł ŲŖŲ§Ų±ŪŲ® Ł Ų³Ų§Ų¹ŲŖ ',
"INLINE_LMGTFY_MSG": " ŁŲ·ŁŲ§ ŪŚ© ŚŪŲ²Ū ŁŲ§Ų±ŲÆ Ś©Ł ŲØŲ±Ų§Ł!",
"INLINE_LMGTFYSEND_MSG" : "Ų§Ų±Ų³Ų§Ł!",
"GP_STATS_MSG" : "Ų¢ŁŲ§Ų± ŚÆŲ±ŁŁ ŲØŲ§ ŲØŲ§ŲŖ *Ų²ŪŚÆ Ų²Ų§ŚÆ*! \n\nš¶ ŲŖŁŲ§ŁŪ Ł¾ŪŲ§Ł ŁŲ§: *{}*\nšø\nš¶ ŁŁŪŲ³ ŁŲ§: *{}*\nšø\nš¶ Ų¢ŁŁŚÆ ŁŲ§: *{}*\nšø\nš¶ Ų¹Ś©Ų³ ŁŲ§: *{}*\nšø\nš¶ ŁŲ§ŪŁ ŁŲ§: *{}*\nšø\nš¶ ŁŪŁŁ ŁŲ§: *{}*\nšø\n",
"GP_NOTINGP_MSG" : "Ų§ŪŁ Ų¢ŁŲ§Ų±, ŁŁŲ· ŲÆŲ± ŚÆŲ±ŁŁ ŁŲ§ Ś©Ų§Ų± ŁŪŚ©ŁŲÆ.",
"GP_RULES_NEA_MSG" : "ŁŲ·ŁŲ§, ŁŲŖŁ ŁŁŲ§ŁŪŁ Ų±Ų§ ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ!",
"GP_RULESSET_MSG" : "Ų¹ŁŁŪŲ§ŲŖ ŁŁŁŁŪŲŖ Ų¢ŁŪŲ² ŲØŁŲÆ! ŁŁŲ§ŁŪŁ ŚÆŲ±ŁŁ Ų³ŲŖ Ų“ŲÆ.",
"CAPTION_REPLYTOMSG_MSG" : "ŁŲ·ŁŲ§ Ų§ŪŁ ŲÆŲ³ŲŖŁŲ± Ų±Ų§ ŲÆŲ± Ų±ŪŁ¾ŁŲ§Ū ŲØŁ ŪŚ© ŁŲ§ŪŁ Ų§Ų±Ų³Ų§Ł Ś©ŁŪŲÆ!",
"CAPTION_NOCAPTION_MSG" : "ŁŲ·ŁŲ§ ŪŚ© Ś©Ł¾Ų“Ł ŁŲ§Ų±ŲÆ Ś©ŁŪŲÆ! \n/caption lablablab",
}
}
