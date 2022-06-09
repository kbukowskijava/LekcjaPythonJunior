import random

s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2 = "0123456789"
s3 = "~!@#$%^&*()_+{}[\]:/"
s = s1 + s1.lower() + s2 + s3
password = ""

x = input("Podaj długość hasła do wygenerowania: ")

for i in range(int(x)):
    p = random.choice(s)
    password += p

print(f"Twoje hasło: {password}")