from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types.web_app_info import WebAppInfo
import configparser
from parser.parser import Parser
#from main import Bot_DB



import datetime
from datetime import timedelta
import pandas as pd



URL = configparser.ConfigParser().read('URL')
TOKEN = configparser.ConfigParser().read('TOKEN')
HELP_COMMANDS = configparser.ConfigParser().read('COMMANDS')


BOT = Bot(TOKEN)
DP = Dispatcher(BOT)


    


@DP.message_handler(commands=['start'])
async def start_command(message: types.Message):  
    
    buttons = [
        [
            types.KeyboardButton(text='Сегодня'),
            types.KeyboardButton(text='Завтра'),
            types.KeyboardButton(text='Расписание', web_app=WebAppInfo(url=URL)),   
        ],

        [
            types.KeyboardButton(text='Анекдоты точка ру'),
            types.KeyboardButton(text='Зачетка'),
            types.KeyboardButton(text='Новости')
        ],

        [
            types.KeyboardButton(text='Настройки')
            ]
    ]
    
    markup = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer(text='Привет', reply_markup=markup)
    await message.delete()

@DP.message_handler(commands=['help'])
async def help_comamnd(message: types.Message):
    await message.reply(text=HELP_COMMANDS)

@DP.message_handler(filters.Text(equals='Сегодня'))
async def today_button(message: types.Message):
    #Bot_DB.add_name(user_id=message.from_user.id, name=message.from_user.full_name, button='Сегодня', time=datetime.datetime.now())
    
    dataframe = Parser(first_date='06.12', second_date='06.20').rasp()
    date = datetime.datetime.now()
    raspisaniye = dataframe[dataframe['date'] == date.date().strftime("%Y.%m.%d")]
    lecturer = raspisaniye['lecturer'].tolist()
    week = raspisaniye['dayOfWeekString'].tolist()
    date = raspisaniye['date'].tolist()
    time_first = raspisaniye['beginLesson'].tolist()
    time_last = raspisaniye['endLesson'].tolist()
    building = raspisaniye['building']
    type = raspisaniye['kindOfWork'].tolist()
    auditorium = raspisaniye['auditorium'].tolist()
    if raspisaniye.empty:
        await message.answer(text='Нет занятий')
    else:
        text_list = 'Расписание на сегодня:\n'
        for i, j, k, t_f, w, ty, t_l, bu in zip(lecturer, date, auditorium, time_first, week, type, time_last ,building):
            text = f'\nПреподаватель {i} \nДата занятия {j} ({w}) \nАудитория ({bu}) {k} \nВремя {t_f} - {t_l} \nТип занятия: {ty} \n'
            text_list = text_list+text
        await message.answer(text=text_list)

@DP.message_handler(filters.Text(equals='Завтра'))
async def today_button(message: types.Message):
    #Bot_DB.add_name(user_id=message.from_user.id, name=message.from_user.full_name, button='Завтра', time=datetime.datetime.now())

    dataframe = Parser(first_date='06.12', second_date='06.20').rasp()
    date = datetime.datetime.now() + timedelta(days=1)
    raspisaniye = dataframe[dataframe['date'] == date.date().strftime("%Y.%m.%d")]
    lecturer = raspisaniye['lecturer'].tolist()
    week = raspisaniye['dayOfWeekString'].tolist()
    date = raspisaniye['date'].tolist()
    time_first = raspisaniye['beginLesson'].tolist()
    time_last = raspisaniye['endLesson'].tolist()
    building = raspisaniye['building']
    type = raspisaniye['kindOfWork'].tolist()
    auditorium = raspisaniye['auditorium'].tolist()
    if raspisaniye.empty:
        await message.answer(text='Нет занятий')
    else:
        text_list = 'Расписание на завтра:\n'
        for i, j, k, t_f, w, ty, t_l, bu in zip(lecturer, date, auditorium, time_first, week, type, time_last ,building):
            text = f'\nПреподаватель: {i} \nДата занятия: {j} ({w}) \nАудитория: ({bu}) {k} \nВремя: {t_f} - {t_l} \nТип занятия: {ty} \n'
            text_list = text_list+text
        await message.answer(text=text_list)

@DP.message_handler(filters.Text(equals='Зачетка'))
async def test(message: types.Message):
    #Bot_DB.add_name(user_id=message.from_user.id, name=message.from_user.full_name, button='Зачетка', time=datetime.datetime.now())


    await message.answer(text='text')


@DP.message_handler(filters.Text(equals='Настройки'))
async def test(message: types.Message):
    buttons = [
        [
            types.KeyboardButton(text='Выбрать период расписания'),
            types.KeyboardButton(text='Выбрать тему расписания'),
            types.KeyboardButton(text='Включить/Отключить рассылку')

         ],

         [
            types.KeyboardButton(text='Назад'),
         ],
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer(text='Привет', reply_markup=markup)
    













