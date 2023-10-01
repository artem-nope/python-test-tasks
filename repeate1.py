# Тема 1. Змінна. Типи даних. Ввід даних. Вивід даних. Оператори
#
# Задача 1
# Створити змінні які будуть містити модель, рік, та колір автомобіля. Повернути всі змінні записані через знак -
# Наприклад
# Программа повертає(audi-1998-red)
#
# model, year, color = input(), input(), input()
# print(model + '-' + year + '-' + color)


# Задача 2
# Прийняти в користувача два слова які помістити в змінні element_1 та element_2
# Повернути інформацію в одній строці але спочатку показати element_2 а потім  element_1
#
# Наприклад
# Вхідні дані:
# Користувач передав Hello Alex
# Программа повертає Alex Hello
#
# element_1, element_2 = input().split()
# print(element_2 + ' ' + element_1)


# Задача 3
# Прийняти в користувача такі змінні як number1, number2, number3
# Перемножити ці елементи
#
# Наприклад
# Вхідні дані:
# number1 - 10
# number2 - 4
# number3 - 2
# Программа повертає 80
#
# number1 = int(input('number1 - '))
# number2 = int(input('number2 - '))
# number3 = int(input('number3 - '))
# print(number1 * number2 * number3)


# Задача 4
# Прийняти в користувача число та звільшити його в 2 рази
#
# Наприклад
# Вхідні дані 4
# Программа повертає 8
#
# num = int(input('Вхідні дані '))
# print(f'Результат {num * 2}')


# Задача 5
# Прийняти два числа number1 та number2 потрібно поділити number1 на number2.
#
# Наприклад:
# Вхідні дані
# number1 - 10
# number2 - 2
# Программа повертає 5
#
# number1 = int(input('number1 - '))
# number2 = int(input('number2 - '))
# print(number1 // number2)


# Задача 6
# Створити змінні str, int, float, bool та вивести їх в одну строку через *
#
# Наприклад:
# Программа повертає: Hello*10*6.5*True
#
# str_in = input()
# int_in = int(input())
# float_in = float(input())
# bool_in = bool(input())
# print(str_in, str(int_in), str(float_in), str(bool_in), sep='*')



# Тема 2. Робота з строками. Робота з списками. Умовні конструкції.
#
# Задача 1. Прийняти в користувача слово та показати довжину цього слова
# str_in = input()
# print(len(str_in))
#
#
# Задача 2. Прийняти в користувача слово та підрахувати кількість символів m
# str_in = input()
# print(str_in.count('m'))
#
#
# Задача 3. Дано список з числами показати перший та останній елемент списку через *
# lst = [1, 2, 5, 12, 18, 100, 0]
# print(f'{lst[0]}*{lst[-1]}')
#
#
# Задача 4. Дано список слів підрахувати кількість слів Hello
# lst = ['Hello', 'Holla', 'Hi', 'Hello', 'Hi', 'Hello', 'Hello']
# print(lst.count('Hello'))
#
#
# Задача 5. Прийняти в користувача слово та замінити всі літери m на *
# str_in = input()
# print(str_in.replace('m', '*'))
#
#
# Задача 6. Задано порожній список необхідно додати до нього 2 елемента “Hello” та Natali
# lst = []
# lst.append('Hello')
# lst.append('Natali')
# print(lst)
#
#
# Задача 7. Задано список [1,2,3,4,5,1,5,5,1] потрібно видалити перше входження числа 5
# lst = [1,2,3,4,5,1,5,5,1]
# lst.remove(5)
# print(lst)
#
#
# Задача 8. Задано список [1,2,3,4,5,6,7,8] потрібно 5 елемент замінити на *
# lst = [1,2,3,4,5,6,7,8, 5, 1, 5]
# print(list(''.join(list(map(str, lst))).replace('5', '*')))
# for i in range(len(lst)):
#     if lst[i] == 5:
#         lst[i] = '*'
#         break
# print(lst)
#
#
# Задача 9. Задано список  [1,2,3] потрібно видалити число 2 по індексу
# lst = [1,2,3]
# lst.pop(lst.index(2))
# print(lst)
#
#
# Задача 10. Задано два слова якщо вони співпадають показати yes
# str1 = input()
# str2 = input()
# if str1 == str2:
#     print('yes')
# else:
#     print('no')
#
#
# Задача 11. Задано слово якщо в слові міститься буква k то показати yes інакше no
# str_in = input()
# if 'k' in str_in:
#     print('yes')
# else:
#     print('no')
#
#
# Задача 12. Задано слово якщо перша літера така сама як остання літера показати yes
# str_in = input()
# if str_in[0] == str_in[-1]:
#     print('yes')
# else:
#     print('no')
#
#
# Задача 13. Задано два числа показати яке з них більше для перевірки використовується знак (>)
# num1 = int(input())
# num2 = int(input())
# if num1 > num2:
#     print(num1)
# elif num1 < num2:
#     print(num2)
# else:
#     print('equals')
#
#
# Задано 14. Задано слово якщо слово містить одночасно букви x, t, g то показати yes
# str_in = input()
# if 'x' in str_in and 't' in str_in and 'g' in str_in:
#     print('yes')
# else:
#     print('no')
#
#
# Задача 15. Задано слово якщо остання літера m або M то показати Yes
# str_in = input()
# if str_in[-1] == 'm' or str_in[-1] == 'M':
#     print('yes')
# else:
#     print('no')
