      '''
      image = open('qrcode.png', 'rb')
      bot.edit_message_media(media=types.InputMedia(type='photo', media=image), inline_message_id=msgid, chat_id=call.message.chat.id, message_id=3289, reply_markup=pho2(call))
      '''

