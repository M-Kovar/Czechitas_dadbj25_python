# Cvičení 1: Výplata přesněji

vykaz = []
with open("vykaz.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        vykaz.append(int(line))

print(vykaz)


hodinova_mzda = int(input("Zadejte hodinovou mzdu: "))
rocni_mzda = sum(vykaz) * hodinova_mzda
prumerna_mzda_mesicni = rocni_mzda / len(vykaz)

print(f"Celková mzda za rok je {rocni_mzda} Kč.")
print(f"Průměrná měsíční mzda je {round(prumerna_mzda_mesicni)} Kč.")