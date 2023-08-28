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

        request = requests.get(f'https://portal.unn.ru/ruzapi/schedule/student/248039?start=2023.{self.first_date}&finish=2023.{self.second_date}&lng=1')
        
        soup = BeautifulSoup(request.text, 'lxml').text
        data = json.loads(soup)
        print(data)
        columns = ['auditorium', 'author', 'beginLesson', 'building', 'date', 'dayOfWeekString', 'kindOfWork', 'lecturer', 'parentschedule', 'stream', 'endLesson']
        needs_values = []
        for j in range(range_date):
            needs_values.append([data[j][i] for i in columns])
        dataframe = pd.DataFrame(np.matrix(needs_values), columns=columns)
        return dataframe
    
    def zach(password, login, semester, index_lesson):
        
        data_ = {
            'AUTH_FORM': 'Y',
            'TYPE': 'AUTH',
            'backurl': '/auth/?backurl=%2Fapp%2Fprofile%3Bmode%3Dedu%2Fmarks',
            'USER_LOGIN': login,
            'USER_PASSWORD': password,
        }
        session = requests.Session()
        
        session.post(url='https://portal.unn.ru', data=data_)
        request = session.get('https://portal.unn.ru/bitrix/vuz/api/marks2/').text
        
        data = json.loads(request)
        

        

        return data[0]['semesters'][semester]['data'][index_lesson]
        

    def news(self, login, password):
        
        au = {
            'AUTH_FORM': 'Y',
            'TYPE': 'AUTH',
            'backurl': '/auth/?backurl=%2Fapp%2Fprofile%3Bmode%3Dedu%2Fmarks',
            'USER_LOGIN': login,
            'USER_PASSWORD': password,
        }
        
        session = requests.Session()
        
        session.post(url='https://portal.unn.ru', data=au)
        request = session.get('https://portal.unn.ru/stream/')
        soup = BeautifulSoup(request.text, 'lxml')
        block = soup.find_all('div', class_="feed-item-wrap")
        for i in block:
            name = i.find('a', class_="feed-post-user-name").text
            time = i.find('div', class_="feed-post-time-wrap")
            text = i.find('div', class_='feed-post-contentview feed-post-text-block-inner')
            url = 'https://portal.unn.ru' + i.find('div', class_="feed-post-time-wrap").find('a').get('href')
            
