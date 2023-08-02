from handlers.actions import *
from aiogram import executor
#from data.analitics_db import Bot_DB



#Bot_DB = Bot_DB('data/shelter/date.db')

if __name__ == '__main__':
    executor.start_polling(DP)