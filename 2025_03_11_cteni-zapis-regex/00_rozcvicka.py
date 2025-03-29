# Rozcvička

# Z následujícího seznamu vypište pod sebe do terminálu pouze názvy předmětů.
# Bonus: Vypište pouze názvy s délkou větší než 10 znaků.

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


for item in school_report:
    name = item[0]
    print(name)

    # Bonus
    # if len(name) > 10:
    #     print(name)