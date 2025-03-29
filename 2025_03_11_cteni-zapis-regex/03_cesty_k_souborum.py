# Cesty k souborum

# Relativni cesta
# (vztahuje se k aktualne otevrene slozce)
# file_path = "praha.txt"         # Soubor je primo v otevrene slozce
# file_path = "data\praha.txt"    # Soubor je v podslozce "data" v otevrene slozce
# file_path = "..\praha.txt"      # Soubor je ve slozce nadrazene otevrene slozce

# Absolutni cesta
# (nezavisla na aktualne otevrene slozce)
file_path = "C:/Users/mapup/OneDrive/Dokumenty/Czechitas/_Kurzy/2025-03_06 DA Data/2025_03_11_prep/data/praha.txt"
# file_path = r"C:\Users\mapup\OneDrive\Dokumenty\Czechitas\_Kurzy\2025-03_06 DA Data\2025_03_11_prep\data\praha.txt"
# file_path = "C:\\Users\\mapup\\OneDrive\\Dokumenty\\Czechitas\\_Kurzy\\2025-03_06 DA Data\\2025_03_11_prep\\data\\praha.txt"


with open(file_path, mode='r', encoding='utf-8') as file:
    print(file.read())