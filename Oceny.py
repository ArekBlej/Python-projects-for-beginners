import ocenyfun

oceny = []
ile = int(input("Podaj ile chcesz wproawdzić ocen: "))
while ile >= 1:
    ocena = round(float(input("Dodaj ocenę ")), 1)
    oceny.append(ocena)
    ile -= 1

print(ocenyfun.srednia(oceny))
print(ocenyfun.mediana(oceny))
print(ocenyfun.wariancja(oceny, ocenyfun.srednia(oceny)))
print(ocenyfun.odchylenie(oceny, ocenyfun.srednia(oceny)))