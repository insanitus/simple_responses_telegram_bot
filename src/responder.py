# -*- coding: utf-8 -*-

# Import the required modules to run the show
import os
import logging
import telebot

# Setup the logger
telebot.logger.setLevel(loggin.DEBUG)

# Load API's key from environment
responder_bot = telebot.AsyncTeleBot(os.environ['BOT_KEY'])

# Dictionary to store the messages or replies
text_messages = {}

'''
Commands:
/start - Turn on the engine
/about - Same as /Start
/help - Usage of the commands
/add - Add a message to the DB
/remove - Remove a message
/edit - Edit a response
/send - Send love
'''

# Message hanlder for the start command
@responder_bot.message_handler(commands=['start', 'about'])
def start_command(message):
	'''
	This is tye /start command. A response is optional but some people
	put a extended description of the bot.
	'''
	responder_bot.reply_to(message, '''Something''')

# Message handler for the add-response command
@responder_bot.message_handler(commands=[''])
def add_response_command(message):
	'''
	'''
	responder_bot.reply_to(message,)


# Message handler for the remove-response command
@responder_bot.message_handler(commands=[''])
def remove_response_command(message):
	'''
	'''
	responder_bot.reply_to(message,)



# Message handler for the edit-response command
@responder_bot.message_handler(commands=[''])
def edit_response_command(message):
	'''
	'''
	responder_bot.reply_to(message,)


# Message handler for the send-response command
@responder_bot.message_handler(commands=[''])
def send_response_command(message):
	'''
	'''
	responder_bot.reply_to(message,)


def main_loop():
	responder_bot.polling(True)
