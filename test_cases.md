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
- **Poznámky:** Ověřuje, že se uživatel dostane k přehledu úkolů a po výpisu se vrátí do menu.

### TC03: Volba 4 – konec programu
- **Popis:** Ověření, že volba 4 ukončí program.
- **Vstupní podmínky:** Je zobrazené hlavní menu.
- **Kroky testu:**
  1. Zadat `4`.
- **Očekávaný výsledek:** Vypíše se „Konec programu.“ a program skončí.
- **Skutečný výsledek:** Vypsalo se „Konec programu.“, program skončil.
- **Stav:** Pass
- **Poznámky:** Volba 4 je jediný řádný způsob ukončení – smyčka menu nesmí běžet dál.

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
- **Poznámky:** Doplňuje TC07 – kontrola musí platit pro obě pole, nejen pro název.

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
- **Poznámky:** Správné číslování je důležité, protože podle něj uživatel úkoly maže.

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
- **Poznámky:** Ověřuje i přečíslování zbývajících úkolů po smazání.

### TC13: Číslo, které neexistuje
- **Popis:** Ověření upozornění při zadání čísla mimo seznam.
- **Vstupní podmínky:** V seznamu jsou 2 úkoly.
- **Kroky testu:**
  1. Zadat `3`, pak `5`.
  2. Na novou výzvu zadat `0`.
  3. Na novou výzvu zadat `1`.
- **Očekávaný výsledek:** U `5` a `0` upozornění, nic se nesmaže a program se znovu zeptá na číslo. Po zadání platného čísla `1` se smaže úkol č. 1.
- **Skutečný výsledek:** U `5` i `0` se vypsalo „Takový úkol neexistuje.“ a nová výzva k zadání čísla. Po zadání `1` se vypsalo „Úkol 'Nakup' byl odstraněn.“
- **Stav:** Pass
- **Poznámky:** Číslo 0 je důležité – bez kontroly by se smazal poslední úkol.

### TC14: Text, záporné číslo nebo speciální znak místo čísla
- **Popis:** Ověření, že program nespadne, když nezadám číslo.
- **Vstupní podmínky:** V seznamu je aspoň 1 úkol.
- **Kroky testu:**
  1. Zadat `3`, pak `abc`.
  2. Na novou výzvu zadat `-1`.
  3. Na novou výzvu zadat `²` (horní index).
- **Očekávaný výsledek:** Upozornění, nic se nesmaže, program se znovu zeptá na číslo a nespadne.
- **Skutečný výsledek:** Pokaždé se vypsalo „Neplatný vstup, zadejte číslo úkolu.“ a nová výzva k zadání čísla, program nespadl.
- **Stav:** Pass
- **Poznámky:** Negativní test. Znak `²` dříve prošel přes `isdigit()` a program spadl na `int()`; po změně na `isdecimal()` je ošetřen.

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

### TC17: Dva úkoly se stejným názvem
- **Popis:** Ověření, že program zvládne úkoly se stejným názvem a smaže jen ten vybraný.
- **Vstupní podmínky:** Seznam úkolů je prázdný.
- **Kroky testu:**
  1. Přidat úkol `Nákup` s popisem `mléko`.
  2. Přidat úkol `Nákup` s popisem `chleba`.
  3. Zadat `2`.
  4. Zadat `3`, pak `1`.
  5. Zadat `2`.
- **Očekávaný výsledek:** Oba úkoly se uloží a zobrazí pod čísly 1 a 2. Po smazání č. 1 zůstane jen `1. Nákup - chleba`.
- **Skutečný výsledek:** Zobrazilo se `1. Nákup - mléko` a `2. Nákup - chleba`. Po smazání č. 1 zůstal `1. Nákup - chleba`.
- **Stav:** Pass
- **Poznámky:** Program duplicitní názvy nezakazuje; díky mazání podle čísla se smaže správný úkol, i když mají úkoly stejný název.
