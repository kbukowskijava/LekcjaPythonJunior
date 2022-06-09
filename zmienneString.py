słowo = "czesc"
słowo2 = "Kacper"
zdanie = "zGadNij moJa LiCZBe "
zdanie2 = "Zielony piesek ma wlosy wlosy"
# Cześć!
# C z e ś ć !
# 0 1 2 3 4 5
# 67 122 101 115 99 33
print(len(słowo))
print(słowo * 3 + słowo2)
print(chr(71))

for i in range(len(słowo)):
    print(chr(ord(słowo[i]) - 32))

print(słowo.upper())
print(zdanie.capitalize())
print(zdanie.title())
print(zdanie.upper())
print(zdanie.lower())

print(zdanie.lower().rfind("a"))
print(zdanie2.replace("wlosy", "uszy"))
print(zdanie2.count("wlosy"))
print(zdanie2.replace(" ", "").isalpha())

temp_isalpha = False

for i in range(len(zdanie2)):
    if ord(zdanie2[i]) <= 90 and ord(zdanie2[i]) >= 65:
        temp_isalpha = True
    elif ord(zdanie2[i]) <= 122 and ord(zdanie2[i]) >= 97:
        temp_isalpha = True
    else:
        temp_isalpha = False
        break

print(temp_isalpha)
print(zdanie2[zdanie2.find("p"):zdanie2.find("k")+1:2])

