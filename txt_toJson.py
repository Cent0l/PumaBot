import json
import re

# Ścieżka do pliku wejściowego (z Twoimi żartami)
input_file = 'yomama.txt'

# Ścieżka do pliku wyjściowego
output_file = 'yomama.json'

# Wczytanie żartów z pliku tekstowego
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

jokes = []
for line in lines:
    clean_line = line.strip()
    if clean_line:
        # Usuwamy numer z początku linii (np. "2. ", "123. ", itd.)
        clean_line = re.sub(r'^\d+\.\s*', '', clean_line)
        jokes.append(clean_line)

# Zapisanie do pliku JSON
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(jokes, f, ensure_ascii=False, indent=2)

print(f'Plik {output_file} został wygenerowany poprawnie.')
