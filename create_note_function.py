from datetime import datetime, timedelta


def create_note():  # Создание функции по наполнению словаря из заметок
    note = {}

    while True:  # Запускаем ввод имени и его проверку на пустую запись
        username = input('Напишите имя пользователя: ')
        if username == "" or username == " ":
            print('Вы не написали имя, повторите!')
        else:
            break
    title = input('Введите заголовок заметки: ')
    content = input('Введите описание заметки: ')
    print('Выберите статус заметки, нажав соответствующую цифру:', '1. Новая', '2. В процессе', '3. Выполнено',
          sep='\n')
    while True:  # Запускаем цикл по определению статуса заметки
        status_num = input()
        if status_num == '1':
            status = 'Новая'
            break
        elif status_num == '2':
            status = 'В процессе'
            break
        elif status_num == '3':
            status = 'Выполнено'
            break
        else:  # Если значение отсутствует из предложенных, сообщаем об ошибке и просим повторить
            print('Вы неправильно выбрали статус, повторите')
    created_date_str = datetime.today()
    created_date = created_date_str.strftime("%d-%m-%Y")  # Присвоение переменной created_date сегодняшней даты
    issue_date_str = created_date_str + timedelta(days=7)
    issue_date = issue_date_str.strftime("%d-%m-%Y")  # Дедлайн через неделю от сегодняшней даты

    note = {'username': username, 'title': title, 'content': content, 'status': status, 'created_date': created_date,
            'issue_date': issue_date}  # Наполнение словаря из полученных данных
    print('Заметка создана:', note, sep='\n')  # Вывод полученной заметки


create_note()
