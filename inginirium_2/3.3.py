#Задействуем фреймворк рандом
import random

#Создаём список с моедлями машин
cars = ['Mercedes', 'KIA', 'LADA', 'Tesla', 'Hyundai', 'Wolksvagen']

#Создаём переменную в которой находится случайное число для выбора модели
a = random.randint(0,5)

#Выводим модель
print(cars[a])