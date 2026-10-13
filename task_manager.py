ukoly = []


def hlavni_menu() -> None:
    """Zobrazuje hlavní menu, dokud uživatel nezvolí konec programu."""
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu.")
            break
        else:
            print("Neplatná volba.")


def pridat_ukol() -> None:
    """Načte název a popis úkolu a uloží ho. Při prázdném vstupu se ptá znovu."""
    while True:
        nazev = input("\nZadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()

        if nazev == "" or popis == "":
            print("Název ani popis úkolu nesmí být prázdný.")
        else:
            break

    ukoly.append({
        "nazev": nazev,
        "popis": popis
    })

    print(f"Úkol '{nazev}' byl přidán.")


def zobrazit_ukoly() -> None:
    """Vypíše všechny úkoly očíslované od 1."""
    if len(ukoly) == 0:
        print("\nSeznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")

    for cislo, ukol in enumerate(ukoly, 1):
        print(f"{cislo}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol() -> None:
    """Zobrazí úkoly a smaže ten, jehož číslo uživatel zadá. Při chybě se ptá znovu."""
    if len(ukoly) == 0:
        print("\nSeznam úkolů je prázdný, není co odstranit.")
        return

    zobrazit_ukoly()

    while True:
        cislo = input("\nZadejte číslo úkolu, který chcete odstranit: ").strip()

        if not cislo.isdecimal():
            print("Neplatný vstup, zadejte číslo úkolu.")
            continue

        cislo = int(cislo)

        if cislo < 1 or cislo > len(ukoly):
            print("Takový úkol neexistuje.")
            continue

        break

    odstraneny_ukol = ukoly.pop(cislo - 1)

    print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.")


if __name__ == "__main__":
    hlavni_menu()
