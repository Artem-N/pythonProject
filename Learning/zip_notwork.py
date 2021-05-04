import os
import time
sourse = ['/Applications']

target_dir = '/Users/artemnovickij/Desktop/python'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_comand = "zip -qr {0}".format(target, ' '.join(sourse))

if os.system(zip_comand) == 0:
    print("Резервная копия успешно создана в ", target)
else:
    print("Создание резервной копии не удалось")

