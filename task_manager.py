ukoly = []


def hlavni_menu():
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


def pridat_ukol():
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


def zobrazit_ukoly():
    if len(ukoly) == 0:
        print("\nSeznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")

    for cislo, ukol in enumerate(ukoly, 1):
        print(f"{cislo}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol():
    if len(ukoly) == 0:
        print("\nSeznam úkolů je prázdný, není co odstranit.")
        return

    zobrazit_ukoly()

    cislo = input("\nZadejte číslo úkolu, který chcete odstranit: ").strip()

    if not cislo.isdigit():
        print("Neplatný vstup, zadejte číslo úkolu.")
        return

    cislo = int(cislo)

    if cislo < 1 or cislo > len(ukoly):
        print("Takový úkol neexistuje.")
        return

    odstraneny_ukol = ukoly.pop(cislo - 1)

    print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.")


if __name__ == "__main__":
    hlavni_menu()
