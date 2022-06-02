import math
import random

# a = 2
# b = 3
# a += 1 #inkrementacja (a = a + 1)
# b -= 1 #dekrementacja (a = a - 1)
# print(a)
# print(b)

print("Wybierz konwerter: \n")
print("1.mile -> km \n")
print("2.parseki -> km\n")
print("3.gramy -> kilogramy")

wybor = input()

if int(wybor) == 1:
    # #zadanie - konwersja mil na kilometry
    n = input("Wprowadź mile: ") #int
    mila = 1.609 #float
    #konwersja mil na kilometry
    km = float(n) * mila
    print(f"{n} mil = {km} km")
elif int(wybor) == 2:
    # zadanie - konwersja paresków na kilometry
    n = input("Wprowadź parseki: ")
    pc = 3.0857 * math.pow(10, 16)
    #konwersja parseków na kilometry
    km = float(n) * pc
    print(f"{n} parseków = {km} km")
elif int(wybor) == 3:
    n = input("Wprowadź gramy: ")
    kg = float(n) / 1000
    print(f"{n} gramów = {kg} kg")
else:
    print("Nie ma takiej opcji w menu!")

