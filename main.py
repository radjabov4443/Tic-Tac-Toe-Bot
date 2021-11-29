from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, Dispatcher, \
    CallbackContext
from telegram.update import Update
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

updater = Updater(token='2113510006:AAHrTEju9Y5bON2s21orEjJXXpAcXUWk_zU')

dispatcher: Dispatcher = updater.dispatcher


def inline_query(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query
    update.inline_query.answer([
        InlineQueryResultArticle(
            id='x', title='X',
            input_message_content=InputTextMessageContent('X')),
        InlineQueryResultArticle(
            id='o', title='O',
            input_message_content=InputTextMessageContent('O')),
    ])


dispatcher.add_handler(InlineQueryHandler(inline_query))

updater.start_polling()
updater.idle()
