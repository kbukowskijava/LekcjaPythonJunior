import random

imie = input("Podaj swoje imie: ")

print("-----------------------------------")
print("-------Kamien, papier nozyce-------")
print(f"Witaj {imie} w grze")
print("Zwycieza osoba z wieksza iloscia punktów.")
print("\t[k] - kamien\n\t[p] - papier\n\t[n] - nozyce")

pkt_gracza = 0
wybor_gracza = 0
pkt_komp = 0
wybor_komp = 0

while True:
    czy_start = input("Czy chcesz rozpocząć? (y/n)")
    if czy_start == "y":
        print("-----------------------------------")
        print("------------START GRY-------------")
    for i in range(3):
        print("\t--------Runda №" + str(i + 1) + "--")
        wybor_komp = random.choice("kpn")
        print(wybor_komp)