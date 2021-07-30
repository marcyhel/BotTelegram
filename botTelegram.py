#-512432540

import telebot
import os






BOT_KEY = ''



if os.environ.get('BOT_KEY', '') != '':
	BOT_KEY = os.environ['BOT_KEY']

chaves=BOT_KEY.split(";")

bot = telebot.TeleBot(chaves[0])


txt_price = ""




bot = telebot.TeleBot(chaves[0])
bot.send_message(chaves[1], "txt_price")
