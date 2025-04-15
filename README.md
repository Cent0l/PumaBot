# 🐾 PumaBot – Twitch Chat Joke Bot

**PumaBot** to prosty, klimatyczny bot do czatu Twitcha, który po komendzie `!puma` rozpoczyna żart, czekając na interakcję użytkownika i rzuca puentę.

---

## 🚀 Jak działa?

1. Użytkownik na czacie wpisuje:
!puma
2. Bot losuje jeden z żartów z pliku `jokes.json` i odpisuje np.:
Ja w sprawie pumy
3. Bot **czeka 20 sekund** na odpowiedź od tej samej osoby (np. „jakiej pumy”).

4. Jeśli odpowiedź pasuje – bot rzuca puentę:
Takiej co ma jaja z gumy

5. Po odpowiedzi lub przekroczeniu czasu – bot kończy „rozmowę” i czeka na kolejne `!puma`.

🔒 **Tylko jeden użytkownik na raz** może prowadzić „rozmowę z botem”. Pozostali muszą poczekać, aż aktualna interakcja się zakończy.

---

## 📁 Format żartów (`jokes.json`)

Bot korzysta z pliku `jokes.json`, który zawiera tablicę żartów w takim formacie:

```json
{
"setup": "Ja w sprawie pumy",
"expected": "jakiej pumy",
"punchline": "Takiej co ma jaja z gumy"
}
