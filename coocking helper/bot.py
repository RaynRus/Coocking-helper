import telebot
from keyboards import get_start_keyboard
from recipeProcessing import syrniki_IzTvoroga_text, soup_s_frikadelykami, seledyPodShuboy, blinyNaMoloke

TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def programm_start(message):
        bot.send_message(
        message.chat.id, 
        """Добро пожаловать, я бот помощник по готовке еды! Чтобы выбрать рецепт еды,
        электронную клавиатуру. Она находится у скрепки.""", 
        reply_markup=get_start_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == 'Сырники с творожком')
def syrnikiIzTvoroga(message):        
    bot.send_message(message.chat.id, "Исходный матреиал - <<https://www.russianfood.com/>>")
    bot.send_message(message.chat.id, syrniki_IzTvoroga_text())

@bot.message_handler(func=lambda message: message.text == 'Суп с фрикадельками')
def syrnikiIzTvoroga(message):
    bot.send_message(message.chat.id, "Исходный матреиал - <<https://www.russianfood.com/>>")
    bot.send_message(message.chat.id, soup_s_frikadelykami())


@bot.message_handler(func=lambda message: message.text == 'Селедь под шубой')
def syrnikiIzTvoroga(message):
    bot.send_message(message.chat.id, "Исходный матреиал - <<https://www.russianfood.com/>>")
    bot.send_message(message.chat.id, seledyPodShuboy())
    
@bot.message_handler(func=lambda message: message.text == 'Блины на молоке')
def blinynaMoloke(message):
    bot.send_message(message.chat.id, "Исходный матреиал - <<https://www.russianfood.com/>>")
    bot.send_message(message.chat.id, blinyNaMoloke())

print('Сервер запущен.')

bot.polling(
    non_stop=True,
    interval=1 
)

