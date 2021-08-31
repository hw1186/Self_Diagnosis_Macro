import telegram

from class_example import MY_TELEGRAM_TOKEN, MY_TELEGRAM_CHAT_ID


class SendTelegram:

    def send_message(self, message):
        telgm_token = MY_TELEGRAM_TOKEN
        bot = telegram.Bot(token=telgm_token)
        bot.sendMessage(chat_id=MY_TELEGRAM_CHAT_ID, text=message)
