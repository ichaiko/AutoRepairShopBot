from telebot import TeleBot
from telebot.types import Message
from telebot import types
import telebot
from .botAttribute import TOKEN
from .botAttribute import Command
from app.models import BotUser
from app.models import State
from .db_scripts import get_goods_list
from .db_scripts import get_services_list
from .db_scripts import get_user_by_id
from .db_scripts import get_state_by_user
from .db_scripts import get_state_by_id

goods_url = 'https://asia-caravan.ru/wp-content/uploads/2023/01/372_big.jpg'
services_url = 'https://ооовебинформ.рф/wp-content/uploads/2014/04/uslugi.jpg'
Command = Command
bot = telebot.TeleBot(TOKEN)


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
        state = State()
        state.bot_user = user
        state.save()

    inline_button(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'goods':
        bot.answer_callback_query(call.id, 'Вы выбрали каталог с товарами')
        bot.send_message(call.message.chat.id, 'Отлично! Для выбора товара введите сообщение в следующем формате:')
        bot.send_message(call.message.chat.id, '@AutoRepairShopBot товары')

        state = get_state_by_id(call.message.chat.id)
        state.registration = False
        state.services = False
        state.goods = True
        state.save()

    elif call.data == 'services':
        bot.answer_callback_query(call.id, 'Вы выбрали каталог с услугами')
        bot.send_message(call.message.chat.id, 'Отлично! Для выбора услуги введите сообщение в следующем формате:')
        bot.send_message(call.message.chat.id, '@AutoRepairShopBot услуги')

        state = get_state_by_id(call.message.chat.id)
        state.registration = False
        state.services = True
        state.goods = False
        state.save()


@bot.inline_handler(func=lambda query: query.query == 'товары')
def query_goods(query):
    results = []
    goods = get_goods_list()
    my_id = 1

    for good in goods:
        result = types.InlineQueryResultArticle(
            id=my_id,
            title=good.name,
            description=' ',
            input_message_content=types.InputTextMessageContent(message_text=f'в наличии:{good.availability}\n'
                                                                             f'описание: {good.description}'),
            thumbnail_url=goods_url
        )
        my_id += 1
        results.append(result)

    bot.answer_inline_query(query.id, results)


@bot.inline_handler(func=lambda query: query.query == 'услуги')
def query_services(query):
    results = []
    my_id = 1
    services = get_services_list()

    for service in services:
        result = types.InlineQueryResultArticle(
            id=my_id,
            title=service.name,
            description=' ',
            input_message_content=types.InputTextMessageContent(message_text=f'описание: {service.description}'),
            thumbnail_url=services_url
        )
        my_id += 1
        results.append(result)

    bot.answer_inline_query(query.id, results)


bot.infinity_polling()
