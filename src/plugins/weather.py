# -*- coding: utf-8 -*-

@bot.message_handler(commands=['weather', 'Weather'])
def weather_image(message):
  cur.execute('SELECT * from language where id = %s', [str(message.from_user.id)])
  record = cur.fetchall()
  for row in record:
      userid = row[0]
      userlang = row[1]
  if len(message.text.replace("đ¤ Weather", "", 1).split()) < 2:
    bot.reply_to(message, language[userlang]["WWEATHER_NEA_MSG"], parse_mode="Markdown")
    return
  city = message.text.replace("/weather ","").replace(" ", "%20")
  try:
    url = json.load(urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&APPID=d2def4a0a0455314526b0f455f98ec0f&units=metric".format(city)))
  except:
    print("[Weather] Exception occured")
    return
  bot.send_message(message.chat.id, "đ˘ Current status of *" + str(url["name"]) + "*: \n\nđ Country: `" + str(url["sys"]["country"]) + "` \nâď¸ Temperature: `" + str(url["main"]["temp"]) + "Â°C` \n" + "đ¤ Weather: `" + str(url["weather"][0]["main"]) + "` \nđ¨ Wind: `" + str(url["wind"]["speed"]) + "m/s` \nđ§ Humidity: `" + str(url["main"]["humidity"]) + "%`", parse_mode="Markdown")
