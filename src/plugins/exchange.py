# -*- coding: utf-8 -*-

@bot.message_handler(commands=['rate'])
def ex_message(message):
  cur.execute('SELECT * from language where id = %s', [str(message.from_user.id)])
  record = cur.fetchall()
  for row in record:
      userid = row[0]
      userlang = row[1]
  if len(message.text.replace("💵 Exchange rate", "", 1).split()) < 2:
    bot.reply_to(message, language[userlang]["EXCHANGE_NEA_MSG"], parse_mode="Markdown")
    return
  currency = message.text.upper().split()[1]
#  rlex = re.compile(r'^\b\w{3}\b')
#  if rlex.search(currency[0]):
#    pass
#  else:
#    bot.reply_to(message, "Error: \n\n`Invalid currency code!`", parse_mode="Markdown")
#    return
  exresult = requests.get('http://api.fixer.io/latest?base={}'.format(currency)).json()
# check for .. chichi bood? aha Check for errors.... rah behtari naresid be zehnam XD IM NOOB IN PYTHON
  try:
    asd = exresult['error']
    bot.reply_to(message, "Error: \n\n`Currency not found!`", parse_mode="Markdown")
    return
  except:
    pass
  ac = ["USD", "EUR", "RUB", "AUD", "CAD", "GBP"]
  for crr in ac:
    if crr == currency:
      break
    if crr == "CAD":
      if currency != crr:
        bot.reply_to(message, "Error: \n\n`Base currency not found!`", parse_mode="Markdown")
        return
  base = str(exresult['base'])
  datet = str(exresult['date'])
# Dirty coding.
  aud = ""
  eur = ""
  rub = ""
  cad = ""
  gbp = ""
  if currency != "AUD":
    aud = "🇦🇮 `AUD`: *" + str(exresult['rates']['AUD']) + "*"
  bgn = "🇧🇬 `BGN`: *" + str(exresult['rates']['BGN']) + "*"
  brl = "🇧🇷 `BRL`: *" + str(exresult['rates']['BRL']) + "*"
  if currency != "CAD":
    cad = "🇨🇦 `CAD`: *" + str(exresult['rates']['CAD']) + "*"
  chf = "🇨🇭 `CHF`: *" + str(exresult['rates']['CHF']) + "*"
  cny = "🇨🇳 `CNY`: *" + str(exresult['rates']['CNY']) + "*"
  czk = "🇨🇿 `CZK`: *" + str(exresult['rates']['CZK']) + "*"
  dkk = "🇩🇰 `DKK`: *" + str(exresult['rates']['DKK']) + "*"
  if currency != "GBP":
    gbp = "🇬🇧 `GBP`: *" + str(exresult['rates']['GBP']) + "*"
  hdk = "🇭🇰 `HKD`: *" + str(exresult['rates']['HKD']) + "*"
#  hrk = exresult['HRK'] FLAG NOT FOUND
#  huf = exresult['HUF'] SAME AS ABOVE
  idr = "🇮🇩 `IDR`: *" + str(exresult['rates']['IDR']) + "*"
#  ils = exresult['ILS'] NOT FOUND? WTF?
  inr = "🇮🇳 `INR`: *" + str(exresult['rates']['INR']) + "*"
  jpy = "🇯🇵 `JPY`: *" + str(exresult['rates']['JPY']) + "*"
#  kry = exresult['KRY'] KOREA? NOT FOUND.
  mxn = "🇮🇹 `MXN`: *" + str(exresult['rates']['MXN']) + "*"
  if currency != "MYR":
    myr = "🇲🇾 `MYR`: *" + str(exresult['rates']['MYR']) + "*"
  nok = "🇳🇴 `NOK`: *" + str(exresult['rates']['NOK']) + "*"
  nzd = "🇬🇸 `NZD`: *" + str(exresult['rates']['NZD']) + "*"
  php = "🇵🇭 `PHP`: *" + str(exresult['rates']['PHP']) + "*"
#  pln = exresult['PLN'] NOT FLAGGED CORRECTLY. MORE THAN 6 FLAGS FOUND
#  ron = exresult['RON'] WTF?
  rub = "🇷🇺 `RUB`: *" + str(exresult['rates']['RUB']) + "*"
  sek = "🇸🇪 `SEK`: *" + str(exresult['rates']['SEK']) + "*"
  sgd = "🇸🇬 `SGD`: *" + str(exresult['rates']['SGD']) + "*"
  thb = "🇹🇭 `THB`: *" + str(exresult['rates']['THB']) + "*"
#  tryy = exresult['TRY'] not found.
#  zar = exresult['ZAR'] NOT SURE WHICH FLAG
  if currency != "EUR":
    eur = "🇪🇺 `EUR`: *" + str(exresult['rates']['EUR']) + "*"
  bot.send_message(message.chat.id, "Exchange date rata as `{}`: \nBase currency: `{}`\n\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(datet, base, aud, bgn, brl, cad, chf, cny, czk, dkk, gbp, hdk, idr, inr, jpy, mxn, myr, nok, nzd, php, rub, sek, sgd, thb, eur), parse_mode="Markdown")
