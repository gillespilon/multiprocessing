#!/usr/bin/env python3

'''
With pool class.
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
    print('{} squared results in {} number.'.format(x, basic_function(y)))


if __name__ == '__main__':
    starttime = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_function, range(0, 10))
    pool.close()
    print('That took {} seconds.'.format(time.time() - starttime))
