import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        data = file.readline()
        while data:
            data = file.readline()
            all_data.append(data)


start = time.time()
filenames = [f'./file {number}.txt' for number in range(1, 5)]
read_info('file 4.txt')
for file in filenames:
    read_info(file)
end = time.time()
final_time = end - start
print(final_time)
# линейно 6.35900616645813
# if __name__ == '__main__':
#    start = time.time()
#    with multiprocessing.Pool(processes=4) as pool:
#        name = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
#        pool.map(read_info, filenames)
#    end = time.time()
#    print(end - start)
# многопроцессорность  3.554210662841797
