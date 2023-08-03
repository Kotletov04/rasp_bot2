

rasp = {
    '16 июня Пт': {
        "id": [1, 2],
        "name_lesson":['Основы теории управления', 'psy'],
        "first_time":['16:20', '18:00'],
        "last_time":['17:50', '19:00'],
        "type_lesson":['Экзамен', 'HUY'],
        "name_lecturer" :['Рушева Анна Витальевна', 'PIDOR'],
        "stream":['Поток:1422Б1УП1-OUP', 'GG'],
        "auditorium":['124 (Корпус № 10)', '1621']

    },
    '17 июня Сб':{
        "id": [1, 2],
        "name_lesson":['Основы теории управления', 'psy'],
        "first_time":['16:20', '18:00'],
        "last_time":['17:50', '19:00'],
        "type_lesson":['Экзамен', 'HUY'],
        "name_lecturer" :['Рушева Анна Витальевна', 'PIDOR'],
        "stream":['Поток:1422Б1УП1-OUP', 'GG'],
        "auditorium":['124 (Корпус № 10)', '1621']
    }
}

for i in rasp:
    print(rasp[i])
    dat = rasp[i]
    print('='*30)
    for j in dat:
        print(j ,dat[j])
        pp = dat[j]
        for k in pp:
            print(k)

    
    print('='*30)