from datetime import datetime, timedelta

list_notes = []
note = {}


def display_notes():  # Создание функции
    while True:  # Запускаем цикл по наполнению списка заметок
        username = input('Напишите имя пользователя: ')
        if username == "" or username == " ":
            print('У вас нет сохранённых заметок.')
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
        created_date = created_date_str.strftime("%d-%m-%Y")  # Дата создания = сегодняшняя дата
        issue_date_str = created_date_str + timedelta(days=7)
        issue_date = issue_date_str.strftime("%d-%m-%Y")  # Дедлайн через неделю от сегодняшней даты
        print('Хотите добавить ещё одну заметку? (да/нет): ')  # Предлагаем пользователю создать ещё заметку
        while True:
            marker = input()
            if marker.lower() == 'нет' or marker.lower() == 'да':
                break
            else:
                print('Вы ответили некорректно, напишите "да"/"нет"')

        note = {'username': username, 'title': title, 'content': content, 'status': status,
                'created_date': created_date,
                'issue_date': issue_date}  # Создание словаря
        list_notes.append(note)  # Добавление словаря в список
        if marker.lower() == 'нет':
            break
    print('Список заметок:')
    for i, item in enumerate(list_notes, start=1):  # Итоговый вывод списка словарей
        print(f"Заметка №{i}.")
        print(f" Имя: {item['username']}")
        print(f" Заголовок: {item['title']}")
        print(f" Описание: {item['content']}")
        print(f" Статус: {item['status']}")
        print(f" Дата создания: {item['created_date']}")
        print(f" Дата дедлайна: {item['issue_date']}")
        print('--------------------------')


display_notes()
