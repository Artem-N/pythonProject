def simple_gen():
    for x in range(3):
        yield x
"""
for num in simple_gen():
    print(num)
"""
'''
g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
'''

s = 'hello'
#перетворюємо об'єкт в такий по якому можна пройтись не тільки циклом
s_iter = iter(s)
print(next(s_iter))



