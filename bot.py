#!/usr/bin/python3.9
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot


bot = telebot.TeleBot('2014811128:AAHv0wo_BQ9_xT-dvsiO1V9jQniSuNMdmdg')


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
	bot.reply_to(message, "Привет, меня зовут Брэйн, я совсем неопытный бот, но если хочешь посмотреть, чему я уже научился набери /help ")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "могу анекдот рассказать, напиши слово анекдот")



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text == 'анекдот':
		bot.reply_to(message, 'Кит плавает вокруг самки и с упреком говорит:Сколько стран, сотни экологических организаций, выдающиеся политические лидеры, миллионы людей – все они борются за то, чтобы наш вид выжил, а ты мне говоришь – голова болит…')

bot.infinity_polling()