import re


def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print('Выполняем поиск фразы, используя следующую проверку re: %r' % pattern)
        print(re.findall(pattern, phrase))
        print('\n')


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',  # s, затем ноль или несколько d
                 'sd+',  # s, затем одна или несколько d
                 'sd?',  # s, затем ноль или одна d
                 'sd{3}',  # s, затем три d
                 'sd{2,3}',  # s, затем от двух до трех d
                 ]

multi_re_find(test_patterns, test_phrase)


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',    # или s, или d
                's[sd]+']   # s, затем одна или больше буква либо s, либо d

multi_re_find(test_patterns,test_phrase)

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns = ['[a-z]+',  # последовательности букв в нижнем регистре
                 '[A-Z]+',  # последовательности букв в верхнем регистре
                 '[a-zA-Z]+',  # последовательности букв в нижнем или верхнем регистре
                 '[A-Z][a-z]+']  # одна буквы в верхнем регистре, затем буквы в нижнем регистре

multi_re_find(test_patterns, test_phrase)
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # последовательность цифр
                r'\D+', # последовательность не-цифр
                r'\s+', # последовательность пробельных символов
                r'\S+', # последовательность не-пробельных символов
                r'\w+', # альфа-цифровые символы
                r'\W+', # не-альфа-цифровые символы
                ]

multi_re_find(test_patterns,test_phrase)