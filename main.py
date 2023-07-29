import telebot
from telebot import types

import weather_report
import translator_4bot
import joking_part

file = open("token.txt")

bot = telebot.TeleBot(
    file.readline() # token
)

file.close()


hi_words  = [
    'привет',
    'приветик',
    'хай',
    'зравствуй',
    'здравствуйте',
    'доброе утро',
    'добрый вечер',
    'добрый день'
]


@bot.message_handler(content_types=['text'])
def get_text_messages(msg):

    message = msg.text.lower()

    if message in weather_report.weather_messages:
        if 'завтра' not in message:
            bot.send_message(msg.from_user.id, "хорошо! \n погода сегодня " + str(weather_report.get_current_weather()))
        else:
            bot.send_message(msg.from_user.id,"погода есть только на сегодня")
    elif 'переведи' in message or 'перевод' in message:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("с английского на русский")
        btn2 = types.KeyboardButton("с русского на английский")
        markup.add(btn1, btn2)
        bot.send_message(msg.from_user.id,"хорошо! \n выбери c какого на какой язык переводить",reply_markup=markup)
        bot.register_next_step_handler(msg, choose_lang)
    elif message in hi_words:
        bot.send_message(msg.from_user.id,"приветик! \n как дела?")
    else:
        bot.send_message(msg.from_user.id,"не понял что вы хотите...")
        bot.send_message(msg.from_user.id,"но вот вам рандомная шутка:")
        bot.send_message(msg.from_user.id,joking_part.random_joke())

def choose_lang(msg):

    message = msg.text.lower()

    bot.send_message(msg.from_user.id,"ок! теперь выбери текст для перевода:")

    if message == "с английского на русский":
        bot.register_next_step_handler(msg, choose_eng_word)
    elif message == "с русского на английский":
        bot.register_next_step_handler(msg, choose_rus_word)

def choose_eng_word(msg): # choosing english word to translate in russian
    translations = translator_4bot.translate_english_to_russian(msg.text)

    res = "Вот возможные переводы слова: \n"

    for word in translations:
        res += word.text
        res += '\n'

    bot.send_message(msg.from_user.id,res)




def choose_rus_word(msg): # choosing russian word to translate in english
    translations = translator_4bot.traslate_russian_to_english(msg.text)

    res = "Вот возможные переводы слова: \n"

    for word in translations:
        res += word.text
        res += '\n'

    bot.send_message(msg.from_user.id,res)

bot.polling(none_stop=True, interval=0)