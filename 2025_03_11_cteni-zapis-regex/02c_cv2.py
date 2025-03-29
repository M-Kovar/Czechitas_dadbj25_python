# Cvičení 2: Vytvoření souboru

file_name = input('Zadej název souboru: ')
text = input('Zadej text, který chceš uložit: ')

# Bonus: pridani spravne pripony, pokud ji nazev souboru neobsahuje
extension = ".txt"
if not file_name.endswith(extension):
    file_name += extension

with open(file_name, mode='w', encoding='utf-8') as file:
    print(text, file=file)
    # Alternativa: metoda write()
    # file.write(text)