# Zápis do souboru

# Mody otevreni souboru:
# File mode in Python: https://www.w3schools.com/python/python_file_handling.asp

text = "Tento text bude zapsán do souboru."
file_name = "soubor.txt"

# mode="w": write, zapis do noveho souboru (prepise existujici se stejnym nazvem)
with open(file_name, mode='w', encoding='utf-8') as output_file:
    print(text, file=output_file)

# mode="a": append, pridavani na konec existujiciho souboru
# with open(file_name, mode='a', encoding='utf-8') as output_file:
#     print(text, file=output_file)

# mode="x": exclusive creation, vytvori novy soubor pouze pokud jeste neexistuje (pokud existuje, vrati chybu)
# with open(file_name, mode='x', encoding='utf-8') as output_file:
#     print(text, file=output_file)

# mode="r": read, cteni ze souboru (vychozi mod) - zname s predchozi kapitoly
# with open(file_name, mode='r', encoding='utf-8') as file:
#     print(file.read())

# mode="rb": read binary, cteni ze souboru v binarni podobe (vychozi je ale textovy mod)
# with open('file_in_use.png', mode='rb') as file:
#     print(file.read())

# -----

names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('uzivatele.txt', mode='w', encoding='utf-8') as output_file:
    for name in names:
        print(name, file=output_file)