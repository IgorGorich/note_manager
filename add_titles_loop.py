title = [] #Создаём пустой список заголовков

while True: #Запускаем цикл ввода заголовков пользователем
    title_ = input('Введите заголовок (или нажмите клавишу "Enter" для завершения):')
    title.append(title_) #Добавляем введённое значение пользователем в список
    if title_ == "": #Определяем введённое значение и если оно пустое, то завершаем ввод заголовков
        break
print(*title) #Выводим полученный список заголовков
