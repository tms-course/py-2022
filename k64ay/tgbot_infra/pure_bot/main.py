from telebot import TeleBot, types

TELEGRAM_TOKEN = '5520789286:AAG9sEYR-stJP4gtgha5vEefFzPWQeUSqEY'

bot = TeleBot(TELEGRAM_TOKEN, threaded=False)

@bot.message_handler(commands=['start']) # /start
def start_message(message):
    bot.send_message(message.chat.id, '''Здароука!!!\nNew line\n/new_command - shows buttons''')

@bot.message_handler(commands=['new_command'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Button 1 😂')
    btn2 = types.KeyboardButton('Button 2 🙊')
    markup.row(btn1, btn2)
    
    bot.send_message(message.chat.id, 'Choose your button type.', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'И тебе не хворать!')
    else:
        bot.send_message(message.chat.id, 'О чем речь?')


bot.infinity_polling()