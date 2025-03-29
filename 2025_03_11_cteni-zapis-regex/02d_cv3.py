# Cvičení 3: Rozepsaná výplata

vykaz = []
with open("vykaz.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        vykaz.append(int(line))

hodinova_mzda = int(input("Zadejte hodinovou mzdu: "))

with open('mzdy_za_mesic.txt', mode="w", encoding="utf-8") as file_output:
    for hodin_za_mesic in vykaz:
        mzda_za_mesic = int(hodin_za_mesic) * hodinova_mzda
        print(mzda_za_mesic, file=file_output)



# Bonus/alternativa: muzeme si otevrit a zpracovat oba soubory zaroven
# with open('vykaz.txt', mode="r", encoding="utf-8") as file_input:
#     with open('mzdy_za_mesic.txt', mode="w", encoding="utf-8") as file_output:
#         for hodin_za_mesic in file_input:
#             mzda_za_mesic = int(hodin_za_mesic) * hodinova_mzda
#             print(mzda_za_mesic, file=file_output)