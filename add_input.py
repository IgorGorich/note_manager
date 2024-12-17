username = input('Напишите своё имя ')
birthday = input('Напишите дату вашего рождения через -, например 08-06-2010 ')
year = 2024
age = year - int(birthday[6:])
print(username, 'вам в этом году исполнилось', age, 'лет')
