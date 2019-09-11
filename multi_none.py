#!/usr/bin/env python3

'''
Without process or pool classes.
'''


import time


def basic_function(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'


starttime = time.time()


for i in range(0, 10):
    y = i*i
    time.sleep(2)
    print('{} squared results in {} number.'.format(i, basic_function(y)))


print('That took {} seconds.'.format(time.time() - starttime))
