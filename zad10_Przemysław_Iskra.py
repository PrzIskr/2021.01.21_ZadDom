import re

bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''

#pattern = re.compile(r'[^ ]{4,}')                      # wszystkie znaki (nie tylko litery)
pattern = re.compile(r'[a-zA-ZąćęłńóśźżĄĘŁŃÓŚŹŻ]{4,}')  # tylko litery
result = set(pattern.findall(bridge_of_death))

for slowo4 in result:
    print(slowo4)