from telebot import types
import settings
from math_parser.math_parser import solve_expression
import telebot

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
    couffaine.reply_to(message, message.text)
    print(message.chat.id)

couffaine.polling()
