import random

liczba_wystapien_parzystej = 0
suma_parzystych = 0
suma_wszystkich = 0

for i in range(20):
    magiczna_liczba = random.randint(12, 24)
    suma_wszystkich += magiczna_liczba
    print(magiczna_liczba)
    if magiczna_liczba % 2 == 0:
        liczba_wystapien_parzystej += 1
        suma_parzystych += magiczna_liczba

print(f"Trafiles w parzysta: {liczba_wystapien_parzystej} razy\n")
print(f"Suma liczb parzystych wynosi: {suma_parzystych}")
print(f"Suma wszystkich wylosowanych liczb wynosi: {suma_wszystkich}")
