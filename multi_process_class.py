#!/usr/bin/env python3

'''
With process class.

The process class is most useful for a small number of processes where each
process would take a longer time to execute.

Place the functions and calculations that are done on each list item in its own
function that will take a list item as one of its arguments.

Create a new process for each list item.

Trigger each process in one call.

Keep track of these processes by making a list and adding each process to it.

After creating all of the processes, take the separate outpuot of each CPU and
join them into a single list.

The process class sends code to a processor as soon as the process is started.
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
