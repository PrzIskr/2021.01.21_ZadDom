def pizza_args(nazwa, ciasto, srednica, *others):
    formatted_data = 'Nazwa pizzy: {},\nGrubość ciasta: {},\nŚrednica pizzy: {} cm'\
                        .format(nazwa, ciasto, srednica)

    others_str = ',\n'
    for arg in others:
        others_str += arg + ',\n'
    print(formatted_data + others_str)


def pizza_kwargs(nazwa, ciasto, srednica, **key_others):
    formatted_data = 'Nazwa pizzy: {},\nGrubość ciasta: {},\nŚrednica pizzy: {} cm'\
                        .format(nazwa, ciasto, srednica)

    print(type(key_others))
    print(key_others)
    others_str = ',\n'
    for value in key_others.values():
        others_str += value + ',\n'
    print(formatted_data + others_str)

print('*args\n')

pizza_args('Margherita','cienkie', 32, 'Składniki: sos pomidorowy, mozarella, oregano', 'Sos do zestawu: -')

print('**kwargs\n')

pizza_kwargs('Hawajska','cienkie', 42, składniki='sos pomidorowy, mozarella, szynka, ananas, oregano', sos_do_zestawu='czosnkowy')