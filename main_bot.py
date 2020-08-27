from telebot import types
import settings
from math_parser.math_parser import solve_expression
import telebot


couffaine = telebot.TeleBot(settings.TELEBOT_TOKEN)


# import threading
# def awake():
#     threading.Timer(1740, awake).start()  # Keep the bot every 29 minutes awake
#     print("29 minutes are over, I'm still alive.")
#     couffaine.send_message(-1001277765819, "29 minutes are over, I'm still alive.")
#
#
# awake()


@couffaine.message_handler(commands=['start'])
def start_handler(message):
    greeting_message = "Hey, {0}! I'm Couffaine. What can i do for you?".format(str(message.from_user.first_name))
    print(message.chat.id)
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
    except (IndexError, KeyError) as exc:
        print(exc)


couffaine.polling()
