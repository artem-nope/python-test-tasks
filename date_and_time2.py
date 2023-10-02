# Вам доступно время `alarm`. Дополните приведенный ниже код, чтобы он вывел следующие его компоненты:
#
# - количество часов в формате `HH`
# - количество минут в формате `MM`
# - количество секунд в формате `SS`
# from datetime import time
#
# alarm = time(7, 30, 25)
#
# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))


# Вам доступна дата `birthday`. Дополните приведенный ниже код, чтобы он вывел следующие её компоненты:
#
# - полное название месяца на английском
# - полное название дня недели на английском
# - год в формате `YYYY`
# - номер месяца в формате `MM`
# - день месяца в формате `DD`
# from datetime import date
#
# birthday = date(1992, 10, 6)
#
# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))


# Ураган Эндрю, который обрушился на Флориду 24 августа 1992 года, был одним из самых дорогостоящих
#и смертоносных ураганов в истории США. Дополните приведенный ниже код, чтобы он вывел дату 24 августа 1992 года
# в трех различных форматах:
#
# - в формате `YYYY-MM`
# - в формате `month_name (YYYY)`, где `month_name` – полное название месяца на английском
# - в формате `YYYY-day_number`, где `day_number` – день года
# from datetime import date
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%d'))   # выводим дату в формате YYYY-day_number


# from datetime import date, time
#
# day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')
# hour, minute, second = input('Введите время в формате ЧЧ:ММ:СС').split(':')
#
# my_date = date(int(year), int(month), int(day))        # создаем объект типа date
# my_time = time(int(hour), int(minute), int(second))    # создаем объект типа time
#
# print(my_date)
# print(my_time)


# Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.
#
# **Формат входных данных**
# На вход программе подаются две корректные даты в ISO формате (`YYYY-MM-DD`), каждая на отдельной строке.
#
# **Формат выходных данных**
# Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате `DD-MM (YYYY)`.
# from datetime import date
#
# year1, month1, day1 = input('Введите первую дату в формате YYYY-MM-DD: ').split('-')
# year2, month2, day2 = input('Введите вторую дату в формате YYYY-MM-DD: ').split('-')
#
# d1 = date(int(year1), int(month1), int(day1))
# d2 = date(int(year2), int(month2), int(day2))
#
# if d1 < d2:
#     print(d1.strftime('%d-%m (%Y)'))
# elif d2 < d1:
#     print(d2.strftime('%d-%m (%Y)'))


# Отсортированные даты
#
# Напишите программу, которая принимает на вход последовательность дат и выводит их в порядке неубывания.
#
# **Формат входных данных**
# На вход программе подается натуральное число n, а затем n корректных дат в ISO формате (`YYYY-MM-DD`),
# каждая на отдельной строке.
#
# **Формат выходных данных**
# Программа должна вывести введенные даты в порядке неубывания, каждую на отдельной строке, в формате `DD/MM/YYYY`.
#
# **Примечание 1.** Последовательность называется неубывающей,
# если каждый ее следующий член не меньше предыдущего, например:1,1,2,3,4,4,4,5,6,...1,1,2,3,4,4,4,5,6,...
#
# Обратите внимание, что такая последовательность не является возрастающей.
# from datetime import date
#
# n = int(input())
# date_lst = []
# for i in range(n):
#     year, month, day = input('Enter a date(`YYYY-MM-DD`): ').split('-')
#     dt = date(int(year), int(month), int(day))
#     date_lst.append(dt)
# res_lst = sorted(date_lst)
# for i in res_lst:
#     print(i.strftime('%d/%m/%Y'))


# Функция print_good_dates()
#
# Тимур считает дату «интересной», если её год совпадает с годом его рождения,
# а сумма номера месяца и номера дня равна его возрасту. Год рождения Тимура — 1992, возраст — 29 лет.
#
# Реализуйте функцию `print_good_dates()`, которая принимает один аргумент:
#
# - `dates` — список дат (тип `date`)
#
# Функция должна **выводить** «интересные» даты в порядке возрастания, каждую на отдельной строке,
# в формате `month_name DD, YYYY`, где `month_name` — полное название месяца на английском.
#
# **Примечание 1.** Если в функцию передается пустой список или список без интересных дат,
# функция ничего не должна выводить.
from datetime import date
# def print_good_dates(dates):
#     dt_lst = []
#     for dt in dates:
#         if dt.year == 1992 and dt.day + dt.month == 29:
#             dt_lst.append(dt)
#     for i in sorted(dt_lst):
#         print(i.strftime('%B %d, %Y'))
# dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
# print_good_dates(dates)
# dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
# print_good_dates(dates)
# print_good_dates([])
# dates = [date(1992, 9, 20), date(1992, 8, 21), date(1992, 7, 22), date(1992, 10, 19)]
# print_good_dates(dates)
# print(print_good_dates([]))


# Функция is_correct()
#
# Реализуйте функцию `is_correct()`, которая принимает три аргумента в следующем порядке:
#
# - `day` — натуральное число, день
# - `month` — натуральное число, месяц
# - `year` — натуральное число, год
#
# Функция должна возвращать `True`, если дата с компонентами `day`, `month` и `year` является корректной,
# или `False` в противном случае.
#
# **Примечание 1.** Вспомните про конструкцию`try-except`.
from datetime import date

def is_correct(day, month, year):
    try:
        dt = date(int(year), int(month), int(day))
        return True
    except:
        return False
#
# print(is_correct(31, 12, 2021))
# print(is_correct(31, 13, 2021))
# print(is_correct(32, 10, 2021))


#  Корректные даты
#
# Напишите программу, которая принимает на вход последовательность дат и проверяет каждую из них на корректность.
#
# **Формат входных данных**
# На вход программе подается последовательность дат в формате `DD.MM.YYYY`, каждая на отдельной строке.
# Концом последовательности является слово `end`.
#
# **Формат выходных данных**
# Программа должна для каждой введенной даты вывести текст `Корректная` или `Некорректная`
# в зависимости от того, является ли дата корректной, а затем вывести количество корректных дат.
#
# **Примечание 1.** Для анализа даты на корректность можете использовать уже реализованную функцию `is_correct()`
# из предыдущей задачи.

dt_lst = []
correct_cnt = 0
while True:
    dt_in = input()
    if dt_in == 'end':
        break
    dt_lst.append(dt_in)
for d in dt_lst:
    day, month, year = d.split('.')
    if is_correct(day, month, year):
        correct_cnt += 1
        print('Корректная')
    else:
        print('Некорректная')
print(correct_cnt)