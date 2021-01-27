import csv
from openpyxl import Workbook
file = open('plik00.csv')
fileReader = csv.reader(file)
book = Workbook()
sheet = book.active
for row in fileReader:
    print(row)
    sheet.append(row)
book.save("arkusz.xlsx")