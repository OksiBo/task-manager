# Test cases – Task manager

## hlavni_menu()

### TC01: Volba 1 – přidání úkolu
- **Popis:** Ověření, že volba 1 spustí přidání úkolu.
- **Vstupní podmínky:** Program běží, je zobrazené hlavní menu.
- **Kroky testu:**
  1. Spustit program.
  2. Zadat `1` a potvrdit Enterem.
- **Očekávaný výsledek:** Program se zeptá na název úkolu.
- **Skutečný výsledek:** Zobrazilo se „Zadejte název úkolu:“.
- **Stav:** Pass
- **Poznámky:** Základní navigace v menu.

### TC02: Volba 2 – zobrazení úkolů
- **Popis:** Ověření, že volba 2 zobrazí seznam úkolů.
- **Vstupní podmínky:** V seznamu je 1 úkol.
- **Kroky testu:**
  1. Zadat `2`.
- **Očekávaný výsledek:** Zobrazí se seznam úkolů a pak znovu menu.
- **Skutečný výsledek:** Zobrazilo se „Seznam úkolů:“ a úkol, potom menu.
- **Stav:** Pass
- **Poznámky:**

### TC03: Volba 4 – konec programu
- **Popis:** Ověření, že volba 4 ukončí program.
- **Vstupní podmínky:** Je zobrazené hlavní menu.
- **Kroky testu:**
  1. Zadat `4`.
- **Očekávaný výsledek:** Vypíše se „Konec programu.“ a program skončí.
- **Skutečný výsledek:** Vypsalo se „Konec programu.“, program skončil.
- **Stav:** Pass
- **Poznámky:**

### TC04: Neplatná volba
- **Popis:** Ověření, co program udělá, když zadám jinou volbu než 1–4.
- **Vstupní podmínky:** Je zobrazené hlavní menu.
- **Kroky testu:**
  1. Zadat `7`.
  2. Zadat `abc`.
  3. Jen stisknout Enter.
- **Očekávaný výsledek:** Pokaždé se vypíše upozornění a menu se zobrazí znovu.
- **Skutečný výsledek:** Vypsalo se „Neplatná volba.“ a znovu menu, program nespadl.
- **Stav:** Pass
- **Poznámky:** Negativní test.

### TC05: Volba s mezerami
- **Popis:** Ověření, že volba ` 2 ` (s mezerou před a za) funguje jako `2`.
- **Vstupní podmínky:** Je zobrazené hlavní menu.
- **Kroky testu:**
  1. Zadat ` 2 `.
- **Očekávaný výsledek:** Zobrazí se seznam úkolů.
- **Skutečný výsledek:** Seznam se zobrazil.
- **Stav:** Pass
- **Poznámky:** Hraniční případ, funguje díky `strip()`.

## pridat_ukol()

### TC06: Přidání prvního úkolu
- **Popis:** Ověření, že se úkol uloží, když vyplním název i popis.
- **Vstupní podmínky:** Seznam úkolů je prázdný.
- **Kroky testu:**
  1. Zadat `1`.
  2. Název: `Úkol 1`, popis: `Popis pro úkol 1`.
  3. Zadat `2`.
- **Očekávaný výsledek:** Vypíše se, že úkol byl přidán, a v seznamu je `1. Úkol 1 - Popis pro úkol 1`.
- **Skutečný výsledek:** Vypsalo se „Úkol 'Úkol 1' byl přidán.“, úkol je v seznamu.
- **Stav:** Pass
- **Poznámky:** Pozitivní test a zároveň hraniční (první úkol).

### TC07: Prázdný název
- **Popis:** Ověření, že nejde uložit úkol bez názvu.
- **Vstupní podmínky:** Je zobrazené hlavní menu.
- **Kroky testu:**
  1. Zadat `1`.
  2. Název nechat prázdný, popis: `Test`.
- **Očekávaný výsledek:** Upozornění a program chce znovu název i popis.
- **Skutečný výsledek:** Vypsalo se „Název ani popis úkolu nesmí být prázdný.“ a program se znovu ptal na název i popis.
- **Stav:** Pass
- **Poznámky:** Požadavek ze zadání.

### TC08: Prázdný popis
- **Popis:** Ověření, že nejde uložit úkol bez popisu.
- **Vstupní podmínky:** Je zobrazené hlavní menu.
- **Kroky testu:**
  1. Zadat `1`.
  2. Název: `Test`, popis nechat prázdný.
- **Očekávaný výsledek:** Upozornění a program chce znovu název i popis.
- **Skutečný výsledek:** Upozornění se vypsalo, program se znovu ptal na oba údaje.
- **Stav:** Pass
- **Poznámky:**

