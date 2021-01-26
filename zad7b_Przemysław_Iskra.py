# def person_print(name, last_name, *others, age): #przed edycją
def person_print(name, last_name, age, *others):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}' \
                     .format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

person_print('Przemysław', 'Iskra', 21, "kraj: Polska", "miasto: Kraków")

# Odp: Nie można wywołać tej funkcji bez wprowadzenia zmian
# Aby było to możliwe argument args/kwargs musi się znajdować na końcu deklaracji funkcji