# Čtení ze souborů

# Zakladni zpusob prace se souborem (vyzkousime pro nazornost):
file = open('mereni.txt')
# print(file)

# read(): Nacte obsah souboru jako jeden retezec
text = file.read()

# Zavreni souboru
file.close()


# Vyuziti bloku "with" (kontextovy manazer) je doporuceny zpusob prace se souborem:
# (soubor je po provedeni kodu v bloku with automaticky zavren, neni tedy potreba volat close())
with open('mereni.txt', mode="r", encoding='utf-8') as file:
    text = file.read()
    
print(text)


# Prochazeni souboru for cyklem radek po radku (oproti readlines() vetsi flexibilita):
file_name = 'mereni.txt'
lines = []

with open(file_name, mode="r", encoding='utf-8') as file:
    for line in file:
        # lines.append(line)
        lines.append(line.strip())
    # Alternativa k for cyklu: readlines(), nacte obsah souboru jako seznam radku
    # lines = file.readlines()

print(lines)


# Priklad zpracovani vstupu:
file_name = 'mereni.txt'
output = []

with open(file_name, mode="r", encoding='utf-8') as file:
    for line in file:
        line_day_temp = line.split('\t')
        day = line_day_temp[0]
        temp = float(line_day_temp[1]) 
        # day, temp = line.split('\t')
        output.append([day, temp])

print(output)