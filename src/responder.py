# -*- coding: utf-8 -*-

# Import the required modules to run the show
import os
import logging
import telebot

# Setup the logger
telebot.logger.setLevel(loggin.DEBUG)

# Load API's key from environment
responder_bot = telebot.AsyncTeleBot(os.environ['BOT_KEY'])
