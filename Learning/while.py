x = 0

while x < 10:
    print('x равен: ',x)
    print(' x всё еще меньше 10, добавляем 1 к x')
    x+=1
    if x==3:
        print('Выходим из цикла (break), потому что x==3')
        break
    else:
        print('продолжаем...')
        continue
else:
    print("Завершено!")