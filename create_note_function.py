from datetime import datetime, timedelta

note = {}


def create_note():  # Создание функции по наполнению словаря из заметок

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


create_note()
