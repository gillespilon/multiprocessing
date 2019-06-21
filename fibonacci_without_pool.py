#!/usr/bin/env python3

'''
Multiprocessing without pool
That is, not multiprocessing
'''


import time


def fibonacci_sequence(number):
    first_number = 0
    second_number = 1
    number = int(number)
    if number == 0:
        print(f'Fibonacci of {number} is {number}')
    elif number == 1:
        print(f'Fibonacci of {number} is {number}')
    else:
        for item in range(2, number):
            new_number = first_number + second_number
            first_number = second_number
            second_number = new_number
        print(f'Fibonacci of {number} is {number}')


if __name__ == '__main__':
    input_number = input(f'Provide number to calculate: ')
    input_value = []
    input_value = input_number.split(f',')
    toc = time.time()
    for item in input_value:
        fibonacci_sequence(item)
    tic = time.time()
    time_taken = round((tic-toc)*1000, 1)
    print(f'It takes {time_taken} milli-seconds to calculate the',
          f'fibonacci of {input_number} concurrently')
