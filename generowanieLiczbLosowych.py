# Czasami programy wymagają generowania losowych liczb, na przykład jeśli symulujemy kostkę do gry lub rzut monetą. W tych przypadkach, powinniśmy losować liczbę od 1 do 6 (kostka) lub 0 i 1 (rzut monetą) (Rysunek 4).
# Do tego użyjemy poznanej biblioteki random. Napiszmy program w którym komputer będzie generował losową liczbę i wyświetlał ją na ekranie. Niech te liczby będą w przedziale od 1 do 6 (jak kostka do gry).
# Rozważmy sytuację: numer 6 na kostce wygrywa. Ile razy wypadnie 6 jeśli podejmiemy 20 prób?

import random

liczba_wystapien_6 = 0
for i in range(20):
    magiczna_liczba = random.randint(1,6)
    print(magiczna_liczba)
    if magiczna_liczba == 6:
        liczba_wystapien_6 += 1

print(f"Trafiles 6: {liczba_wystapien_6} razy")