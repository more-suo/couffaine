from math_parser.math_parser import solve_expression
from settings import MATH_BOT
from telebot import types
import telebot


math_bot = telebot.TeleBot(MATH_BOT)


@math_bot.message_handler(commands=['start'])
def start_handler(message):
    greeting_message = "Hey, {0}! Let's solve some mathematical problems. " \
                       "Enter your problem".format(str(message.from_user.first_name))
    print(message.chat.id)
    math_bot.send_message(message.chat.id, greeting_message)
