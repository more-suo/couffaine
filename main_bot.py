from telebot import types
import settings
import telebot

couffaine = telebot.TeleBot(settings.TELEBOT_TOKEN)


@couffaine.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        result = types.InlineQueryResultArticle(
            id='1',
            title='Result',
            description='123',
            input_message_content=types.InputTextMessageContent(output)
        )
        couffaine.answer_inline_query(query.id, result)
    except (NameError, TypeError, SyntaxError) as exc:
        return


@couffaine.message_handler(func=lambda message: True)
def echo_all(message):
    couffaine.reply_to(message, message.text)
    print(message.chat.id)

couffaine.polling()
