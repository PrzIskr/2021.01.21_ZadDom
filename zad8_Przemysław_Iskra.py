txt_file = open('plik01.txt', 'w+')
txt_file.write('w pierwszej ćwiartce wszystkie są dodatnie,'
               '\nw drugiej tylko sinus,'
               '\nw trzeciej tangens i cotangens,'
               '\na w czwartej cosinus')
txt_file = open('plik01.txt', 'r')
print(txt_file.read())
txt_file.close()