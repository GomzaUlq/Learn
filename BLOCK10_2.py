import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy = 100
        days = 0
        print(f'{self.name}, на нас напали')
        while enemy > 0:
            enemy -= self.power
            days += 1
            print(f"{self.name} сражается {days}..., осталось {self.power} воинов.")

            time.sleep(1)
        else:
            print(f'{self.name} одержал победу спустя {days} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
