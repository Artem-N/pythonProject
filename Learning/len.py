ten_things = "Apples Oranges Crows Telephone Light Sugar"

print('Погодите, тут меньше 10 обьектов. Давайте исправим это!')

stuf = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl',
              'Boy']

while len(stuf) != 10:
    next_one = more_stuff.pop()
    print(f'Добавляем {next_one}')
    stuf.append(next_one)
    print(f'Теперь у нас {len(stuf)} обьектов')

print(f'Итак: {stuf}')

print('Давайте кое-что сделаем с нашими обьектами.')

print(stuf[1])
print(stuf[-1])
print(stuf.pop())
print(stuf)
print(' '.join(stuf))
print('#'.join(stuf[3:5]))


