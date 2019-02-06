klucz = 0

def szyfruj(txt):
    z = 0
    txt = txt.upper()
    zaszyfrowany = ""
    for i in range(len(txt)):
        #print(z)
        #print(ord(txt[i]), txt[i])
        if (ord(txt[i]) + klucz) > 90:
            roznica = ord(txt[i]) + klucz - 90
            z = roznica + 64
            zaszyfrowany += chr(z)
        else:
            z = ord(txt[i]) + klucz
            zaszyfrowany += chr(z)
    return zaszyfrowany

wyraz = input("Podaj wyraz do zaszyfrowania: ")
klucz = int(input("Podaj klucz od 1 do 26 "))
x = 0
for j in range(65, 91):
    litera = chr(j)
    x += 1
    tmp = litera + " => " + litera.lower() + " " + str(ord(litera))
    if j > 65 and x == 15:
        x = 0
        tmp += "\n"
    print(tmp, end=" ")
print("\n\n")
print(szyfruj(wyraz))

