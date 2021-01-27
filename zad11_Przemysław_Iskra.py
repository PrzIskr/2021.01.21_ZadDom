import csv
from openpyxl import Workbook

plik_csv = open('plik00.csv')
fileReader = csv.reader(plik_csv)
wb = Workbook()
sheet = wb.active

for row in fileReader:
    print(row)
    sheet.append(row)
wb.save("arkusz.xlsx")