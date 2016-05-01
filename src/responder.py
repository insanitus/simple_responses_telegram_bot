# -*- coding: utf-8 -*-

# Import the required modules to run the show
import os
import logging
import telebot
import responder_utils

# Setup the logger
telebot.logger.setLevel(logging.DEBUG)

# Load API's key from environment
responder_bot = telebot.AsyncTeleBot(os.environ['BOT_KEY'])

# Dictionary to store the messages or replies
text_messages_list = []

'''
Commands:
/start - Turn on the engine
/about - Same as /Start
/help - Usage of the commands
/add - Add a message to the DB
/list - List messages
/remove - Remove a message
'''

# Message hanlder for the start command
@responder_bot.message_handler(commands=['start', 'about'])
def start_command(message):
	'''
	This is tye /start command. A response is optional but some people
	put a extended description of the bot.
	'''
	responder_bot.reply_to(message, 'Something')


# Message handler for the add-response command
@responder_bot.message_handler(commands=['add'])
def add_response_command(message):
	'''
	Add
	'''
	response = responder_utils.command_remove(message.text)
	if  response is '':
		responder_bot.reply_to(message, 'Cant add empty messages. Try again!')
	else:
		if response not in text_messages_list:
			text_messages_list.append(response)
			responder_bot.reply_to(message, 'Added: ' + response)
		else:
			responder_bot.reply_to(message, 'It is a duplicate response')


# Message handler for the remove-response command
@responder_bot.message_handler(commands=['remove'])
def remove_response_command(message):
	'''
	Remove
	'''
	response = responder_utils.command_remove(message.text)
	try:
		text_messages_list.remove(response)
		responder_bot.reply_to(message, 'Done. Use /list to see other resonses')
	except:
		responder_bot.reply_to(message, 'Hey! The message wasnt in the list.')


# Message handler for the list-response command
@responder_bot.message_handler(commands=['list'])
def list_messages_command(message):
	'''
	List
	'''
	if not text_messages_list:
		responder_bot.reply_to(message, 'Please, add responses with /add')
	else:
		responder_bot.reply_to(message, str(text_messages_list))


# Handler for the in-line command
@responder_bot.inline_handler(lambda query: len(query.query) is 0)
def default_query(inline_query):
	try:
		queries_array = []
		for element_number in range(len(text_messages_list)):
			queries_array = telebot.types.InlineQueryResultArticle(element_number, text_messages_list[element_number], text_messages_list[element_number])

		responder_bot.answer_inline_query(inline_query.id, queries_array)
	except Exception as e:
		print(e)


# def console_listener(messages):
#     for message in messages:
#         '''
#         To have a message listener is to have a Single Point OF Failure(SPOF)
#         So, we must handle exceptions for failure. In case of any expected
#         action, command or Unicode character our app doesn't support.
#         Without error handling our bot can stop working and we could enter
#         to an infinite loop using nohup
#         '''
#         try:
#             # Print the good stuff on the console
#             print('[Sender ID: ' + str(message.chat.id) + '] Text: ' + message.text)
#         except:
#             # Ignore errors at printing the messages
#             pass


def main_loop():
	responder_bot.polling(True)
	# responder_bot.set_update_listener(console_listener)



if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
