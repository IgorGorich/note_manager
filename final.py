print('Создадим карточку читателя библиотеки')
username = input('Имя читателя ')
title = input('Наименование книги ')
autor = input('Автор книги ')
created_date = input('Дата начала чтения (день-месяц-год) ')
issue_date = input('Дата возврата книги (день-месяц-год) ')
card_book = [username, title, autor, created_date, issue_date]
print(card_book)
cont_date = input('Дата продления (день-месяц-год) ')
card_book.append(cont_date)
card_book.remove(issue_date)
print(card_book, '- книга продлина')