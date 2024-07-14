import os
import inspect
import threading
from telebot.types import Message, InlineKeyboardMarkup, CallbackQuery, User, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove, InlineKeyboardButton

import telebot

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"), parse_mode="MARKDOWN")
bot_thread = threading.Thread(target=bot.infinity_polling)

def start():
    """
    Запуск бота
    """
    global bot_thread
    print(f"{inspect.currentframe().f_code.co_name}")
    bot_thread.start()


def stop():
    """
    Остановка бота
    """
    global bot_thread
    print(f"{inspect.currentframe().f_code.co_name}")
    bot_thread.join()


@bot.message_handler(commands=['hello'])
def hello(message: Message):
    """
    Ответ на команду test
    """
    print(f"{inspect.currentframe().f_code.co_name}")
    bot.send_message(message.chat.id,
                        text=f'Hello',
                        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None if message.reply_to_message else None).message_id

