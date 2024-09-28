import random
import threading
import time
from threading import Thread, Lock


class Bank:
    def __init__(self, balance: int):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            number_dep = random.randint(50, 500)
            self.balance += number_dep
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение:{number_dep}. Баланас: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            number_take = random.randint(50, 500)
            print(f"Запрос на {number_take}")
            if number_take <= self.balance:
                self.balance -= number_take
                print(f'Снятие: {number_take}. Баланс: {self.balance}')
                time.sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                time.sleep(0.001)


bk = Bank(300)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
