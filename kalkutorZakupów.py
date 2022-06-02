import math

price_1 = 270 #cena do 0,5kg
price_2 = 200 #cena powyżej 0,5kg

gramy = input("Wprowadź wagę (gramy): ")
kg = float(gramy) / 1000
print(f"Twoje zakupy to: {kg} kg")

if kg < 0.5:
    total = kg * price_1
else:
    total = kg * price_2
total = math.ceil(total)
print(f"Kwota do zapłaty: {total} monet")