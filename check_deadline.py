from datetime import datetime

print('Текущая дата:', datetime.today().strftime("%d-%m-%Y"))  # Выводим сегодняшнюю дату
while True:
    try:
        issue_date = input('Введите дату дедлайна в формате день-месяц-год ')  # Запрашиваем дату дедлайна
        issue_date_1 = datetime.strptime(issue_date, "%d-%m-%Y").date()
        break  # Если дата корректна, то продолжаем выполнение с 11-й строки
    except:
        print('Дата некорректна')  # Если дата некорректна, возвращаемся и просим ввести дату дедлайна снова
days = (issue_date_1 - datetime.today().date()).days  # Находим разницу в днях между датами
if days == 0:
    print('Дедлайн истекает сегодня!')
elif days < 0:
    print('Внимание! Дедлайн истёк', abs(days), 'дней назад!')
elif days > 0:
    print('Осталось дней до дедлайна:', days)
