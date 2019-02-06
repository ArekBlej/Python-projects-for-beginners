import random

def Sorting1(lista):
    for i in range(len(lista)):
        j = len(lista) - 1
        while i < j:
            if lista[j] > lista[j-1]:
                schowek = lista[j]
                lista[j] = lista[j-1]
                lista[j-1] = schowek
            j -= 1
    return lista

def Sorting2(lista):
    for i in range(len(lista)):
        j = 0
        while j <= len(lista):
            try:
                if lista[j] > lista[j+1]:
                    schowek = lista[j]
                    lista[j] = lista[j+1]
                    lista[j + 1] = schowek
                j += 1
            except IndexError:
                break
    return lista

print("Jest to program sortujący")
lista = []

n = int(input("Podaj ilość losowych elementów naszej listy: "))
up = int(input("Podaj górny pułap zbioru, z którego będą losowane liczby: "))
down = int(input("Podaj dolny pułap zbioru, z którego będą losowane liczby: "))

print("\nOto lista zawierająca losowe liczby:")
for i in range(n):
    lista.append(random.randrange(down,up))
    print(lista[-1], end=" ")

print("\n\nTeraz nastąpi losowanie!")
Sorting1(lista)

print("\nOto posortowana lista:")
for i in lista:
    print(i, end=" ")



