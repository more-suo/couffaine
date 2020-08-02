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


@couffaine.message_handler(func=lambda message: True)
def echo_all(message):
    hate_answers = ["Длявер, замолчи уже, пожалуйста.",
                    "Длявер совсем заебал.",
                    "Длявер, иди нахуй, а.",
                    "Длявер, тупица ты недоделанная.",
                    "Длявер, ты таким родился?"]
    classic_answers = ["Let's do some math.",
                       "I will solve your problems.",
                       "Math is fun."]
    couffaine.reply_to(message, classic_answers[randint(0,2)] if message.chat.id != -1001277765819 else hate_answers[randint(0, 4)])
    print(message.chat.id)


awake()
couffaine.polling()
