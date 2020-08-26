from telebot import types
import settings
from math_parser.math_parser import solve_expression
import telebot
import threading
from random import randint


def awake():
    threading.Timer(1740, awake).start()  # Перезапуск через 5 секунд
    print("29 minutes are over, I'm still alive.")
    couffaine.send_message(-1001277765819, "29 minutes are over, I'm still alive.")


couffaine = telebot.TeleBot(settings.TELEBOT_TOKEN)


@couffaine.message_handler(commands=['start'])
def start_handler(message):
    greeting_message = "Hey, {0}! I'm Couffaine. What can i do for you?".format(str(message.from_user.username))
    couffaine.send_message(message.chat.id, greeting_message)


@couffaine.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        answer = str(solve_expression(query.query))
        result = types.InlineQueryResultArticle(
            id='1',
            title=query.query + ' = ' + answer,
            description='Solved!',
            input_message_content=
            types.InputTextMessageContent(message_text=query.query + ' = ' + answer)
        )
        couffaine.answer_inline_query(query.id, [result])
    except (IndexError) as exc:
        return


awake()
couffaine.polling()
