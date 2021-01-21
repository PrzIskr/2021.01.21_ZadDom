txt_file_A = None
txt_file_B = None
try:
    with open("plik02_A.txt", 'r') as txt_file_A:
        with open("plik02_B.txt", 'w') as txt_file_B:
            for linia in txt_file_A:
                print(linia)
                txt_file_B.write(linia)
    txt_file_A.close()
    txt_file_B.close()
except IOError as ioe:
    print("Błąd: {}".format(ioe))
    if txt_file_A:
        txt_file_A.close()
    if txt_file_B:
        txt_file_B.close()