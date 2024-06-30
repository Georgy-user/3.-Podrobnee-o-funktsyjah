# Переменная calls - общий счётчик вызовов других функций.
calls = 0
# calls = calls + 1
# print(calls)

# Функция count_calls при обращении к ней увеличивает значение переменной calls на 1.
def count_calls(calls):
    s = calls + 1
    return s

# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):
    global calls
    info_o_stroke = (len(string), string.upper(), string.lower())
    calls = count_calls(calls)
    return info_o_stroke

# Функция is_contains принимает два аргумента: строку и список,
# и возвращает True, если строка находится в этом списке,
# False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string, list_to_search):
    global calls
    calls = count_calls(calls)
    a = 0
    t = False
    while a < len(list_to_search):
        if string.casefold() == list_to_search[a].casefold():
            t = True
            break
        elif a == len(list_to_search):
            t = False
            break
        else:
            a = a + 1
            continue
    return t


print(string_info('Energy'))
print(string_info('Impulse'))
print(is_contains('Babochka', ['baBOchka', 'streCOZa', 'muravei']))
print(is_contains('Zurbagan', ['Djezkazgan', 'Drabagan', 'Urkagan', 'Balagan']))
print(calls)