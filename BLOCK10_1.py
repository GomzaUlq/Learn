import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w+') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start_time = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = time.time()
final_time = end_time - start_time
print(final_time)  # 34.24547219276428

thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_two = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_four = Thread(target=write_words, args=(100, 'example8.txt'))

start_time = time.time()

thr_first.start()
thr_two.start()
thr_third.start()
thr_four.start()

thr_first.join()
thr_two.join()
thr_third.join()
thr_four.join()

end_time = time.time()
final_time = end_time - start_time
print(f'Работа c потоками {final_time}')
# Работа с потоками 20.140324115753174
