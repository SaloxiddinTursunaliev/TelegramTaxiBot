# -*- coding: utf-8 -*-

# WARNING: This is OLD locale, Its for when the bot wasnt multilanguage. (-v1.1.0)
# It will be fully removed on next versions.

import sys

reload(sys)  
sys.setdefaultencoding("UTF8")
# LANGUAGE FILE


START_MSG = str("Hey! š \n \nWelcome to the *ZigZagBot*! š±š \nDeveloped by @WebShark25! \n \nAll bot commands: \nš¢ _/help_ - Get help message \nš¢ _/time <city>_ - Gets current time in any timezone! \nš¢ _/calc_ - Lets do some maths \nš¢ _/support_ - Chat with us! \nš¢ _/sendcontact_ - Forward contact to admin \nš¢ _Send feedback_ - Send feedback! \nš¢ _/echo <msg>_ - Echoes the message \nš¢ _/short <link>_ - Shorts the link! \nš¢ _/weather <city>_ - Gets weather! \nš¢ _/mp3tag <artist>||<title>_ - Edits audios tags! \nš¢ _/tocontact <phone>||<name>_ - Turns string to Telegram contact! \nš¢ _/qrcode <text>_ - QR Code creator!! \nš¢ _/ip <IP/Hostname>_ - Get IP location & more! \nš¢ _/rate <currency>_ - Get latest exchange rates! \nš¢ _/addcounter add_ - Add seen counter to your message! \nš¢ _/lmgtfy <text>_ - Let me google that for you! \nš¢ _/download <link>_ - Download a file and send it using telegram! \nš¢ _/addreply <syntax>_ - Learn the bot how to respond! \nš¢ _/id_ - Get your ID & Group's ID \n \n_More commands comming soon!_ \n \nI Hope you enjoy it! ").encode("utf-8")
START_BUTTONS = ("ā Id", "ā± Time", "š Memes", "š­ Send feedback", "š¤ Weather", "š„ Support", "š Link shortner", "āļø Calculate", "š§ Mp3Tag", "š” IP Geolocation", "ā»ļø QR Code", "šµ Exchange rate") # SPLITS 3 PER LINE
SHOWED_BUTTONS_MSG = "Here you are ;)"
TEST_MSG = "This is a test message."
SHARE_CONTACT_MSG = "Please share your contact to the bot (in a private message)."
NO_ECHO_IN_SUPERGP_MSG = "Unfortunately I wont reply to messages sent in a supergroup to prevent spamming."
ECHO_REPLY_MSG = "Please enter a text so I reply to it!"
ERROR_MSG = "Error occured."
CONTACT_RECIEVED_MSG = "New contact recieved:"
CONTACT_FORWARDED_MSG = "Contact successfully forwarded!"
# {0} = name | {1} = gp title
GP_GREETING_MSG = "Hey *{0}*! \n \nWelcome to the group *{1}* š \n \n_Have fun & Enjoy!_"
GP_FAREWELL_MSG = "Oh no š \n*{0} left the group ā¹ļø"
# {0} = name | {1} = id | {2} = gp id
ID_MSG = "š¢ Your name: *{0}* \nš¢ Your ID: *{1}* \n"
INGP_ID_MSG = "š¢ Group ID: *{2}* \n"
REPLIED_ID_MSG = "š¢ Users ID: *{3}* \n"
FORWARDED_ID_MSG = "š¢ Users ID: *{4}* \n"
NON_ADMIN_ADDED_BOT_MSG = "Im sorry ā¹ļø \nIm not authorized to join groups by normal members. \nOnly *admins* can add me to groups."
BOT_JOINED_MSG = "Heyš§! I am here, At your service."
MESSANGER_JOIN_MSG = "Now sending feedback. \nPlease enter your message!"
MESSANGER_SUBMIT_MSG = "OK. I got your message. Are you sure you want to send it?"
MESSANGER_CANCEL_MSG = "Canceled!"
MESSANGER_LEAVE_MSG = "Thanks for your feedback! Exiting."
WEBSHOT_CAPTION_MSG = "By the ZigZag bot"
COMMAND_NOT_FOUND = "Im sorry š¢ But the command you entered does not exists."
BANNED_MSG = ":O You got banned from the bot!"
UNBANNED_MSG = "Welcome back! You are unbanned now ;)"
GP_STATUS_MSG = "ā”ļø All group messages: {0}"
TIME_MSG = "ā”ļø Date & Time: {0}"
# JOINED_MESSENGER_MSG = "ā”ļø Now chatting with support team!"
WAITING_APPROVAL_MESSENGER_MSG = "ā”ļø Your request has been submitted! Please wait for manual approval."
ACCEPTED_MESSENGER_MSG = "ā”ļø Your request has been approved! Now chatting with support."
DENIED_MESSENGER_MSG = "ā”ļø Im sorry, But your request has been denied."
MESSAGE_SENT_MESSENGER_MSG = "Message sent! Please wait for response"
KICKED_MESSENGER_MSG = "You got auto-kicked from the messenger because you spammed alot."
ALREADY_IN_MESSENGER_MSG = "You are already chatting with support! to exit, type '/leave'"
NOT_IN_MESSENGER_MSG = "You are not chatting with support! to start, type '/support'"
LEFT_MESSENGER_MSG = "ā”ļø We hope you enjoyed ;) Leaving the messenger."
MEME_NEA_MSG = "To use this command, you need to follow this format: \n`/meme <type>||<top>||<bottom>` \nFor example: `/meme Gangnam Style||Oppa||Gangnam style!`\n_Remember: No spaces within words and ||s!_ \n\nRemember, this bot supports more than a thousand of memes! Some examples: \n\nš¢ Good Guy Greg\nš¢ First World Problems\nš¢ Scumbag Steve\nš¢ Hipster Barista\nš¢ Bad Luck Brian\nš¢ Success Kid\nš¢ Ridiculously Photogenic Guy\nš¢ Sudden Clarity Clarence\nš¢ College Freshman\nš¢ Skeptical Baby\nš¢ Gangnam Style\nš¢ Talk To Spongebob\nš¢ Suspicious Cat"
CALC_NEA_MSG = "How can i calculate null? \nYour command should be like this: \n`/calc 5+5*2`"
CHATTER_NEA_MSG = "Hey! š± \n \nI think you don't know how to work with this. \n \nYou can actually learn me how to respond to some messages š \n \nSimply do: /addreply <Text>||<Response> \n \nFor example, if you want to enter 'hi' and then you want me to say 'hello', you need to execute this: \n /addreply Hi||Hello \n \nIts simple š And also fun š"
CHATTER_INCORRECT_MSG = "String recieved in an incorrect format.."
CHATTER_ALREADYDEFINED_MSG = "Im sorry, this message had already been defined!"
CHATTER_DONE_MSG = "Ooo yeah! Now I know if you say `{}`, I Should Answer `{}` :) \nCan you teach me *more*? šš"
IP_ERROR_MSG = "Error: \n\n`Invalid IP/Hostname`"
IP_NEA_MSG = "Please, enter an IP address or hostname. \n\nExample: `/ip 4.2.2.4`"
IP_DONE_MSG = "IP Information for *{}*: \n\nš Country: *{}* \nš« City: *{}* \nš” ISP: *{}* \nā± TimeZone: *{}*"
MP3TAG_NEA_MSG = "Please use correct syntax: \n`/mp3tag Artist||Title`\nAnd then, send the audio file."
MP3TAG_SENDAUDIO_MSG = "Please send the audio now!"
QRCODE_NEA_MSG = "Please, enter a text so I can convert it to QR code. \n\nFor example: `/qrcode http://sadeco.ir`"
SHORTNER_NEA_MSG = "Please enter a link so I can short it. \nLike: `/short http://google.com`"
TIME_NEA_MSG = "Enter a time zone/city/region/etc. please! \n\nExample: `/time Tehran`"
WWEATHER_NEA_MSG = "Enter a city so I can tell its weather! :P \n\nExample: `/weather Tehran`"
INLINE_HELP_MSG = "*Inline mode help!:* \n \nTo use inline mode, first mention the bots ID (@TheZigZagBot) in your message, then use one of theese syntaxes: \n \nš¢echo <message> (_Echoes the message using HTML markup_) \nš¢cal <ex> (_Calculator.. Easy as a pie_) \nš¢time <city> (_Get time for anywhere! even nowhere!_) \nš¢weather <city> (_Current weather in <city>!_) \nš¢hideit <message> (_Hides the message you enter! :D So its un-forwardable._) \n \nExample: `@TheZigZagBot time tehran` \n\nMore options comming *soon*!"
ADDCOUNTER_NEA_MSG = "Do you want to know how many people saw your message? Yeah! Now its possible! \nJust type `/addcounter add` and then forward/send your message!"
LMGTFY_NEA_MSG = "Let me *Google* that for you! \n\nJust do `/lmgtfy <search>`"
DOWNLOADER_NEA_MSG = "Welcome to *ZigZag* downloader! \n\nYou can enter a *link* with a file size below *30MB*, and recieve that file in Telegram! \n\nPlease use this syntax: `/download http://example.com/file.zip` \n\nWarning: You have a limit of *3 files per minute*. Please dont exceed it."
DOWNLOADER_WAIT_MSG = "Im sorry, but you can only have *1 concurrent download*."
DOWNLOADER_DL_MSG = "Retrieving the file from server. Please wait..."
DOWNLOADER_UP_MSG = "Uploading the file for you. Please wait..."
DOWNLOADER_OVERSIZE_MSG = "The file was too *big*! Maximum file size should be *below 30MB*."
DOWNLOADER_ERROR_MSG = "Im sorry, but an unknown error occured. \nPlease check the *file name* & *file size*, then try again."
SETTINGS_WLC_MSG = "TheZigZag *Settings*! \nPlease, choose a _value_ to edit. \nć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°"
SETTINGS_LANGUAGE_CHANGED_MSG = "Success! Language has been updated. \nć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°ć°"
