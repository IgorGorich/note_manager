from datetime import datetime

list_notes = []  # Создание пустого списка из словарей
print('Добро пожаловать в "Менеджер заметок"!')
while True:  # Начинаем цикл запросов по наполнению словарей у пользователя
    username = input('Напишите имя пользователя: ')
    title = input('Введите заголовок заметки: ')
    content = input('Введите описание заметки ')
    print('Выберите статус заметки, нажав соответствующую цифру:', '1. Новая', '2. В процессе', '3. Выполнено',
          sep='\n')
    while True:  # Запускаем цикл по определению статуса заметки
        status_num = input()
        if status_num == '1':
            status = ('Новая')
            break
        elif status_num == '2':
            status = ('В процессе')
            break
        elif status_num == '3':
            status = ('Выполнено')
            break
        else:  # Если значение отсутствует из предложенных, сообщаем об ошибке и просим повторить
            print('Вы неправильно выбрали статус, повторите')
    while True:  # Запускаем цикл по корректному вводу даты создания
        try:
            created_date = input('Введите дату создания (день-месяц-год) ')
            created_date_1 = datetime.strptime(created_date, "%d-%m-%Y").date()
            break
        except:
            print('Дата некорректна')
    while True:  # Запускаем цикл по корректному вводу даты дедлайна
        try:
            issue_date = input('Введите дату дедлайна (день-месяц-год) ')
            issue_date_1 = datetime.strptime(issue_date, "%d-%m-%Y").date()
            break
        except:
            print('Дата некорректна')
    print('Хотите добавить ещё одну заметку? (да/нет): ')  # Предлагаем пользователю создать ещё заметку
    while True:
        marker = input()
        if marker == 'нет' or marker == 'да':
            break
        else:
            print('Вы ответили некорректно, напишите "да"/"нет"')
    note = {'username': username, 'title': title, 'content': content, 'status': status, 'created_date': created_date,
            'issue_date': issue_date}  # Создание словаря
    list_notes.append(note)  # Добавление словаря в список
    if marker == 'нет':
        break
print(*list_notes, sep='\n')  # Итоговый вывод списка словарей
