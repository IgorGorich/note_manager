import add_titles_loop

print('Выберите новый статус заметки, нажав соответствующую цифру:', '1. Выполнено', '2. В процессе', '3. Отложено',
      sep='\n')
while True:
    status = input()  # Заносим вводимое значение пользователем в переменную status
    print('Вы установили статус:')
    if status == '1':  # Определяем значение и выводим результат, соответствующий этому значению
        print('Выполнено')
        break  # Если значение соответствует заданному, завершаем цикл while
    elif status == '2':
        print('В процессе')
        break  # Если значение соответствует заданному, завершаем цикл while
    elif status == '3':
        print('Отложено')
        break  # Если значение соответствует заданному, завершаем цикл while
    else:  # Если значение отсутствует из предложенных, сообщаем об ошибке и просим повторить
        print('Вы неправильно выбрали статус, повторите')
