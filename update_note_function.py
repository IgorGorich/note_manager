from datetime import datetime, timedelta

note = {}

while True:  # Запускаем ввод имени и его проверку на пустую запись
    note['username'] = input('Напишите имя пользователя: ')
    if note['username'] == "" or note['username'] == " ":
        print('Вы не написали имя, повторите!')
    else:
        break
note['title'] = input('Введите заголовок заметки: ')
note['content'] = input('Введите описание заметки: ')
print('Выберите статус заметки, нажав соответствующую цифру:', '1. Новая', '2. В процессе', '3. Выполнено',
      sep='\n')
while True:  # Запускаем цикл по определению статуса заметки
    status_num = input()
    if status_num == '1':
        note['status'] = 'Новая'
        break
    elif status_num == '2':
        note['status'] = 'В процессе'
        break
    elif status_num == '3':
        note['status'] = 'Выполнено'
        break
    else:  # Если значение отсутствует из предложенных, сообщаем об ошибке и просим повторить
        print('Вы неправильно выбрали статус, повторите')
created_date_str = datetime.today()
note['created_date'] = created_date_str.strftime("%d-%m-%Y")  # Дата создания = сегодняшняя дата
issue_date_str = created_date_str + timedelta(days=7)
note['issue_date'] = issue_date_str.strftime("%d-%m-%Y")  # Дедлайн через неделю от сегодняшней даты
print('Ваша заметка содержит:')

for i in note:
    print(*note[i])


def update_note():
    while True:
        print('Вы хотите обновить какое-либо поле заметки?')
        print('1. Имя', '2. Заголовок', '3. Описание', '4. Статус', '5. Дата дедлайна', sep='\n')
        marker = input('Если да, то выберите заменяемое поле, набрав соответствующую цифру: ')
        if marker == '1':
            note['username'] = input('Напишите новое имя: ')
            break
        elif marker == '2':
            note['title'] = input('Введите новый заголовок заметки: ')
            break
        elif marker == '3':
            note['content'] = input('Напишите новое описание заметки: ')
            break
        elif marker == '4':
            print('Выберите новый статус заметки, нажав соответствующую цифру:', '1. Новая', '2. В процессе',
                  '3. Выполнено',
                  sep='\n')
            while True:  # Запускаем цикл по определению статуса заметки
                status_num = input()
                if status_num == '1':
                    note['status'] = 'Новая'
                    break
                elif status_num == '2':
                    note['status'] = 'В процессе'
                    break
                elif status_num == '3':
                    note['status'] = 'Выполнено'
                    break
                else:  # Если значение отсутствует из предложенных, сообщаем об ошибке и просим повторить
                    print('Вы неправильно выбрали статус, повторите')
            break
        elif marker == '5':
            while True:
                try:
                    issue_date = input(
                        'Введите новую дату дедлайна в формате день-месяц-год ')  # Запрашиваем дату дедлайна
                    issue_date_str = datetime.strptime(issue_date, "%d-%m-%Y").date()
                    note['issue_date'] = issue_date
                    break  # Если дата корректна, то продолжаем выполнение
                except:
                    print('Дата некорректна')  # Если дата некорректна, возвращаемся и просим ввести дату дедлайна снова
            break
        else:
            print('Вы неправильно сделали выбор, повторите.')


update_note()
print('Вы обновили свою заметку!')
for i in note:
    print(*note[i])
