#-512432540

import telebot
import os






BOT_KEY = ''

GROUP_KEY = ''

if os.environ.get('BOT_KEY', '') != '':
	BOT_KEY = os.environ['BOT_KEY']
if os.environ.get('GROUP_KEY', '') != '':
	GROUP_KEY = os.environ['GROUP_KEY']

bot = telebot.TeleBot(BOT_KEY)


txt_price = ""




bot = telebot.TeleBot(BOT_KEY)
bot.send_message(GROUP_KEY, "txt_price")
