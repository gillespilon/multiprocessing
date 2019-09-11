#!/usr/bin/env python3

'''
With process class.
'''


import time
import multiprocessing


def basic_function(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'


def multiprocessing_function(x):
    y = x*x
    time.sleep(2)
    print('{} squared results in {} number.'.format(i, basic_function(y)))


if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(0, 10):
        p = multiprocessing.Process(target=multiprocessing_function, args=(i,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()


print('That took {} seconds.'.format(time.time() - starttime))
