def person_print(name_1, last_name, age, **key_others):
    formatted_data = 'Imię: {},'\
    ' nazwisko: {}, wiek: {}'.\
    format(name_1, last_name, age)

    print(type(key_others)) # <class 'dict'>
    print(key_others) # {'name_2': 'Józef','name_3': 'Karol'}
    others_str = ' '
    for value in key_others.values():
        others_str += value + ' '
    print(formatted_data + others_str)

person_print('Jan', 'Kowal', 33, name_2='Józef', name_3='Karol')