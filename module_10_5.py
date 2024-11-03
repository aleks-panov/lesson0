import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, "r") as file1:
        while True:
            line = file1.readline().strip()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]
# Линейный вызов
start1 = datetime.now()
for f in filenames:
    read_info(f)
end1 = datetime.now()
time1 = end1 - start1
print(f"время линейного вызова, {time1}")
# Многопроцессный
if __name__ == '__main__':
    start2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end2 = datetime.now()
    time2 = end2 - start2
    print(f'время многопроцессорного вызова, {time2}')
