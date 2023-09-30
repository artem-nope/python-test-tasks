# Реализуйте функцию get_min_max()`, которая принимает один аргумент:
#
# - `dates`— список дат (тип`date`)
#
# Функция должна возвращать кортеж, первым элементом которого является
# минимальная дата из списка `dates`, вторым— максимальная дата из списка`dates`.
# сли список`dates` пуст, функция должна вернуть пустой кортеж.
#
from datetime import date
def get_min_max(dates):
    if len(dates) == 0:
        return ()
    else:
        return (min(dates), max(dates))

# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
# print(get_min_max(dates))

# print(get_min_max([]))



# Реализуйте функцию`get_date_range()`, которая принимает два аргумента в следующем порядке:
#
# - `start` — начальная дата, тип `date`
# - `end` — конечная дата, тип `date`
#
# Функция `get_date_range()` должна возвращать список, состоящий из дат
# (тип `date`) от `start` до `end` включительно. Если `start > end`, функция должна вернуть пустой список.
from datetime import date
import datetime
def get_date_range(start, end):
    if start > end:
        return []
    else:
        res = []
        curr_date = start
        while curr_date <= end:
            res.append(curr_date)
            curr_date += datetime.timedelta(days=1)
        return res
# date1 = date(2021, 10, 1)
# date2 = date(2021, 10, 5)
#
# print(*get_date_range(date1, date2), sep='\n')

# date1 = date(2019, 6, 5)
# date2 = date(2019, 6, 5)
#
# print(get_date_range(date1, date2))

# date1 = date(2025, 6, 5)
# date2 = date(2022, 6, 6)
# print(len(get_date_range(date1, date2)))



# Реализуйте функцию `saturdays_between_two_dates()`, которая принимает два аргумента в следующем порядке:
#
# - `start` — начальная дата, тип `date`
# - `end` — конечная дата, тип `date`
#
# Функция должна возвращать количество суббот между датами `start` и `end` включительно.
#
# **Примечание 1.**Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.

def saturdays_between_two_dates(start, end):
    saturday_cnt = 0
    if start > end:
        start, end = end, start
    w_days = []
    curr_date = start
    while curr_date <= end:
        w_days.append(curr_date)
        curr_date += datetime.timedelta(days=1)
    for dt in w_days:
        if dt.weekday() == 6:
            saturday_cnt += 1

    return saturday_cnt

# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)
#
# print(saturdays_between_two_dates(date1, date2))
# date1 = date(2020, 7, 26)
# date2 = date(2020, 7, 2)
#
# print(saturdays_between_two_dates(date1, date2))
# date1 = date(2018, 7, 13)
# date2 = date(2018, 7, 13)
#
# print(saturdays_between_two_dates(date1, date2))