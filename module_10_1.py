import time
from datetime import datetime
from threading import Thread

time_start = datetime.now()
def wite_words(word_count, file_name):
    number_word = 1
    with open(file_name, "a", encoding="utf-8") as file:
        for number_word in range(1, word_count+1):
            if number_word <= word_count:
                file.write(f"Какое-то слово № {number_word}")
                time.sleep(0.1)
                file.write("\n")
                number_word += 1
        else:
            print(f"Завершилась запись в файл {file_name}")
        file.close()



wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
time_stop = datetime.now()
time_res = time_stop - time_start
print(f"Работа функций {time_res}")

time_start = datetime.now()
thr_first = Thread(target=wite_words, args=(10, "example5.txt"))
thr_second = Thread(target=wite_words, args=(30, "example6.txt"))
thr_third = Thread(target=wite_words, args=(200, "example7.txt"))
thr_four = Thread(target=wite_words, args=(100, "example8.txt"))

thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()

time_stop = datetime.now()
time_res = time_stop - time_start
print(f"Работа функций {time_res}")