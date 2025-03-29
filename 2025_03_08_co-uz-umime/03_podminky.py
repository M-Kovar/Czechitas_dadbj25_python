# Podmínky

number_of_tickets = 12
price_per_ticket = 190

total_price = number_of_tickets * price_per_ticket

if total_price >= 1500:
    total_price = total_price * (1 - 0.2)
    print("Získáváte slevu 20 %")
elif total_price >= 500:
    total_price = total_price * (1 - 0.1)
    print("Získáváte slevu 10 %")
else:
    print("Bohužel nezískáváte slevu.")

print(f"Celková cena nákupu je {total_price} Kč.")