# Модуль threading
#
# В основном треде создать переменную daddys_money = 100
# и в цикле прибавлять к ней 1000 каждые 2 секунды 10 раз
# выводя сообщение типа:
# "папа получил 1000 грн и теперь у него 1100 грн"
#
# Создать класс- наследник Thread с названием MoneyWaster
# и полями name и money = 0
#
# Создать три объекта этого класса в основном треде - мама, сын и дочь
# с соответствующими именами
#
# После запуска они через случайные интервалы времени (1-3 сек.)
# случайно выбирают сумму, которую хотят получить
# от папы (500-2000),
# если у папы нет столько (daddys_money), то выводим сообщение типа
# "доча хочет 720 грн, но фигушки"
#
# если у папы есть столько, то daddys_money уменьшается на эту сумму,
# поле money объекта соответственно увеличивается на эту же сумму
# и сообщение типа:
# "мама получила от папы 720 грн, и теперь у нее 1254 грн"
#
# Когда закончится цикл папы в основном треде, нужно
# вывести сообщение "папа денег больше не дает"
# сообщить об этом нашим тредам-хотелкам, чтобы они завершили работу
# и попрощались "мама говорит пока-пока с 3420 грн на кармане"

from threading import current_thread, Thread
import time
import random

daddys_money = 100
N = 10
is_gives = True


class MoneyWaster(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.money = 0

    def run(self):
        global daddys_money
        while True:
            tm = random.randint(1, 3)
            mon = random.randint(500, 2000)
            time.sleep(tm)
            if is_gives:
                if mon > daddys_money:
                    print(f'{current_thread().name} хочет {mon} грн, но фигушки\n', end='')
                else:
                    daddys_money -= mon
                    self.money += mon
                    print(f'{current_thread().name} получила от папы {mon} грн, и теперь у нее {self.money} грн\n', end='')
            else:
                print(f'{current_thread().name} говорит пока-пока с {self.money} грн на кармане')
                break


def add1000(n):
    global daddys_money
    global is_gives
    while True:
        if n > 0:
            n -= 1
            daddys_money += 1000
            time.sleep(2)
            print(f'папа получил 1000 грн и теперь у него {daddys_money} грн')
        else:
            is_gives = False
            print('папа денег больше не дает')
            break


if __name__ == '__main__':
    t = Thread(target=add1000, args=[N])
    # t.start()
    t1 = MoneyWaster('Mom')
    t2 = MoneyWaster('Son')
    t3 = MoneyWaster('Daughter')
    threads = [t, t1, t2, t3]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
