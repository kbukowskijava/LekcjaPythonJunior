import datetime as dt

print("---------------------------------------\n")
print("Wciśnij 1 jeśli chcesz informacje o roku (365 lub 366 dni).")
print("Wciśnij 2 jeśli chcesz informacje o grupie wiekowej.")
print("Wciśnij 3 jeśli chcesz poznać wartość wieku w sekundach.\n")
print("---------------------------------------")

dzien_urodzenia = int(input("Twój dzień urodzenia to: \n"))
miesiac_urodzenia = int(input("Twój miesiac urodzenia to: \n"))
rok_urodzenia = int(input("Twój rok urodzenia to: \n"))

dzien = int(dt.date.today().day)
miesiac = int(dt.date.today().month)
rok = int(dt.date.today().year)

if miesiac > miesiac_urodzenia:
    wiek = rok - rok_urodzenia
else:
    wiek = (rok - rok_urodzenia) - 1

wybrana_opcja = int(input("Podaj pozycje z menu: \n"))

if (wybrana_opcja > 0) and (wybrana_opcja < 4) and (wiek >= 0) and (wiek < 118):
    if wybrana_opcja == 1:
        # pierwsza opcja z menu
        if rok_urodzenia % 4 != 0:
            print("Jest to zwykły rok (365 dni)")
        else:
            print("Jest to rok przestępny (366 dni)")
    elif wybrana_opcja == 2:
        # druga opcja z menu
        if wiek < 1:
            print("Dziecko")
        elif (wiek >= 1) and (wiek < 3):
            print("Raczkujacy")
        elif (wiek >= 3) and (wiek < 5):
            print("Przedszkolak")
        elif (wiek >= 5) and (wiek < 12):
            print("Uczen")
        elif (wiek >= 12) and (wiek < 19):
            print("Nastolatek")
        elif wiek >= 19:
            print("Dorosły")
    elif wybrana_opcja == 3:
        # trzecia opcja z menu
        print(f"Twój wiek: {wiek} lat, {12 - abs(miesiac_urodzenia - miesiac)} miesiecy, {30 - abs(dzien - dzien_urodzenia)} dni")
        sekundy = (wiek * 365 * 24 * 60 * 60) + ((miesiac - 1) * 30 * 24 * 60 * 60) + ((dzien - 1) * 24 * 60 * 60)
        print(f"Twój wiek w sekundach to {sekundy}")
else:
    print("Wystąpił błąd programu!\n")
