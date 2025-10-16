import telebot
import random
    
bot = telebot.TeleBot("Токен")

@bot.message_handler(commands=['password'])
def gen_pass(message):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(10):
        password += random.choice(elements)
    bot.reply_to(message, password)  

@bot.message_handler(commands=['smile'])
def gen_pass(message):
    elements = "🤓🙊😁😞🙈💋😭❤️😎😋🙂‍↔️🧐😂😘😍😊😔😄😒😳😜😉😃😢😝😱😏😅😚😌😀😆😕😈👿👹👺🤧😪🫡🤫🫠🤥😶‍🌫️🥶🥵😳🤯"
    smile = ""
    for i in range(1):
        smile += random.choice(elements)
    bot.reply_to(message, smile) 


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()
