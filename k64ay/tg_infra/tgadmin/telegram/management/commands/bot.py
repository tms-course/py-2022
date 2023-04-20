import os
import json

from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot, types


bot = TeleBot(settings.TELEGRAM_TOKEN, threaded=False)
PAYMENT_PROVIDER_TOKEN = "284685063:TEST:MGYzOGFjNmEyY2Rk"

class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()	


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо',reply_markup=markup)
    
@bot.message_handler(commands=['buy'])
def buy_process(message):
    bot.send_invoice(
        chat_id=message.chat.id,
        title="Payment Example",
        description="Payment Example using python-telegram-bot",
        invoice_payload="Custom-Payload",
        provider_token=PAYMENT_PROVIDER_TOKEN,
        currency="USD",
        prices=[types.LabeledPrice("Test", 1 * 100)],
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=True,
        is_flexible=True)

@bot.shipping_query_handler(lambda q: True)
def shipping_process(shipping_query: types.ShippingQuery):
    if shipping_query.shipping_address.country_code == 'UK':
        return bot.answer_shipping_query(
            shipping_query_id=shipping_query.id,
            ok=False,
            error_message='Shipping process failed')
    
    superspeed_option = types.ShippingOption(
        id='superspeed',
        title='Супер быстрая!')
    superspeed_option.add_price(types.LabeledPrice('Лично в руки!', 1000))
    shipping_options = [superspeed_option]

    if shipping_query.shipping_address.country_code == 'RU':
        post_options = types.ShippingOption(
            id='post',
            title='Почта России')

        post_options.add_price(types.LabeledPrice('Кортонная коробка', 1000))
        post_options.add_price(types.LabeledPrice('Срочное отправление!', 1000))
        shipping_options.append(post_options)

        if shipping_query.shipping_address.city == 'Санкт-Петербург':
            pickup_options = types.ShippingOption(
                id='pickup',
                title='Самовывоз')
            pickup_options.add_price(types.LabeledPrice('Самовывоз в Сантк-Петербурге', 1000))
            shipping_options.append(pickup_options)

    bot.answer_shipping_query(
        shipping_query.id,
        ok=True,
        shipping_options=shipping_options)

@bot.pre_checkout_query_handler(lambda q: True)
def checkout_process(pre_checkout_query: types.PreCheckoutQuery):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message: types.Message):
    bot.send_message(
        message.chat.id,
        'Платеж на сумму `{total_amount} {currency}` совершен успешно!'.format(
            total_amount=message.successful_payment.total_amount // 100,
            currency=message.successful_payment.currency))
    
# @bot.message_handler(content_types='text')
# def message_reply(message):
#     markup = types.ReplyKeyboardMarkup()
#     itembtna = types.KeyboardButton('a')
#     itembtnv = types.KeyboardButton('v')
#     itembtnc = types.KeyboardButton('c')
#     itembtnd = types.KeyboardButton('d')
#     itembtne = types.KeyboardButton('e')
#     markup.row(itembtna, itembtnv)
#     markup.row(itembtnc, itembtnd, itembtne)
#     bot.send_message(message.chat.id, message, reply_markup=markup)
        

page = 1
count = 10


@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')
    global count
    global page
		#Обработка кнопки - скрыть
    if req[0] == 'unseen':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    #Обработка кнопки - вперед
    elif req[0] == 'next-page':
        if page < count:
            page = page + 1
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
            markup.add(types.InlineKeyboardButton(text=f'<--- Назад', callback_data=f'back-page'),
                       types.InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       types.InlineKeyboardButton(text=f'Вперёд --->', callback_data=f'next-page'))
            bot.edit_message_text(f'Страница {page} из {count}', reply_markup = markup, chat_id=call.message.chat.id, message_id=call.message.message_id)
    #Обработка кнопки - назад
    elif req[0] == 'back-page':
        if page > 1:
            page = page - 1
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
            markup.add(types.InlineKeyboardButton(text=f'<--- Назад', callback_data=f'back-page'),
                       types.InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       types.InlineKeyboardButton(text=f'Вперёд --->', callback_data=f'next-page'))
            bot.edit_message_text(f'Страница {page} из {count}', reply_markup = markup, chat_id=call.message.chat.id, message_id=call.message.message_id)

    elif call.data == 'btn1':
        try:
            foto2 = open(os.path.join(settings.BASE_DIR, 'static/snowman.png'), 'rb')
            bot.edit_message_media(media=types.InputMedia(type='photo', media=foto2, caption = "noitpac"), chat_id=call.message.chat.id, message_id=call.message.message_id)		
        except:	
            bot.send_message(call.message.chat.id, "Бот не смог изменить фото!")



@bot.message_handler(commands=["editphoto"])
def editfoto(message):
  try:
    kbi = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="Кнопка", callback_data='btn1')
    kbi.add(btn)    #!		
    foto1 = open(os.path.join(settings.BASE_DIR, 'static/birthday.png'), 'rb')
    bot.send_photo(message.chat.id, foto1, caption = "caption", reply_markup = kbi)
  except:	
    bot.send_message(message.chat.id, "Бот не смог отправить фото!")

#Обработчик входящих сообщений
@bot.message_handler(content_types=['text'])
def start(m):
    global count
    global page
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(types.InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               types.InlineKeyboardButton(text=f'Вперёд --->', callback_data=f'next-page'))
    bot.send_message(m.from_user.id, "Привет!!!", reply_markup = markup)

