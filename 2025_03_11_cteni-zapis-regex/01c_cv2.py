# Cvičení 2: Počet slov

file_name = "praha.txt"
lines = []
with open(file_name, mode="r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())


words_count = 0
for line in lines:
    words = line.split()
    # print(words)
    words_count += len(words)
# ...Alternativa: pocitani slov lze i zahrnout rovnou do cyklu ve with bloku nahore

print(f"Celkový počet slov v souboru je {words_count}")