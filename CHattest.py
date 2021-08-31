import telegram

telgm_token = '1923774179:AAHEXsSgs5mDMqf8PVVNTn1kOb2S_SFX2Ng'

bot = telegram.Bot(token = telgm_token)

updates = bot.getUpdates()

print(updates)

for i in updates:
    print(i)

print('start telegram chat bot')

#'676149244'