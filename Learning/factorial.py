number = 2000

def factorial (n):
    if n == 0:
        return 1

    f = 1
    i = 0

    while i < n:
        i+=1
        f=f*i

    return f

print(f'Факториала числа {number} равен {factorial(number)}')
