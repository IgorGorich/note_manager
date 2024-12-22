note = {}   #Создание словаря и последующее его наполнение
note['username'] = input('Напишите имя ')
title1 = input('Напишите подзаголовок заметки 1 ')
title2 = input('Напишите подзаголовок заметки 2 ')
title3 = input('Напишите подзаголовок заметки 3 ')
title = [title1, title2, title3]    #Создание списка из подзаголовков
note['title'] = title   #Добавление списка в словарь

note['content'] = input('Введите описание заметки ')
note['status'] = input('Введите статус заметки ')
note['created_date'] = input('Введите дату создания заметки в формате день-месяц-год ')
note['issue_date'] = input('Введите дату истечения заметки в формате день-месяц-год ')

print('Имя пользователя' , note['username'])
print('Заголовки заметки' , note['title'])
print('Описание заметки' , note['content'])
print('Статус заметки' , note['status'])
print('Дата создания заметки' , note['created_date'])
print('Дата истечения заметки' , note['issue_date'])