import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import numpy as np




class Parser:

    def __init__(self, first_date, second_date) -> None:
        self.first_date = first_date
        self.second_date = second_date

    def rasp(self):
    
        #first_date = '06.12'
        #second_date = '06.20'
        range_date = int(self.second_date[-2:]) - int(self.first_date[-2:]) 

        request = requests.get(f'https://portal.unn.ru/ruzapi/schedule/student/206242?start=2023.{self.first_date}&finish=2023.{self.second_date}&lng=1')

        soup = BeautifulSoup(request.text, 'lxml').text
        data = json.loads(soup)
        columns = ['auditorium', 'author', 'beginLesson', 'building', 'date', 'dayOfWeekString', 'kindOfWork', 'lecturer', 'parentschedule', 'stream', 'endLesson']
        needs_values = []
        for j in range(range_date):
            needs_values.append([data[j][i] for i in columns])
        dataframe = pd.DataFrame(np.matrix(needs_values), columns=columns)
        return dataframe