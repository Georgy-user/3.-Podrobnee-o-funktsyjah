# Функция send_email принимает 2 обычных аргумента:
# message(сообщение), recipient(получатель)
# и 1 обязательно именованный аргумент (отправитель)
# со значением по умолчанию sender = "university.help@gmail.com".
def send_email(message, recipient, *, sender = "university.help@gmail.com"):

    mail1 = False # mail1 определяет, правильно или нет введён e-mail получателя
    mail2 = False # mail2 определяет, правильно или нет введён e-mail отправителя

    for i in recipient:
        # ищет символ @ в e-mail получателя,
        # оставляет у переменной mail1 значение False, если не находит
        if i != '@':
            continue
        else:
            mail1 = True
            break


    if mail1 == True:
        for i in sender:
            # ищет символ @ в e-mail отправителя,
            # оставляет у переменной mail2 значение False, если не находит
            if i != '@':
                # print(i)
                continue
            else:
                mail2 = True
                # print(mail2)
                break

    # Проверка окончаний строк sender и recipient на наличие окончаний ".com", ".ru", ".net".
    # Если окончание другое, то переменной mail1 и|или mail2 присваивается значение False.
    if recipient[-3:] == '.ru' or recipient[-4:] == '.com' or recipient[-4:] == '.net':
        mail1 = True
    else:
        mail1 = False
    if sender[-3:] == '.ru' or sender[-4:] == '.com' or sender[-4:] == '.net':
        mail2 = True
    else:
        mail2 = False


    # Если отправитель по умолчанию - university.help@gmail.com, то выводится сообщение:
    # "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    if mail1 == True and mail2 == True and sender == "university.help@gmail.com" and recipient != sender:
        print("Письмо успешно отправлено  с адреса ", sender, "на адрес ", recipient, '.')

    # Если адрес отправителя не по умолчанию, то выводится сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!
    # Письмо отправлено с адреса <sender> на адрес <recipient>."
    elif mail1 == True and mail2 == True and sender != "university.help@gmail.com" and recipient != sender:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено  с адреса ", sender, "на адрес ", recipient, '.')

    # Если sender и recipient совпадают, то выводится "Нельзя отправить письмо самому себе!"
    elif mail1 == True and mail2 == True and recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    # Если строки recipient и sender не содержат "@" или не оканчиваются
    # на ".com"/".ru"/".net", то на экран выводится строка:
    # "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    # elif mail1 == False or mail2 == False:
    else:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient, '.' )



send_email("Это сообщение для проверки связи", 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.uk', sender='urban.teacher@mail.ru')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')