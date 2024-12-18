username = input('Напишите своё имя ')
city = input('Напишите название города, в котором вы живёте ')
street = input('Напишите название улицы, на которой вы проживаете ')
house = input('Напишите номер вашего дома ')
home_adress = [city, street, house]
print(username, 'вы проживаете по адресу', *home_adress)