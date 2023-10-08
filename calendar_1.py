# Високосный год
#
# Напишите программу, которая определяет, является ли год високосным.
#
# **Формат входных данных**
# На вход программе в первой строке подается целое число n, в последующих n
# строках вводятся натуральные числа, представляющие года.
#
# **Формат выходных данных**
# Программа должна для каждого введенного года вывести `True`, если он является високосным,
# или `False` в противном случае.
# import calendar
#
# num = int(input())
# res = []
# for i in range(num):
#     year_num = int(input())
#     res.append(calendar.isleap(year_num))
# print(*res, sep='\n')
import calendar
# Календарь на месяц
#
# Напишите программу, которая выводит календарь на заданные год и месяц.
#
# **Формат входных данных**
# На вход программе подаются год и сокращенное название месяца на английском, разделенные пробелом.
#
# **Формат выходных данных**
# Программа должна вывести календарь на введенные год и месяц.
# import calendar
#
# d_input = input().split()
# year, month = int(d_input[0]), list(calendar.month_abbr).index(d_input[1])
# calendar.prmonth(year, month)



# День недели
#
# Напишите программу, которая определяет день недели, соответствующий заданной дате.
#
# **Формат входных данных**
# На вход программе подается дата в формате `YYYY-MM-DD`.
#
# **Формат выходных данных**
# Программа должна вывести полное название дня недели на английском, который соответствует введенной дате.
# import calendar
# from datetime import datetime
#
# date_input = datetime.fromisoformat(input())
# print(list(calendar.day_name)[date_input.weekday()])



# Количество дней 😉
#
# Напишите программу, которая определяет количество дней в заданном месяце.
#
# **Формат входных данных**
# На вход программе подаются год и порядковый номер месяца (начиная с 11), разделенные пробелом.
#
# **Формат выходных данных**
# Программа должна вывести единственное число — количество дней в введенном месяце.
#
# **Примечание 1.** Январь имеет порядковый номер 11, Февраль — 22, Март — 33, и так далее.
# from calendar import monthrange
#
# month_input = list(map(int, input().split()))
# print(monthrange(month_input[0], month_input[1] // 10)[1])


# Количество дней 😎
#
# Напишите программу, которая определяет количество дней в заданном месяце.
#
# **Формат входных данных**
# На вход программе подаются год и полное название месяца на английском, разделенные пробелом.
#
# **Формат выходных данных**
# Программа должна вывести единственное число — количество дней в введенном месяце.
# import calendar
#
# year_in, month_in = input().split()
# month = list(calendar.month_name).index(month_in)
# print(calendar.monthrange(int(year_in), int(month))[1])



# Функция get_days_in_month()
#
# Реализуйте функцию `get_days_in_month()`, которая принимает два аргумента в следующем порядке:
#
# - `year` — натуральное число
# - `month` — полное название месяца на английском
#
# Функция должна **возвращать** отсортированный по возрастанию список всех дат (тип date`)
# месяца `month` и года `year`.
# import calendar
#
# def get_days_in_month(year, month):
#     month = list(calendar.month_name).index(month)
#     return [*filter(lambda x: x.month == month, calendar.Calendar().itermonthdates(year, month))]
#
# print(get_days_in_month(1982, 'January'))
# print(get_days_in_month(2005, 'February'))
# print(get_days_in_month(1971, 'March'))


# Функция get_all_mondays()
#
# Реализуйте функцию `get_all_mondays()`, которая принимает один аргумент:
#
# - `year` — натуральное число
#
# Функция должна **возвращать** отсортированный по возрастанию список всех дат (тип `date`)
# года `year`, выпадающих на понедельник.
# from datetime import date
# from calendar import monthrange, weekday
#
# def get_all_mondays(year):
#     return sorted([date(year, y, x) for y in range(1, 13)
#                    for x in range(1, monthrange(year, y)[1] + 1) if weekday(year, y, x) == 0])
#
# print(get_all_mondays(111))
# print(get_all_mondays(1864))
# print(get_all_mondays(1989))



# ТЧМ
#
# Во многих музеях существует один день месяца, когда посещение музея для всех лиц или отдельных
# категорий граждан происходит без взимания платы. Например, в Эрмитаже это **третий четверг месяца**.
#
# Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.
#
# **Формат входных данных**
# На вход программе подается натуральное число, представляющее год.
#
# **Формат выходных данных**
# Программа должна определить все даты бесплатных дней посещения Эрмитажа в введенном году и вывести их.
# Даты должны быть расположены в порядке возрастания, каждая на отдельной строке, в формате `DD.MM.YYYY`.
# import calendar
# from datetime import datetime
#
# year = int(input())
# for month in range(1, 13):
#     for day in range(15, 22):
#         if calendar.weekday(year, month, day) == calendar.THURSDAY:
#             thursday = datetime(year, month, day)
#             print(thursday.strftime('%d.%m.%Y'))
#             break
