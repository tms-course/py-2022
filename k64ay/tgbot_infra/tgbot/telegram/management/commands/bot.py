from typing import Optional, Any
from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot, types

from telegram.models import Event


bot = TeleBot(settings.TELEGRAM_TOKEN, threaded=False)

class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        bot.infinity_polling()

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hello there!!')

@bot.message_handler(commands=['list_events'])
def list_events_handler(message):
    count = Event.objects.count()

    bot.send_message(message.chat.id, f"Event's count = {count}")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    Event.objects.create(
        desc=message.text,
        user_id=message.from_user.id)
    
    bot.send_message(message.chat.id, 'Event is tracked.')