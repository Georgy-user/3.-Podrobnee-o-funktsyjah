# Функция print_params(a = 1, b = 'строка', c = True) принимает три параметра со значениями по умолчанию.
def print_params(a = 1, b = 'String', c = True):
   print(a, ';', b, ';', c)

# Примеры вызова функции print_params с разным количеством аргументов, включая вызов без аргументов.
print()
print('Примеры вызова функции print_params:')
print_params(2, 'ert', True)
print_params()
print_params('ert', False)
print_params(True)
print_params(2, '', [1,2,3])
print_params(b=25)
print_params(c=[1,2,3])

values_list = [2.5,[3,4],False] # список с тремя элементами разных типов.
print()
print("Распаковка списка:")
print_params(*values_list) # Передача values_list в функцию print_params.

values_dict ={'a':33.4,'b':('qwe','rty'),'c':'boom'} # словарь с тремя ключами и значениями разных типов.
print()
print("Распаковка словаря:")
print_params(**values_dict) # Передача values_dict в функцию print_params.

values_list_2 = [{'K1':3,'K2':4},False] # список с двумя элементами разных типов.
print()
print("Распаковка списка + отдельные параметры:")
print_params(*values_list_2,True) # Передача values_list в функцию print_params.