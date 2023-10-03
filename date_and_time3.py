# Дополните приведенный ниже код, чтобы в переменной `dt` содержался объект типа `datetime` с датой и временем, которые указаны в строке `text`.
#
# **Примечание.** Дата, указанная в строке `text`, записана в формате `DD.MM.YYYY`, а время — в формате `HH:MM`
# from datetime import datetime
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(dt)


# Дополните приведенный ниже код, чтобы он преобразовал секунды `seconds` (прошедшие от начала эпохи) в объект `datetime`
# и, наоборот, объект `datetime` в секунды (прошедшие от начала эпохи).
# from datetime import datetime
# seconds = 2483228800
# dt = datetime(2011, 11, 4)
# print(datetime.fromtimestamp(seconds))
# print(dt.timestamp())


# Вам доступен список `times_of_purchases`, содержащий даты (тип `datetime`), в
# которые были совершены покупки в некотором интернет-магазине. Дополните приведенный ниже код,
# чтобы он вывел текст `До полудня`, если большее число покупок было совершено до полудня, или текст
# `После полудня` в противном случае.
#
# **Примечание 1.** Гарантируется, что ни одна покупка не была совершена ровно в `12:00:00`.
#
# **Примечание 2.** Гарантируется, что до полудня и после полудня совершено различное количество покуп
# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25),
#                       datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57),
#                       datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10),
#                       datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45),
#                       datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48),
#                       datetime(2017, 10, 2, 12, 45, 5)]
# am_cnt = 0
# pm_cnt = 0
# for d in times_of_purchases:
#     if d.hour > 11:
#         pm_cnt += 1
#     else:
#         am_cnt += 1
#
# if am_cnt > pm_cnt:
#     print('До полудня')
# else:
#     print('После полудня')
#
# dts = [d.strftime('%p') for d in times_of_purchases]
# print(['До полудня', 'После полудня'][dts.count('PM') > dts.count('AM')])


# Вам доступны список `dates`, содержащий даты, и список `times`, содержащий времена. Количество элементов
# в этих списках одинаковое. Дополните приведенный ниже код, чтобы он вывел `datetime` объекты,
# полученные путем объединения элементов списков `dates` и `times`, находящихся на одинаковых позициях.
# Полученные объекты должны быть расположены в порядке возрастания секунд, каждый на отдельной строке.
#
# **Примечание 1.** Например, если бы списки `dates` и `times` имели вид:
#
# dates = [date(2020, 11, 12), date(2021, 7, 2), date(2020, 9, 25)]
# times = [time(12, 50, 22), time(12, 19, 1), time(7, 30, 1)]
#
# то программа должна была бы вывести:
#
# 2021-07-02 12:19:01
# 2020-09-25 07:30:01
# 2020-11-12 12:50:22
#
# **Примечание 2.** Если объекты имеют равное количество секунд, то следует сохранить их исходный порядок.
# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11),
#          date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24),
#          date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14),
#          date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10),
#          time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57),
#          time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10),
#          time(17, 55, 40), time(9, 14, 9)]
#
# datetimes = [datetime.combine(d, t) for d, t in zip(dates, times)]
#
# print(*sorted(datetimes, key=lambda x: x.second), sep='\n')


# Ученики онлайн-школы решили выяснить, кто из них быстрее всех решит домашнее задание по математике.
# Для этого каждый ученик зафиксировал время начала и окончания решения своей домашней работы.
#
# Вам доступен словарь `data`, содержащий результаты учеников.
# Ключом в словаре является имя ученика, а значением — кортеж, первый элемент которого —
# время начала решения, второй элемент — время окончания решения. Дополните приведенный ниже код,
# чтобы он вывел имя ученика, который затратил на решение домашнего задания меньше всего времени.
#
# **Примечание 1.** Гарантируется, что искомый ученик единственный.
#
# **Примечание 2.** Дата-времена в кортежах представлены в виде строк в формате `DD.MM.YYYY HH:MM:SS`.
# from datetime import datetime
#
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
#
# dates = {}
#
# for k, v in data.items():
#     dt1 = datetime.strptime(v[0], '%d.%m.%Y %H:%M:%S')
#     dt2 = datetime.strptime(v[1], '%d.%m.%Y %H:%M:%S')
#     dates[k] = (dt2 - dt1).seconds
#
# print(sorted(dates.items(), key=lambda x: x[1])[0][0])


# Дневник космонавта
#
# Вам доступен текстовый файл `diary.txt`, в который космонавт записывал небольшие отчёты за день.
# Каждый новый отчёт он мог записать либо в начало файла, либо в середину, либо в конец.
# Все отчеты разделены между собой пустой строкой. Каждый новый отчёт начинается со строки с датой
# и временем в формате `DD.MM.YYYY; HH:MM`, после которой следуют события, произошедшие за указанный день:
#
# 29.04.2006; 06:55
# It wasn’t until several hours after launch that we were able to take the time to get out of our seats
# and enter the “habitation module.”
# Then, after another orbital maneuver, we finally were able to take a several hour break and get a little sleep.
#
# 03.05.2006; 20:24
# Everybody had a sleeping bag although I only used mine on a couple of brief occasions,
# and then only when getting a little chilly.
#
#
# Напишите программу, которая расставляет все записи космонавта в хронологическом порядке
# и выводит полученный результат.
# from datetime import datetime
#
# with open('diary.txt', encoding="utf-8") as f:
#     print(*sorted(f.read().split('\n\n'),
#                 key=lambda t: datetime.strptime(t.split('\n')[0], '%d.%m.%Y; %H:%M')),
#                 sep='\n\n')
