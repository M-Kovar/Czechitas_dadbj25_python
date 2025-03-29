# 4. Největší prvek v seznamu

numbers = [23, 4, -8, 16, 15, -42]

number_max = numbers[0]

for number in numbers:
    if number > number_max:
        number_max = number

print(number_max)


# 5. Rodná čísla

rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081"
]

pocet_muzu = 0
pocet_zen = 0
nejmladsi = int(rodna_cisla[0][:6])
nejstarsi = int(rodna_cisla[0][:6])

for cislo in rodna_cisla:

    rok = int(cislo[0] + cislo[1])
    mesic = int(cislo[2] + cislo[3])
    den = int(cislo[4] + cislo[5])

    datum_jako_cislo = int(cislo[:6])

    if mesic >= 50:
        pocet_zen += 1
        mesic -= 50
        datum_jako_cislo -= 5_000
    else:
        pocet_muzu += 1

    if datum_jako_cislo > nejmladsi:
        nejmladsi = datum_jako_cislo

    if datum_jako_cislo < nejstarsi:
        nejstarsi = datum_jako_cislo

print(f"Ordinaci navštívilo {pocet_zen} žen a {pocet_muzu} mužů.")
print(f"Nejstarší pacient: {nejstarsi}")
print(f"Nejmladší pacient: {nejmladsi}")


# 6. Nákupní košík

basket = [
    ["Chléb", 39, 1],
    ["Mléko", 32, 2],
    ["Avokádo", 35, 3],
    ["Máslo", 68, 1],
    ["Těstoviny", 40, 2]
]

total_price = 0

for item in basket:
    price = item[1]
    amount = item[2]
    total_price += price * amount

print(f"Celková cena je {total_price} Kč.")