def ask():
    while True:
        try:
            result = int(input('enter numder: '))
        except:
            print('its not number')
            continue
        else:
            print('good job')
            break
        finally:
            print('finish')
            print('it is end')
ask()