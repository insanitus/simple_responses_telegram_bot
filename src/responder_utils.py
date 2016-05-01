# -*- coding: utf-8 -*-
'''
responder_utils.py
Utilities for responder_bot
'''

# command_remove function
def command_remove(message_text):
	'''
	This function receives a string from the chat in the format:
	\\/COMMAND TEXT
	And removes the slashes and command verb. Thus, we obtain the user's text
	to use it as a parameter for a function.
	'''
	joiner = ''
	split_message = message_text.split()
	for element in split_message[1:]:
		joiner += element + ' '

	return joiner
