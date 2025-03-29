# Cvičení 1: Dny v měsíci

day_counts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('kalendar.txt', 'w', encoding='utf-8') as output_file:
    for count in day_counts:
        print(count, file=output_file)