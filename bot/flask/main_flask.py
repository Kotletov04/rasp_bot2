from flask import Flask, render_template

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
                            day = day,
                            week = week,
                            name_lesson = name_lesson,
                            first_time = first_time,
                            last_time = last_time,
                            type_lesson = type_lesson,
                            name_lecturer = name_lecturer,
                            stream = stream,
                            auditorium = auditorium
                           )

if __name__ == '__main__':
    app.run()