# Řetězce jako sekvence

# Napr. cislo letu
# RETEZEC:  "BA 853"
# POZICE:    123456
# INDEX:     012345

flight_number = "BA 853"
# flight_number = input("Zadejte číslo letu: ")

prefix = flight_number[0] + flight_number[1]

if prefix == "BA":
    company = "British Airways"
elif prefix == "LH":
    company = "Lufthansa"
else:
    company = "Neznámá společnost"

print(f"Letíte se společností {company}")