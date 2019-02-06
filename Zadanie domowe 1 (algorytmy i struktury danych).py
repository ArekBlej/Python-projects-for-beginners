import random

def zadanie1(m, n):
    if czy_pierwsza(m) and czy_pierwsza(n):
        if m + 2 == n or m - 2 == n:
            print(m, "i", n, "to liczby bliźniacze")
        else:
            print(m, "i", n, "nie są liczbami bliźniaczymi")
    else:
        print(m, "i", n, "nie są liczbami bliźniaczymi")

def czy_pierwsza(m):
   a = 2
   if m < a:
       print(m, "nie jest liczbą pierwszą")
       return False
   while True:
       if a == m:
           print(m, "jest liczbą pierwszą")
           return True
       if m % a == 0:
           print(m, "nie jest liczbą pierwszą")
           return False
       a += 1

def zadanie22(k):
    liczba_bin1 = bin(2*k-1)[2:]
    liczba_bin2 = bin(2*k-2)[2:]
    ile = 0
    for i in liczba_bin1:
        if i == "1":
            ile += 1
    if ile % 2 == 0:
        print(int(liczba_bin1, 2), "jest %s-tą liczbą królewską" %k)
    ile = 0
    for i in liczba_bin2:
        if i == "1":
            ile += 1
    if ile % 2 == 0:
        print(int(liczba_bin2, 2), "jest %s-tą liczbą królewską" %k)

def zadanie2(k):
    liczba_bin1 = dzies_na_bin(2*k-1)
    liczba_bin2 = dzies_na_bin(2*k-2)
    ile = 0
    for i in liczba_bin1:
        if i == "1":
            ile += 1
    if ile % 2 == 0:
        print(bin_na_dzies(liczba_bin1), "jest %s-tą liczbą królewską" %k)
    ile = 0
    for i in liczba_bin2:
        if i == "1":
            ile += 1
    if ile % 2 == 0:
        print(bin_na_dzies(liczba_bin2), "jest %s-tą liczbą królewską" %k)

def bin_na_dzies(n):
    n = reversed(str(n))
    l = 0
    m = 0
    for i in n:
        m += int(i)*2**l
        l += 1
    return m

def dzies_na_bin(n):
    i = ""
    while n != 0:
        i = str(n%2) + i
        n = n//2
    return i



def zadanie3(n, m):
    tab = []
    for i in range(n):
        tab.append(random.randint(2, m))
    max1 = 0
    max2 = 0
    for i in range(n):
        if tab[i] > max1:
            max1 = tab[i]
    for i in range(n):
        if tab[i] != max1:
            if tab[i] > max2:
                max2 = tab[i]
    if max1 == max2:
        print("Wszystkie liczby listy są sobie równe tzn. że nie ma drugiej co do wartości liczby w tym ciągu")
    elif max2 < max1:
        print("Drugą co do wartości liczbą w tym ciągu jest", max2)
    print("Sprawdzenie wizualne ciągu: ", tab)

def zadanie4(n, m):
    a = 1
    b = 0
    tab = []
    for i in range(n):
        tab.append(random.randint(2, m))
    for i in range(1, n):
        if tab[i] == tab[i-1]:
            a += 1
        else:
            if a > b:
                b = a
                a = 1
    print("Najdłuższy podciąg zawiera", b, "liczb(y)")
    print("Sprawdzenie wizualne ciągu: ", tab)

answer = None
while answer not in ("1", "2", "3", "4"):
    answer = input("Które zadanie domowe ma być pokazane przez program? 1,2,3 czy 4? ")
if answer == "1":
    m, n = 0, 0
    while m < 1 or n < 1:
        m = int(input("Podaj liczbę naturalną m "))
        n = int(input("Podaj liczbę naturalną n "))
    zadanie1(m, n)
elif answer == "2":
    k = 0
    while k < 1:
        k = int(input("Podaj liczbę naturalną k "))
    zadanie2(k)
elif answer == "3":
    m, n = 0, 0
    while m < 1 or n < 1:
        m = int(input("Podaj liczbę naturalną m, która będzie możliwie maksymalną losową liczbą: "))
        n = int(input("Podaj liczbę naturalną n, która stanowi o długości ciągu: "))
    zadanie3(n, m)
elif answer == "4":
    m, n = 0, 0
    while m < 1 or n < 1:
        m = int(input("Podaj liczbę naturalną m, która będzie możliwie maksymalną losową liczbą: "))
        n = int(input("Podaj liczbę naturalną n, która stanowi o długości ciągu: "))
    zadanie4(n, m)
