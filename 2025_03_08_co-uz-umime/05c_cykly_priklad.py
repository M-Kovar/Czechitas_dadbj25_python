# Cykly: Příklad

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 2],
    ["Chemie", 4],
]

# Zalozeni promenne pro soucet znamek
sum_of_marks = 0

for subject in school_report:
    # Postupne pricitani znamek k prubeznemu souctu
    # sum_of_marks = sum_of_marks + subject[1]
    sum_of_marks += subject[1]

# Vypocet prumeru jako celkovy soucet znamek vydeleny jejich poctem
average = sum_of_marks / len(school_report)

print(f"Průměrná známka studenta/studentky je {average}.")


# Vypis problematickych predmetu
print("Pro studenta/studentku jsou problematické tyto předměty:")

for mark in school_report:
    if mark[1] > 3:
        print(mark[0])