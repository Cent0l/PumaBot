
# 🐾 PumaBot – Twitch Chat Joke Bot

**PumaBot** to prosty, klimatyczny bot do czatu Twitcha, który rozkręca zabawę żartami na kilka sposobów.

---

## 🚀 Jak działa?

### Komenda `!puma`
1. Użytkownik wpisuje na czacie:
   ```
   !puma
   ```
2. Bot losuje jeden z żartów z pliku `jokes.json` i odpisuje np.:
   ```
   Ja w sprawie pumy
   ```
3. Bot **czeka 20 sekund** na odpowiedź od tej samej osoby (np. „jakiej pumy”).

4. Jeśli odpowiedź pasuje – bot rzuca puentę:
   ```
   Takiej co ma jaja z gumy
   ```

5. Po odpowiedzi lub przekroczeniu czasu – bot kończy „rozmowę” i czeka na kolejne `!puma`.

🔒 **Tylko jeden użytkownik na raz** może prowadzić „rozmowę z botem**. Inni muszą poczekać aż aktualna interakcja się zakończy.

---

### Komenda `!zart`
- Bot losuje **krótki żart (oneliner)** z pliku `oneliners.json`.
- Żarty są typu „Co mówi elektryk do elektryka? Będziemy w kontakcie.”
- Komenda `!zart` może być użyta **maksymalnie raz na 30 sekund** (globalnie dla wszystkich użytkowników).

---

### Komenda `!yomama`
- Bot losuje żart typu **"Twoja stara..."** z pliku `yomama.json`.
- Przykład:
  ```
  Twoja stara nie ma dzieci.
  ```
- Komenda `!yomama` może być użyta **maksymalnie raz na 30 sekund** (globalnie dla wszystkich użytkowników).

---

## 📁 Format plików z żartami

### `jokes.json`
Tablica obiektów:
```json
{
  "setup": "Ja w sprawie pumy",
  "expected": "jakiej pumy",
  "punchline": "Takiej co ma jaja z gumy"
}
```

### `oneliners.json`
Tablica krótkich tekstów:
```json
[
  "Ile zarabia mechanik? 4 koła",
  "Co robi elektryk na scenie? Buduje napięcie",
  "Dlaczego ściany nie toczą wojen? Bo między nimi jest pokój"
]
```

### `yomama.json`
Tablica żartów "twoja stara":
```json
[
  "Twoja stara kupuje w Lidlu.",
  "Twoja stara prasuje trawnik czajnikiem.",
  "Twoja stara kopie rowy uszami."
]
```

---

## ⚙️ Konfiguracja bota

W pliku `main.py` ustaw:

- `nickname` – nazwa konta bota na Twitchu
- `token` – Twój token OAuth
- `channel` – kanał Twitcha, na którym bot ma działać (np. `#twojkanal`)

Bot łączy się przez protokół IRC z serwerami Twitcha.

---


## 💬 Przykład na czacie

```
🧑: !puma
🤖: Ja w sprawie borsuka
🧑: jakiego borsuka
🤖: Co jajami stuka

🧑: !zart
🤖: Dlaczego imprezy w kosmosie są nieudane? Bo nie ma atmosfery.

🧑: !yomama
🤖: Twoja stara pierze w rzece.
```

