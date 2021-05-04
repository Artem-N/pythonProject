def is_prime(num):
    '''
    Наивный метод проверки простых чисел.
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'не является простым')
            break
    else: # Если остаток никогда не был равен нулю, то число простое
        print(num,'является простым!')

is_prime()