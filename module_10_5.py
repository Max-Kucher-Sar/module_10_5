import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            string = file.readline().strip()
            if not string:
                break
            all_data.append(string)


filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']


if __name__ == '__main__':
    start = datetime.now()
    for file in filenames:
        read_info(file)
    end = datetime.now()
    print('Линейный вызов:', end - start)

    start2 = datetime.now()
    with multiprocessing.Pool() as pool:
        result = pool.map(read_info, filenames)
    end2 = datetime.now()
    print('Многопроцессный вызов:', end2 - start2)



