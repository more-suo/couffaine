from telebot import types
import telebot
import settings
from layout_switcher.layout_switcher import translate_to_cyrillic
from layout_switcher.layout_switcher import translate_to_latin


couffaine = telebot.TeleBot(settings.MAINBOT_TOKEN)


# import threading
# def awake():
#     threading.Timer(1740, awake).start()  # Keep the bot every 29 minutes awake
#     print("29 minutes are over, I'm still alive.")
#     couffaine.send_message(-1001277765819, "29 minutes are over, I'm still alive.")
#
#
# awake()


def send_solution(id, expression):
    answer = str(solve_expression(expression))
    result = types.InlineQueryResultArticle(
        id='1',
        title=expression + ' = ' + answer,
        description='Solved!',
        input_message_content=
        types.InputTextMessageContent(message_text=expression + ' = ' + answer)
    )
    couffaine.answer_inline_query(id, [result])


@couffaine.message_handler(commands=['start'])
def start_handler(message):
    greeting_message = "Hey, {0}! I'm Couffaine. What can i do for you?".format(str(message.from_user.first_name))
    print(message.chat.id)
    couffaine.send_message(message.chat.id, greeting_message)


@couffaine.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    split_query = query.query.split()
    command = split_query[0]

    if command[0] == 's':  # stands for solve
        try:
            send_solution(query.id, ''.join(split_query[1:]))
        except (IndexError, KeyError) as exc:
            print("Failed to solve:", exc)

    elif command[0] == 't':  # stands for translate
        try:
            split_text = query.query.split()
            layout, text = split_text[1], ' '.join(split_text[2:])
            print(layout, text)
        except IndexError as exc:
            print("Failed to translate:", exc)


couffaine.polling()
