import random

print("DUŻY LOTEK\n")
liczba = []


for i in range(6):
    p = True
    while p:
        l = int(input("Wpisz liczbę. Pamiętaj aby znajdowała się w przedzaile 1-49. "))
        if l >= 1 and l <= 49:
            liczba.append(l)
            p = False
        else:
            print("Podałeś liczbę z poza przedziału. Ponów próbę.")

losowa = []
print("\nNastępuje losowanie liczb\n")

for j in range(6):
    losowa.append(random.randint(1,49))

trafione = []
x = 0

for k in range(6):
    for m in range(6):
        if losowa[k-1] == liczba[m-1]:
            trafione.append(liczba[m])
            x += 1

print("Oto liczby, które trafiłeś:\n")
for s in range(x):
    print(trafione[s-1])

print("Oto liczby, które wylosowała maszyna losująca:\n")
for z in range(6):
    print(losowa[z-1])



