# -*- coding: utf-8 -*-


START_BUTTONS = ("❓ Id", "⏱ Time", "🙈 Memes", "🎭 Send feedback", "🌤 Weather", "👥 Support", "🔗 Link shortner", "✒️ Calculate", "🎧 Mp3Tag", "📡 IP Geolocation", "◻️ QR Code", "💵 Exchange rate") # SPLITS 3 PER LINE

language = { "en" : {
"START_MSG" : "Hey! 😊 \n \nWelcome to the *ZigZagBot*! 😱🚀 \nDeveloped by @WebShark25! \n \nAll bot commands: \n💢 _/help_ - Get help message \n💢 _/time <city>_ - Gets current time in any timezone! \n💢 _/calc_ - Lets do some maths \n💢 _/support_ - Chat with us! \n💢 _/sendcontact_ - Forward contact to admin \n💢 _Send feedback_ - Send feedback! \n💢 _/echo <msg>_ - Echoes the message \n💢 _/short <link>_ - Shorts the link! \n💢 _/weather <city>_ - Gets weather! \n💢 _/mp3tag <artist>||<title>_ - Edits audios tags! \n💢 _/tocontact <phone>||<name>_ - Turns string to Telegram contact! \n💢 _/qrcode <text>_ - QR Code creator!! \n💢 _/ip <IP/Hostname>_ - Get IP location & more! \n💢 _/rate <currency>_ - Get latest exchange rates! \n💢 _/addcounter add_ - Add seen counter to your message! \n💢 _/lmgtfy <text>_ - Let me google that for you! \n💢 _/download <link>_ - Download a file and send it using telegram! \n💢 _/addreply <syntax>_ - Learn the bot how to respond! \n💢 _/id_ - Get your ID & Group's ID \n \n_More commands comming soon!_ \n \nI Hope you enjoy it! ",
"START_BUTTONS" : ("❓ Id", "⏱ Time", "🙈 Memes", "🎭 Send feedback", "🌤 Weather", "👥 Support", "🔗 Link shortner", "✒️ Calculate", "🎧 Mp3Tag", "📡 IP Geolocation", "◻️ QR Code", "💵 Exchange rate"),
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
"GP_GREETING_MSG" : "Hey *{0}*! \n \nWelcome to the group *{1}* 😊 \n \n_Have fun & Enjoy!_",
"GP_FAREWELL_MSG" : "Oh no 😕 \n*{0} left the group ☹️",
"ID_MSG" : "💢 Your name: *{0}* \n💢 Your ID: *{1}* \n",
"INGP_ID_MSG" : "💢 Group ID: *{2}* \n",
"CHATID_ID_MSG" : "💢 Forwarded chat ID: *{}* \n",
"REPLIED_ID_MSG" : "💢 Users ID: *{}* \n",
"FORWARDED_ID_MSG" : "💢 Forwarded message sender's ID: *{}* \n",
"NON_ADMIN_ADDED_BOT_MSG" : "Im sorry ☹️ \nIm not authorized to join groups by normal members. \nOnly *admins* can add me to groups.",
"BOT_JOINED_MSG" : "Hey😧! I am here, At your service.",
"MESSANGER_JOIN_MSG" : "Now sending feedback. \nPlease enter your message!",
"MESSANGER_SUBMIT_MSG" : "OK. I got your message. Are you sure you want to send it?",
"MESSANGER_CANCEL_MSG" : "Canceled!",
"MESSANGER_LEAVE_MSG" : "Thanks for your feedback! Exiting.",
"WEBSHOT_CAPTION_MSG": "By the ZigZag bot",
"COMMAND_NOT_FOUND" : "Im sorry 😢 But the command you entered does not exists.",
"BANNED_MSG" : ":O You got banned from the bot!",
"UNBANNED_MSG" : "Welcome back! You are unbanned now ;)",
"GP_STATUS_MSG" : "⚡️ All group messages: {0}",
"TIME_MSG" : "⚡️ Date & Time: {0}",
"WAITING_APPROVAL_MESSENGER_MSG" : "⚡️ Your request has been submitted! Please wait for manual approval.",
"ACCEPTED_MESSENGER_MSG" : "⚡️ Your request has been approved! Now chatting with support.",
"DENIED_MESSENGER_MSG" : "⚡️ Im sorry, But your request has been denied.",
"MESSAGE_SENT_MESSENGER_MSG" : "Message sent! Please wait for response",
"KICKED_MESSENGER_MSG" : "You got auto-kicked from the messenger because you spammed alot.",
"ALREADY_IN_MESSENGER_MSG" : "You are already chatting with support! to exit, type '/leave'",
"NOT_IN_MESSENGER_MSG" : "You are not chatting with support! to start, type '/support'",
"LEFT_MESSENGER_MSG" : "⚡️ We hope you enjoyed ;) Leaving the messenger.",
"MEME_NEA_MSG" : "To use this command, you need to follow this format: \n`/meme <type>||<top>||<bottom>` \nFor example: `/meme Gangnam Style||Oppa||Gangnam style!`\n_Remember: No spaces within words and ||s!_ \n\nRemember, this bot supports more than a thousand of memes! Some examples: \n\n💢 Good Guy Greg\n💢 First World Problems\n💢 Scumbag Steve\n💢 Hipster Barista\n💢 Bad Luck Brian\n💢 Success Kid\n💢 Ridiculously Photogenic Guy\n💢 Sudden Clarity Clarence\n💢 College Freshman\n💢 Skeptical Baby\n💢 Gangnam Style\n💢 Talk To Spongebob\n💢 Suspicious Cat",
"CALC_NEA_MSG" : "How can i calculate null? \nYour command should be like this: \n`/calc 5+5*2`",
"CHATTER_NEA_MSG" : "Hey! 😱 \n \nI think you don't know how to work with this. \n \nYou can actually learn me how to respond to some messages 😏 \n \nSimply do: /addreply <Text>||<Response> \n \nFor example, if you want to enter 'hi' and then you want me to say 'hello', you need to execute this: \n /addreply Hi||Hello \n \nIts simple 😌 And also fun 😍",
"CHATTER_INCORRECT_MSG" : "String recieved in an incorrect format..",
"CHATTER_ALREADYDEFINED_MSG" : "Im sorry, this message had already been defined!",
"CHATTER_DONE_MSG" : "Ooo yeah! Now I know if you say `{}`, I Should Answer `{}` :) \nCan you teach me *more*? 😁😁",
"IP_ERROR_MSG" : "Error: \n\n`Invalid IP/Hostname`",
"IP_NEA_MSG" : "Please, enter an IP address or hostname. \n\nExample: `/ip 4.2.2.4`",
"IP_DONE_MSG" : "IP Information for *{}*: \n\n🌍 Country: *{}* \n🏫 City: *{}* \n📡 ISP: *{}* \n⏱ TimeZone: *{}*",
"MP3TAG_NEA_MSG" : "Please use correct syntax: \n`/mp3tag Artist||Title`\nAnd then, send the audio file.",
"MP3TAG_SENDAUDIO_MSG" : "Please send the audio now!",
"MP3COVER_NEA_MSG" : "Please reply to a photo to set it as an audios cover!",
"MP3COVER_REPLYTOPHOTO_MSG" : "Please reply to a photo, nothing else!",
"QRCODE_NEA_MSG" : "Please, enter a text so I can convert it to QR code. \n\nFor example: `/qrcode http://sadeco.ir`",
"SHORTNER_NEA_MSG" : "Please enter a link so I can short it. \nLike: `/short http://google.com`",
"TIME_NEA_MSG" : "Enter a time zone/city/region/etc. please! \n\nExample: `/time Tehran`",
"WWEATHER_NEA_MSG" : "Enter a city so I can tell its weather! :P \n\nExample: `/weather Tehran`",
"INLINE_HELP_MSG" : "*Inline mode help!:* \n \nTo use inline mode, first mention the bots ID (@TheZigZagBot) in your message, then use one of theese syntaxes: \n \n💢echo <message> (_Echoes the message using HTML markup_) \n💢cal <ex> (_Calculator.. Easy as a pie_) \n💢time <city> (_Get time for anywhere! even nowhere!_) \n💢lmgtfy <query> (_Let me google that for you!_) \n💢weather <city> (_Current weather in <city>!_) \n💢hideit <message> (_Hides the message you enter! :D So its un-forwardable._) \n \nExample: `@TheZigZagBot time tehran` \n\nMore options comming *soon*!",
"ADDCOUNTER_NEA_MSG" : "Do you want to know how many people saw your message? Yeah! Now its possible! \nJust type `/addcounter add` and then forward/send your message!",
"LMGTFY_NEA_MSG" : "Let me *Google* that for you! \n\nJust do `/lmgtfy <search>`",
"DOWNLOADER_NEA_MSG" : "Welcome to *ZigZag* downloader! \n\nYou can enter a *link* with a file size below *30MB*, and recieve that file in Telegram! \n\nPlease use this syntax: `/download http://example.com/file.zip` \n\nWarning: You have a limit of *3 files per minute*. Please dont exceed it.",
"DOWNLOADER_WAIT_MSG" : "Im sorry, but you can only have *1 concurrent download*.",
"DOWNLOADER_DL_MSG" : "Retrieving the file from server. Please wait...",
"DOWNLOADER_UP_MSG" : "Uploading the file for you. Please wait...",
"DOWNLOADER_OVERSIZE_MSG" : "The file was too *big*! Maximum file size should be *below 30MB*.",
"DOWNLOADER_ERROR_MSG" : "Im sorry, but an unknown error occured. \nPlease check the *file name* & *file size*, then try again.",
"SETTINGS_WLC_MSG" : "TheZigZag *Settings*! \nPlease, choose a _value_ to edit. \n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰",
"SETTINGS_LANGUAGE_CHANGED_MSG" : "Success! Language has been updated. \n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰",
"ADDCOUNTER_SENDNOW_MSG" : "Send your message now!",
"EXCHANGE_NEA_MSG" : "Enter a base currency! \n\nExample: `/rate USD` \n\nAvailable base currencies: `USD, EUR, RUB, AUD, CAD, GBP`",
"CHATBOT_IDK_MSG" : "I don't know how to reply to this 🙁 Teach me by executing /addreply 😶😄",
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
"GP_STATS_MSG" : "Group statistics by the *ZigZag Bot*! \n\n🔶 All messages: *{}*\n🔸\n🔶 Sent voices: *{}*\n🔸\n🔶 Sent audios: *{}*\n🔸\n🔶 Sent photos: *{}*\n🔸\n🔶 Sent files: *{}*\n🔸\n🔶 Sent videos: *{}*\n🔸\n",
"GP_NOTINGP_MSG" : "This statistics only works in groups & supergroups.",
"GP_RULES_NEA_MSG" : "Rules set to null! Please enter something :)",
"GP_RULESSET_MSG" : "Success! Group rules updated.",
"CAPTION_REPLYTOMSG_MSG" : "Please reply to a file!",
"CAPTION_NOCAPTION_MSG" : "Please enter a caption! \n/caption lablablab",
}, "fa" : {
"START_MSG" : "سلام! 😊 \n \nبه بات *زیگ زاگ* خوش آمدید 😱🚀 \nساخته شده توسط @WebShark25! \n \nکامند های بات: \n💢 _/help_ - دریافت راهنما \n💢 _/time <city>_ - دریافت زمان به وقت هرجایی! \n💢 _/calc_ - ماشین حساب! \n💢 _/support_ - با ما صحبت کنید! \n💢 _/sendcontact_ - فوروارد کردن کانتکت به ادمین \n💢 _Send feedback_ - ارسال نظر! \n💢 _/echo <msg>_ - بازگرداندن پیام \n💢 _/short <link>_ - کوتاه کردن لینک! \n💢 _/weather <city>_ - دریافت آب و هوا! \n💢 _/mp3tag <artist>||<title>_ - ادیت کردن تگ های یک آهنگ \n💢 _/tocontact <phone>||<name>_ - تبدیل نوشته به کانتکت تلگرام \n💢 _/qrcode <text>_ - ساخت کد کیو آر!! \n💢 _/ip <IP/Hostname>_ - دریافت موقعیت مکانی یک آیپی! \n💢 _/rate <currency>_ - دریافت آخرین نرخ ارز دنیا! \n💢 _/addcounter add_ - افزودن تعداد مشاهده به پیام شما! \n💢 _/lmgtfy <text>_ - به من اجازه بده آن را برای تو گوگل کنم! \n💢 _/download <link>_ - لینک دهید, فایل در تلگرام تحویل بگیرید! \n💢 _/addreply <syntax>_ - به بات آموزش چت کردن دهید! \n💢 _/id_ - دریافت آیدی \n \n_هرروز با آپدیت های بیشتر در خدمت شما هستیم!_ \n \nامیدواریم که لذت ببرید! ",
"START_BUTTONS" : ("❓ Id", "⏱ Time", "🙈 Memes", "🎭 Send feedback", "🌤 Weather", "👥 Support", "🔗 Link shortner", "✒️ Calculate", "🎧 Mp3Tag", "📡 IP Geolocation", "◻️ QR Code", "💵 Exchange rate"),
"SHOWED_BUTTONS_MSG" : "خدمت شما ;)",
"TEST_MSG" : "This is a test message.",
"HELP" : "راهنما",
"CHANNEL" : "کانال",
"SETTINGS" : "تنظیمات",
"SHOW_ALL" : "مشاهده تمام دستور ها (پایین کیبورد)",
"INLINE_HELP" : "راهنمای اینلاین",
"SHARE_CONTACT_MSG" : "لطفا کانتکت خود را برای بات شیر کنید",
"NO_ECHO_IN_SUPERGP_MSG" : "متاسفانه, من در سوپر گروه ها بدلیل جلوگیری از اسپم, پیام را باز نمیگردانم",
"ECHO_REPLY_MSG" : "لطفا یه پیام وارد کنید تا من آن را بازگردانم!",
"ERROR_MSG" : "مشکلی پیش آمد.",
"CONTACT_RECIEVED_MSG" : "New contact recieved:",
"CONTACT_FORWARDED_MSG" : "شماره تلفن با موفقیت فوروارد شد",
"GP_GREETING_MSG" : "Hey *{0}*! \n \nWelcome to the group *{1}* 😊 \n \n_Have fun & Enjoy!_",
"GP_FAREWELL_MSG" : "Oh no 😕 \n*{0} left the group ☹️",
"ID_MSG" : "💢 نام شما: *{0}* \n💢 آیدی شما: *{1}* \n",
"INGP_ID_MSG" : "💢 آیدی گروه: *{2}* \n",
"CHATID_ID_MSG" : "💢 آیدی چتی که پیام از آن فروارد شده: *{}* \n",
"REPLIED_ID_MSG" : "💢 آیدی یوزر: *{}* \n",
"FORWARDED_ID_MSG" : "💢 آیدی پیام فورواردشده: *{}* \n",
"NON_ADMIN_ADDED_BOT_MSG" : "متاسفم ☹️ \nمن اجازه افزوده شدن در گروه های ناشناخته را ندارم \nتنها *ادمین من* میتواند من را ادد کند.",
"BOT_JOINED_MSG" : "هی😧! من اینجام, درخدمت شما",
"MESSANGER_JOIN_MSG" : "در حال ارسال نظر \nلطفا نظر خود را وارد کنید",
"MESSANGER_SUBMIT_MSG" : "خیلی خب, پیام شما دریافت شد. \nآیا از ارسال آن اطمینان دارید؟",
"MESSANGER_CANCEL_MSG" : "کنسل شد!",
"MESSANGER_LEAVE_MSG" : "با تشکر, نظر ارسال شد!",
"WEBSHOT_CAPTION_MSG": "توسط بات زیگ زاگ",
"COMMAND_NOT_FOUND" : "من متاسفم 😢 اما کامندی که وارد کردی, وجود خارجی ندارد",
"BANNED_MSG" : "وای! شما از بات بلاک شدید!",
"UNBANNED_MSG" : "خوش آمدید! آن بلاک شدید.",
"GP_STATUS_MSG" : "⚡️ All group messages: {0}",
"TIME_MSG" : "⚡️ ساعت و تاریخ: {0}",
"WAITING_APPROVAL_MESSENGER_MSG" : "⚡️ درخواستشما ثبت شد! لطفا تا تایید توسط ادمین صببر کنید",
"ACCEPTED_MESSENGER_MSG" : "⚡️ درخواست شما قبول شد! هم اکنون پیام های شما برای تیم پشتیبانی ارسال میشود",
"DENIED_MESSENGER_MSG" : "⚡️ متاسفم, اما درخواست شما رد شد",
"MESSAGE_SENT_MESSENGER_MSG" : "پیام ارسال شد! لطفا صبور باشید",
"KICKED_MESSENGER_MSG" : "بدلیل اسپم زیاد, بصورت خودکار از چت اخراج شدید",
"ALREADY_IN_MESSENGER_MSG" : "شما هم اکنون در حال چت با پشتیبانی هستید! \nجهت خروج: /leave",
"NOT_IN_MESSENGER_MSG" : "شما با پشتیبانی چت نمیکنید! جهت آغاز: '/support'",
"LEFT_MESSENGER_MSG" : "⚡️ امیدواریم که لذت کافی را برده باشید :) با تشکر از تماس شما",
"MEME_NEA_MSG" : "جهت استفاده از این کامند, شما باید مانند زیر عمل کنید \n`/meme <type>||<top>||<bottom>` \nبرای مثال: `/meme Gangnam Style||Oppa||Gangnam style!`\n_پی نوشت: بین || ها فاصله نگذارد!!_ \n\nپی نوشت 2: این بات بیشتر از 1000 نوع عکس را پشتیبانی میکند! برای مثال: \n\n💢 Good Guy Greg\n💢 First World Problems\n💢 Scumbag Steve\n💢 Hipster Barista\n💢 Bad Luck Brian\n💢 Success Kid\n💢 Ridiculously Photogenic Guy\n💢 Sudden Clarity Clarence\n💢 College Freshman\n💢 Skeptical Baby\n💢 Gangnam Style\n💢 Talk To Spongebob\n💢 Suspicious Cat",
"CALC_NEA_MSG" : "لطفا یک مقدار عددی وارید کنید. \nبرای مثال: \n`/calc 5+5*2`",
"CHATTER_NEA_MSG" : "فکر کنم نمیدونی چجوری با این قسمت کار کنی, درسته؟ \n \nمیتونی به من حرف زدن یاد بدی 😏 \n \nخیلی راحت: /addreply <پیام>||<جواب> \n \nبرای مثال, اگه میخوای تو بگی hi و من جواب بدم hello, باید چنین چیزی رو بزنی \n /addreply Hi||Hello \n \nخیلی آسون 😌 و کاربردی 😍",
"CHATTER_INCORRECT_MSG" : "چیزی که نوشتی برای من نا مفهوم بود!",
"CHATTER_ALREADYDEFINED_MSG" : "متاسفانه, چیزی که وارد کردید قبلا ثبت شده!",
"CHATTER_DONE_MSG" : "هورا! حالا میدونم اگه بگی `{}`, باید جواب بدم `{}` ا\nمیتونی بیشتر یادم بدی؟ 😁😁",
"IP_ERROR_MSG" : "مشکلی پیش آمد: \n\n`آیپی اشتباه`",
"IP_NEA_MSG" : "لطفا, یک آدرس ایپی یا ادرس سایت وارد کنید \n\nمثال: `/ip 4.2.2.4`",
"IP_DONE_MSG" : "مشخصات آیپی *{}*: \n\n🌍 کشور: *{}* \n🏫 شهر: *{}* \n📡 سرویس دهنده: *{}* \n⏱ موقعیت زمانی: *{}*",
"MP3TAG_NEA_MSG" : "لطفا مقدار را وارد کنید: \n`/mp3tag Artist||Title`\nو در پیام بعد, آهنگ را ارسال کنید",
"MP3TAG_SENDAUDIO_MSG" : "خب, حالا آهنگ رو ارسال کن!",
"MP3COVER_NEA_MSG" : "لطفا, این دستور رو در ریپلای به عکسی که میخواهید برروی ترک ست شود, ارسال کنید",
"MP3COVER_REPLYTOPHOTO_MSG" : "لطفا به یک عکس ریپلای کنید.",
"QRCODE_NEA_MSG" : "لطفا, یک لینک وارد کنید تا آن را تبدیل به کیو آر کد بکنم. \n\nمثال: `/qrcode http://sadeco.ir`",
"SHORTNER_NEA_MSG" : "لطفا یک لینک وارد کنید تا آن را کوتاه کنم! \nمثلا: `/short http://google.com`",
"TIME_NEA_MSG" : "لطفا یک موقعیت زمانی وارد کنید! \n\nمثل: `/time Tehran`",
"WWEATHER_NEA_MSG" : "نام یک شهر را وارد کنید تا وضعیت آب و هوای آنرا بگویم! :P \n\nمثال: `/weather Tehran`",
"INLINE_HELP_MSG" : "*راهنمای اینلاین!:* \n \nجهت استفاده از حالت این لاین, ابتدا آیدی بات را وارد کنید (@TheZigZagBot) و سپس یکی از مقادیر زیر را وارد کنید: \n \n💢echo <message> (_بازگرداندن پیام_) \n💢cal <ex> (_ماشین حساب... خیلی ساده_) \n💢lmgtfy <query> (_بزار من برات گوگلش کنم!_) \n💢time <city> (_دریافت زمان به وقت هرجا!_) \n💢weather <city> (_دریافت آب و هوای هر شهر!_) \n💢hideit <message> (_مخفی کردن پیام! که قابل فوروارد نباشد._) \n \nمثال: `@TheZigZagBot time tehran` \n\nآپشن های بیشتر, بزودی در زیگ زاگ!",
"ADDCOUNTER_NEA_MSG" : "دوست داری بدونی چند نفر پیامتو دیدن؟ اره! خیلی سادست!\nفقط بنویس `/addcounter add` و بعد پیامتو ارسال کن",
"LMGTFY_NEA_MSG" : "بزار من برای تو گوگل کنمش! \n\nخیلی راحته: `/lmgtfy <search>`",
"DOWNLOADER_NEA_MSG" : "به داونلودر زیگ زاگ خوش آمدید \n\nمیتونی یه لینک وارد کنی, و فایلش رو در تلگرام بگیری! \n\nمثل این: `/download http://example.com/file.zip` \n\nتوجه: فقط میتونی 3 فایل در دقیقه دانلود کنی.",
"DOWNLOADER_WAIT_MSG" : "متاسفم, اما فقط میتونی یک دانلود همزمان داشته باشی",
"DOWNLOADER_DL_MSG" : "در حال دریافت فایل از سرور...",
"DOWNLOADER_UP_MSG" : "در حال ارسال فایل برای شما...",
"DOWNLOADER_OVERSIZE_MSG" : "فایل خیلی بزرگ بود! حداکثر سایز قابل قبول 30 مگابایت هست",
"DOWNLOADER_ERROR_MSG" : "متاسفم, اما یه مشکل ناشناخته پیش اومد! \nشاید سایز فایل زیادی بزرگه, شایدم مشکل های دیگه.",
"SETTINGS_WLC_MSG" : "تنظیمات زیگ زاگ! لطفا یک گزینه را انتخاب کنید \n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰",
"SETTINGS_LANGUAGE_CHANGED_MSG" : "عملیات موفقیت آمیز بود! زبان به روز شد \n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰",
"ADDCOUNTER_SENDNOW_MSG" : "لطفا پیام خود را ارسال کنید!",
"EXCHANGE_NEA_MSG" : "لطفا یک ارز را وارد کنید! \n\nبرای مثال: `/rate USD` \n\nارز های موجود: `USD, EUR, RUB, AUD, CAD, GBP`",
"CHATBOT_IDK_MSG" : "من بلد نیستم چجوری به این جواب بدم 🙁 ولی میتونی بهم یاد بدی!: /addreply 😶😄",
"INLINE_ENTERTEXT_MSG" : "لطفا یک پیام وارد کنید",
"INLINE_SUCCESSECHO_MSG" : "ارسال پیام با استفاده از تگ های اچ تی ام ال",
"INLINE_ERRORECHO_MSG" : 'مشکلی پیش آمد. یکی از تگ ها بسته نشده اند!',
"INLINE_CALC_MSG" : 'لطفا یک عملیات وارد کنید',
"INLINE_HIDEIT_MSG" : 'لطفا پیامی وارد کنید تا آن را مخفی کنم!',
"INLINE_WEATHER_MSG" : 'لطفا نام یک شهر را وارد کنید!',
"INLINE_SENDWEATHER_MSG" : 'ارسال وضعیت آب و هوای ',
"INLINE_SENDTIME_MSG" : 'لطفا یک شهر/موقعیت زمانی/محله وارد کنید!',
"INLINE_TIMETIME_MSG" : 'ارسال تاریخ و ساعت ',
"INLINE_LMGTFY_MSG": " لطفا یک چیزی وارد کن برام!",
"INLINE_LMGTFYSEND_MSG" : "ارسال!",
"GP_STATS_MSG" : "آمار گروه با بات *زیگ زاگ*! \n\n🔶 تمامی پیام ها: *{}*\n🔸\n🔶 وویس ها: *{}*\n🔸\n🔶 آهنگ ها: *{}*\n🔸\n🔶 عکس ها: *{}*\n🔸\n🔶 فایل ها: *{}*\n🔸\n🔶 فیلم ها: *{}*\n🔸\n",
"GP_NOTINGP_MSG" : "این آمار, فقط در گروه ها کار میکند.",
"GP_RULES_NEA_MSG" : "لطفا, متن قوانین را وارد کنید!",
"GP_RULESSET_MSG" : "عملیات موفقیت آمیز بود! قوانین گروه ست شد.",
"CAPTION_REPLYTOMSG_MSG" : "لطفا این دستور را در ریپلای به یک فایل ارسال کنید!",
"CAPTION_NOCAPTION_MSG" : "لطفا یک کپشن وارد کنید! \n/caption lablablab",
}
}
