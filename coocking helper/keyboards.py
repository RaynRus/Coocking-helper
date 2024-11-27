import telebot
from functools import lru_cache # Можно понять по названию декаратора

@lru_cache(maxsize=3)
def get_start_keyboard()-> telebot.types.ReplyKeyboardMarkup:
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    syinikiIzTvoroga = telebot.types.KeyboardButton('Сырники с творожком')
    soupSfrikadelykami = telebot.types.KeyboardButton('Суп с фрикадельками')
    seledyPodShuboy = telebot.types.KeyboardButton('Селедь под шубой')
    blinyNaMoloke = telebot.types.KeyboardButton('Блины на молоке')

    keyboard.add(syinikiIzTvoroga, soupSfrikadelykami, seledyPodShuboy, blinyNaMoloke)

    return keyboard