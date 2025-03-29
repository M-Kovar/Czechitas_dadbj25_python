# Cvičení 3: Půjčovna

kilometres_total = 0
with open('auta.txt', encoding='utf-8') as file:
    for line in file:
        kilometres = float(line.replace(',', '.').split(' ')[-1])
        kilometres_total += kilometres

print(f'celkovy pocet ujetych kilometru je {kilometres_total}')