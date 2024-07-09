# Функция single_root_words принимает одно обязательное слово в параметр
# root_word, а далее неограниченную последовательность в параметр *other_words.
def single_root_words(root_word, *other_words):
    # Пустой список same_words, который пополнится нужными словами.
    same_words = []
    for i in range(len(other_words)):
        if len(root_word) <= len(other_words[i]):
            comparison = other_words[i].lower().find(root_word.lower())
            if comparison != -1:
                same_words.append(other_words[i])

        else:
            comparison = root_word.lower().find(other_words[i].lower())
            if comparison != -1:
                same_words.append(other_words[i])

    return same_words


nuclear_words3 = single_root_words('Тон', 'Шапито', 'питОн', 'тРойниК', 'тоНик', 'РоТоНда', 'Нота')
print(nuclear_words3)

nuclear_words3 = single_root_words('парабеллум', 'Пара', 'раб', 'араб', 'НиБеллунг', 'клумба')
print(nuclear_words3)

nuclear_words3 = single_root_words('шарик', 'шар', 'шариковый', 'шарнир', 'смешарик', 'квадрат')
print(nuclear_words3)