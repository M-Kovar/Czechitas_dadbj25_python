# Úvod, proměnné a hodnoty

play = "Každý má svou pravdu"
number_of_tickets = 3
price_per_ticket = 190

total_price = price_per_ticket * number_of_tickets

# Jednoduchy vypis
# print(total_price)

# Vypis pomoci formatovaneho retezce (f-string):
print(f"Cena {number_of_tickets} lístků na hru {play} je celkem {total_price} Kč.")

# Alternativa: Vypis spojenim retezcu funkci print() - moc namahave, malo prizpusobitelne
# print("Cena", number_of_tickets, "lístků na hru", play, "je celkem", total_price, "Kč.")

# Alternativa: Vypis rucnim spojenim retezcu - jeste vic namahave
# print("Cena " + number_of_tickets + " lístků na hru " + play + " je celkem " + total_price + " Kč.")



# Mimochodem: vyzkousime operatory // a % (budou se hodit pozdeji)

# Celociselne deleni //
print(190 // 3)

# Zbytek po celociselnem deleni % (modulo)
print(190 % 3)