from telebot import TeleBot
from telebot.types import Message
import telebot
from .botAttribute import TOKEN
from .botAttribute import Command
from app.models import BotUser

Command = Command
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message: Message):
    bot.send_message(message.chat.id, "Здравствуйте!")

    BotUser.objects.get_or_create(telegram_id=message.chat.id,
                    telegram_login=message.from_user.username)


bot.infinity_polling()
