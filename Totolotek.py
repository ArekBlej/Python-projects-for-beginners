import random

liczba = random.randint(1,10)
print("Wylosowana liczba:", liczba)
i = 3
while i>0:
    odp = int(input(f"Zgadnij jaka jest wylosowana liczba. Masz {i} próby: "))
    if odp == liczba:
        print("Zgadłeś!")
        i=0
    else:
        print("Nie zgadłeś :(")
    i -= 1
print("\nKoniec gry.")