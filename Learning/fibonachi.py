def find_fibonachi(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

# for x in find_Fibonacci(100):
#for x in find_fibonachi(10):
    #print(x)


#print(list(find_fibonachi(10)))
