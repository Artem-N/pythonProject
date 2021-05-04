the_count = [1,2,3,4,5]
fruits = ['яблоко', 'апельсин', 'персик', 'абикос']
change = [1,'25', 2,'50', 3, '75']

for number in the_count:
    print(f'Счетчик {number}')

for fruit in fruits:
    print('Фрукт ' + fruit)

for i in change:
    print(f'Я получил {i}')

elements = []

for i in range (0,6):
    print(f'Добавление {i} в список.')

elements.append(i)

for i in elements:
    print(f'Номер елемента: {i}')