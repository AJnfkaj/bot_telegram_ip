import telebot
from datetime import datetime
import backend

bot = telebot.TeleBot('5228977375:AAH1I_53-pqhaVk_sAjwp_Wzyz5UK_r4or4')
start_station = ""
finish_station = ""


def answ_hello(message):
    current_datetime = datetime.now()
    a = current_datetime.hour
    mess = ""
    if 6 <= a <= 12:
        mess = (" Доброе утро, я твой навигатор, помочь добраться до остановки?")
    elif 13 <= a < 17:
        mess = (" Добрый день, я твой навигатор, помочь добраться до остановки?")

    elif 17 <= a <= 24:
        mess = (" Добрый вечер, я твой навигатор, помочь добраться до остановки?")
    else:
        mess = (" Доброй ночи, я твой навигатор, помочь добраться до остановки?")

    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row("Да")
    bot.send_message(message.from_user.id, mess, reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def hello(message):
    if message.text == "Привет":
        answ_hello(message)
        bot.register_next_step_handler(message, get_answer_hello)
    else:
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Привет")
        bot.send_message(message.from_user.id, "Напиши привет", reply_markup=user_markup)


def get_answer_hello(message):
    if message.text == "Да":
        bot.send_message(message.from_user.id, "На какой остановке вы находитесь?")
        bot.register_next_step_handler(message, get_start_station)


def get_start_station(message):
    global start_station
    start_station = message.text
    """ сделать проверку есть ли такая станция в базе!!!"""
    if backend.check_ost(start_station):
        bot.send_message(message.from_user.id, "На какую остановку вам надо?")
        bot.register_next_step_handler(message, get_finish_station)
    else:
        bot.send_message(message.from_user.id, "Остановки нет в базе \nВведите остановку корректно еще раз:")
        bot.register_next_step_handler(message, get_start_station)


def get_finish_station(message):
    global finish_station
    finish_station = message.text
    if backend.check_ost(finish_station):
        finish_station = message.text
        final(message)
    else:
        bot.send_message(message.from_user.id, "Остановки нет в базе \nВведите остановку корректно еще раз:")
        bot.register_next_step_handler(message, get_finish_station)


def final(message):
    answer = backend.main(start_station, finish_station)
    bot.send_message(message.from_user.id, answer)


bot.polling(none_stop=True, interval=0)
