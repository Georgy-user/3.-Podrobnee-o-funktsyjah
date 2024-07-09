# Функция get_multiplied_digits принимает аргумент целое число number
# и подсчитывает произведение цифр этого числа.
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        iteraction = first * get_multiplied_digits(int(str_number[1:]))
        return iteraction
    else:
        return first

result1 = get_multiplied_digits(60203)
print(result1)
result2 = get_multiplied_digits(7)
print(result2)