### TC09: Název jen z mezer
- **Popis:** Ověření, že název ze samých mezer se bere jako prázdný.
- **Vstupní podmínky:** Je zobrazené hlavní menu.
- **Kroky testu:**
  1. Zadat `1`.
  2. Název: `   ` (3 mezery), popis: `Popis`.
- **Očekávaný výsledek:** Upozornění, úkol se neuloží.
- **Skutečný výsledek:** Vypsalo se upozornění, úkol se neuložil.
- **Stav:** Pass
- **Poznámky:** Bez `strip()` by takový úkol prošel.

## zobrazit_ukoly()

### TC10: Zobrazení více úkolů
- **Popis:** Ověření, že se zobrazí všechny úkoly ve správném pořadí.
- **Vstupní podmínky:** V seznamu jsou 2 úkoly.
- **Kroky testu:**
  1. Zadat `2`.
- **Očekávaný výsledek:** Úkoly jsou očíslované od 1 v pořadí, jak byly přidány.
- **Skutečný výsledek:** Zobrazilo se `1. Nakup - mleko` a `2. Uklid - kuchyn`.
- **Stav:** Pass
- **Poznámky:**

### TC11: Prázdný seznam
- **Popis:** Ověření, co se zobrazí, když nejsou žádné úkoly.
- **Vstupní podmínky:** Seznam je prázdný.
- **Kroky testu:**
  1. Zadat `2`.
- **Očekávaný výsledek:** Hláška, že seznam je prázdný.
- **Skutečný výsledek:** Vypsalo se „Seznam úkolů je prázdný.“
- **Stav:** Pass
- **Poznámky:** Hraniční případ.

## odstranit_ukol()

### TC12: Odstranění úkolu
- **Popis:** Ověření, že se vybraný úkol smaže.
- **Vstupní podmínky:** V seznamu jsou 2 úkoly.
- **Kroky testu:**
  1. Zadat `3`.
  2. Zkontrolovat, že se zobrazil seznam úkolů.
  3. Zadat `1`.
  4. Zadat `2`.
- **Očekávaný výsledek:** Úkol č. 1 se smaže, zbývající úkol má teď číslo 1.
- **Skutečný výsledek:** Vypsalo se „Úkol 'Nakup' byl odstraněn.“, v seznamu zůstal `1. Uklid - kuchyn`.
- **Stav:** Pass
- **Poznámky:**

### TC13: Číslo, které neexistuje
- **Popis:** Ověření upozornění při zadání čísla mimo seznam.
- **Vstupní podmínky:** V seznamu jsou 2 úkoly.
- **Kroky testu:**
  1. Zadat `3`, pak `5`.
  2. Zadat `3`, pak `0`.
- **Očekávaný výsledek:** Upozornění, nic se nesmaže, program se vrátí do menu.
- **Skutečný výsledek:** V obou případech „Takový úkol neexistuje.“ a návrat do menu.
- **Stav:** Pass
- **Poznámky:** Číslo 0 je důležité – bez kontroly by se smazal poslední úkol.

### TC14: Text nebo záporné číslo místo čísla
- **Popis:** Ověření, že program nespadne, když nezadám číslo.
- **Vstupní podmínky:** V seznamu je aspoň 1 úkol.
- **Kroky testu:**
  1. Zadat `3`, pak `abc`.
  2. Zadat `3`, pak `-1`.
- **Očekávaný výsledek:** Upozornění, nic se nesmaže, návrat do menu.
- **Skutečný výsledek:** Vypsalo se „Neplatný vstup, zadejte číslo úkolu.“ a návrat do menu.
- **Stav:** Pass
- **Poznámky:** Negativní test.

### TC15: Odstranění posledního úkolu
- **Popis:** Ověření, že jde smazat i jediný zbývající úkol.
- **Vstupní podmínky:** V seznamu je 1 úkol.
- **Kroky testu:**
  1. Zadat `3`, pak `1`.
  2. Zadat `2`.
- **Očekávaný výsledek:** Úkol se smaže, seznam je prázdný.
- **Skutečný výsledek:** Úkol se smazal, vypsalo se „Seznam úkolů je prázdný.“
- **Stav:** Pass
- **Poznámky:** Hraniční případ ze zadání.

### TC16: Odstranění z prázdného seznamu
- **Popis:** Ověření, co se stane, když není co mazat.
- **Vstupní podmínky:** Seznam je prázdný.
- **Kroky testu:**
  1. Zadat `3`.
- **Očekávaný výsledek:** Hláška a návrat do menu bez ptaní na číslo.
- **Skutečný výsledek:** Vypsalo se „Seznam úkolů je prázdný, není co odstranit.“
- **Stav:** Pass
- **Poznámky:** Hraniční případ.
