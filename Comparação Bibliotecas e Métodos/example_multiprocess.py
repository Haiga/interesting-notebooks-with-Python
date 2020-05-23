import time
import multiprocessing

import numpy as np


def multiprocessing_func(arr, i):
    arr[i] = i
    print('Array at end of process ' + str(i) + ':' + str(np.array(arr)))


if __name__ == '__main__':
    starttime = time.time()
    processes = []
    x = np.zeros(10) - 1
    print(x)
    for i in range(0, 10):
        p = multiprocessing.Process(target=multiprocessing_func, args=(x, i,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    print(x)
    print('Time: {} seconds'.format(time.time() - starttime))
    # Too bad
    # Processos tem suas próprias memórias
    # Não utilizar if __name__ == '__main__': acarretará em erros
    # As funções devem estar definidas fora do main

    starttime = time.time()
    processes = []
    # x = np.zeros(10) - 1
    x = multiprocessing.Array('f', 10)
    print(np.array(x))
    for i in range(0, 10):
        p = multiprocessing.Process(target=multiprocessing_func, args=(x, i,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    print(np.array(x))
    print('Time: took {} seconds'.format(time.time() - starttime))
