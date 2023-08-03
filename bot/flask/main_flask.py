from flask import Flask, render_template


rasp = {
    '16 июня Пт': {
        'power_lesson': 2,
        "name_lesson":['Основы теории управления', 'psy'],
        "first_time":['16:20', '18:00'],
        "last_time":['17:50', '19:00'],
        "type_lesson":['Экзамен', 'HUY'],
        "name_lecturer" :['Рушева Анна Витальевна', 'PIDOR'],
        "stream":['Поток:1422Б1УП1-OUP', 'GG'],
        "auditorium":['124 (Корпус № 10)', '1621']

    },
    '17 июня Сб':{
        'power_lesson': 2,
        "name_lesson":['Основы теории управления', 'psy'],
        "first_time":['16:20', '18:00'],
        "last_time":['17:50', '19:00'],
        "type_lesson":['Экзамен', 'HUY'],
        "name_lecturer" :['Рушева Анна Витальевна', 'PIDOR'],
        "stream":['Поток:1422Б1УП1-OUP', 'GG'],
        "auditorium":['124 (Корпус № 10)', '1621']
    }
}
id = [1, 2, 3, 4]
day = '16 июня'
week = 'Пт'
name_lesson = 'Основы теории управления'
first_time = '16:20'
last_time = '17:50'
type_lesson = 'Экзамен'
name_lecturer = 'Рушева Анна Витальевна'
stream = 'Поток:1422Б1УП1-OUP'
auditorium = '124 (Корпус № 10)'

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('rasp.html',
                            rasp = rasp
                           )

if __name__ == '__main__':
    app.run()