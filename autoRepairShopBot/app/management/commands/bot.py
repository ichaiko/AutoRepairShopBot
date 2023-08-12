from telebot import TeleBot
from telebot.types import Message
import telebot
from .botAttribute import TOKEN
from .botAttribute import Command
from app.models import BotUser
from app.models import State

Command = Command
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message: Message):
    bot.send_message(message.chat.id, "Здравствуйте!")

    user, flag = BotUser.objects.get_or_create(telegram_id=message.chat.id,
                                               telegram_login=message.from_user.username)

    if flag:
        state = State()
        state.bot_user = user
        state.registration = True
        state.save()


bot.infinity_polling()
