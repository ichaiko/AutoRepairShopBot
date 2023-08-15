from telebot import TeleBot
from telebot.types import Message
from telebot import types
import telebot
from .botAttribute import TOKEN
from .botAttribute import Command
from app.models import BotUser
from app.models import State
from .db_scripts import get_goods_list

Command = Command
bot = telebot.TeleBot(TOKEN)
user = BotUser()
state = State()


def inline_button(message: Message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Товары", callback_data='goods')
    item2 = types.InlineKeyboardButton(text='Услуги', callback_data='services')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=markup)


@bot.message_handler(commands=["start", "старт"])
def start_message(message: Message):
    bot.send_message(message.chat.id, "Здравствуйте!")

    user, flag = BotUser.objects.get_or_create(telegram_id=message.chat.id,
                                               telegram_login=message.from_user.username)

    if flag:
        state.bot_user = user
        state.save()

    inline_button(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'goods':
        bot.answer_callback_query(call.id, 'Вы выбрали каталог с товарами')
        bot.send_message(call.message.chat.id, 'Отлично! Для выбора товара введите сообщение в следующем формате:')

    elif call.data == 'services':
        bot.answer_callback_query(call.id, 'Вы выбрали каталог с услугами')
        bot.send_message(call.message.chat.id, 'Отлично! Для выбора услуги введите сообщение в следующем формате:')

    bot.send_message(call.message.chat.id, '@AutoRepairShopBot ')


bot.infinity_polling()
