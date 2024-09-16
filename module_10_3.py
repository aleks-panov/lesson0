import time
from datetime import datetime
from random import randint
from threading import Thread, Lock

class Bank:
    def __init__(self, lock = Lock(), balance = 123):
        self.lock = lock
        self.balance = balance

    def deposit(self):
        num1 = 100
        for i in range(num1):
            ran1 = randint(50, 500)
            self.balance += ran1
            print(f"Пополнение: {ran1}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
               self.lock.release()
            time.sleep(0.001)


    def take(self):
        num2 = 100
        for i in range (num2):
            ran2 = randint(50, 500)
            print(f"Запрос на {ran2}.")
            if self.balance >= ran2:
                self.balance -= ran2
                print(f"Снятие: {ran2}. Баланс {self.balance}.")
            else:
                print("Запрос отклонен, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)


if __name__ == "__main__":

    bk = Bank()

    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')