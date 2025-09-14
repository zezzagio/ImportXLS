#! /usr/bin/env python3
import openpyxl

def change_first_row(file_path, nuova_prima_riga):
    # Apri il file Excel esistente
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for colonna, valore in enumerate(nuova_prima_riga, start=1):
        sheet.cell(row=1, column=colonna).value=valore
    workbook.save(file_path)

def main():
    # Esempio di utilizzo
    file_path = 'Generi.xlsx'
    new_first_row = ('id', 'famiglia', 'genere', 'categoria')
    change_first_row(file_path, new_first_row)

if __name__ == "__main__":
    main()
