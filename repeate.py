# Функция hide_card()
# Реализуйте функцию hide_card(), которая принимает один аргумент:
#
# card_number — строка, представляющая собой корректный номер банковской карты из
# 16
# 16 цифр, между которыми могут присутствовать символы пробела
# Функция должна заменять первые
# 12
# 12 цифр в строке card_number на символ * и возвращать полученный результат. Если между цифрами в номере имелись символы пробела, их следует удалить.
#
#
# Sample Input 1:
#
# card = '1234567890123456'
#
# print(hide_card(card))
# Sample Output 1:
#
# ************3456
# Sample Input 2:
#
# card = '3456 9012 5678 1234'
#
# print(hide_card(card))
# Sample Output 2:
#
# ************1234
# Sample Input 3:
#
# card = '905 678123 45612 56'
#
# print(hide_card(card))
# Sample Output 3:
#
# ************1256
def hide_card(card):
    res = ''
    for i in range(12):
        res += '*'
    res += card.replace(' ', '')[-4:]
    return res


# card = '1234567890123456'
# print(hide_card(card))
# card = '3456 9012 5678 1234'
# print(hide_card(card))
# card = '905 678123 45612 56'
# print(hide_card(card))


# Функция same_parity()
# Реализуйте функцию same_parity(), которая принимает один аргумент:
#
# numbers — список целых чисел
# Функция должна возвращать новый список, элементами которого являются числа из списка numbers, имеющие ту же четность, что и первый элемент этого списка.
#
# Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.
#
# Sample Input 1:
#
# print(same_parity([]))
# Sample Output 1:
#
# []
# Sample Input 2:
#
# print(same_parity([6, 0, 67, -7, 10, -20]))
# Sample Output 2:
#
# [6, 0, 10, -20]
# Sample Input 3:
#
# print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
# Sample Output 3:
#
# [-7, 67, -9, -29]
def same_parity(nums):
    if len(nums) == 0:
        return []
    elif nums[0] % 2 == 0:
        return list(filter(lambda x: x % 2 == 0, nums))
    elif nums[0] % 2 != 0:
        return list(filter(lambda x: x % 2 != 0, nums))


# print(same_parity([]))
# print(same_parity([6, 0, 67, -7, 10, -20]))
# print(same_parity([-7, 0, 67, -9, 70, -29, 90]))