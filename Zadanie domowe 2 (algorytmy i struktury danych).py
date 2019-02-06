import random

def SUMACYFR(n):
    if n > 0:
        return n%10 + SUMACYFR(n//10)
    return 0

def f(n, k):                #W programie głównym zablokowałem możliwość wproadzenia k większego od n.
    if n == k:
        return 1
    if n > 0 and k == 0:    #Dla tych sytuacji od razu zwracam wartości 1 i 0
        return 0            #by nie marnować pamieci na niepotrzbne tworzenie macierzy i obliczenia.

    A = [[None] * (k + 1) for i in range(n + 1)]
    for i in range(k + 1):
        A[i][i] = 1
    for i in range(1, n + 1):
        A[i][0] = 0
    for i in range(2, n + 1):
        for j in range(1, min(i, k + 1)):
            A[i][j] = i * A[i - 1][j] + j * A[i - 1][j - 1]
    print(A)
    return A[n][k]

def ff(n,k):            #Jest to funkcja rekurencyjna
    if n == k:          #Służy mi do sprawdzania poprawności wyników z funkcji napisanej w stylu programowania dynamicznego
        return 1
    if n>0 and k == 0:
        return 0
    if n > 0 and 1 <= k and k <= n -1:
        return n * f(n - 1, k) + k * f(n - 1, k - 1)

def zadanie3(n, x, y):
    tab = []
    for i in range(2 * n):
        tab.append(random.randint(x, y + 1))
    print("Oto nieposortowany ciąg liczb losowych:")
    print(tab)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if tab[j] > tab[j - 1]:
                tab[j], tab[j - 1] = tab[j - 1], tab[j]
    for j in range(n +1, (2 * n)):
        r = tab[j]
        i = j - 1
        while i > n - 1 and tab[i] > r:
            tab[i + 1] = tab[i]
            i -= 1
        tab[i + 1] = r
    print("\nOto ciąg posortowany zgodnie z treścią zadania trzeciego:")
    print(tab)

def zadanie5(n, x, y):
    A = [[None] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = random.randint(x, y)
    s = []
    for i in range(n):
        print(A[i], end="")
        suma = 0
        for j in range(n):
            suma += A[i][j]
        print("   suma: ", suma)
        s.append(suma)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if s[j] < s[j - 1]:
                s[j], s[j - 1] = s[j - 1], s[j]
                A[j], A[j - 1] = A[j - 1], A[j]
    print()
    for i in range(n):
        print(A[i], end="")
        suma = 0
        for j in range(n):
            suma += A[i][j]
        print("   suma: ", suma)

def zadanie4(A, n):
    B = []
    print("\nOto ciąg odwrotnie V-kształtny:")
    print(A)
    i1 = 0
    i2 = -1
    for i in range(n):
        if A[i1] < A[i2]:
            B.append(A[i1])
            i1 += 1
        else:
            B.append(A[i2])
            i2 -= 1
    print("\nOto ciąg posortowny:")
    print(B)

def czy_v(A):
    rosnace = True
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            rosnace = False
        if A[i - 1] < A[i] and not rosnace:
            return False
    return A[0] <= A[1] and not rosnace


while True:
    answer = None
    while answer not in ("1", "2", "3", "4", "5"):
        answer = input("\nKtóre zadanie domowe ma być pokazane przez program? 1, 2, 3, 4 czy 5? ")

    if answer == "1":
        print("\nZaraz podasz liczby: 'n' i 'k' do obliczenia funkcji f(n, k). \nPamiętaj, że 'k' musi być większe lub równe zero \na 'n' musi być większe lub równe 'k'.\n")
        n = -1
        k = -1
        while n < 0:
            while True:
                try:
                    n = int(input("Podaj 'n': "))
                    if n < 0:
                        print("\n'n' nie może być liczbą ujemną!!!\n")
                    break
                except ValueError:
                    print("\nPodaj liczbę!!!\n")
        while k < 0 or k > n:
            while True:
                try:
                    k = int(input("Podaj 'k': "))
                    if n < k:
                        print("\n'k' musi być mniejsze lub równe 'n'!!!\n")
                    if k < 0:
                        print("\n'k' nie może być liczbą ujemną!!!\n")
                    break
                except ValueError:
                    print("\nPodaj liczbę!!!\n")

        print("\nWynik funkcji f(%d, %d) wynosi: %d "%(n, k, f(n, k)))

    if answer == "2":
        print("\nZaraz program obliczy sumę cyfr liczby, którą za chwilę podasz. \nPamiętaj, że musi to być liczba naturalna.\n")
        n = -1
        while n < 0:
            while True:
                try:
                    n = int(input("Podaj 'n': "))
                    break
                except ValueError:
                    print("\nPodaj liczbę!!!\n")
        print("\nSuma cyfr liczby", n, "wynosi: ", SUMACYFR(n))

    if answer == "3":
        print("\nZaraz program wygeneruje ciąg liczb losowych. \nNastępnie posortuje liczby 'a[1], a[2] ... a[n]' malejąco \na liczby 'a[n+1], a[n+2] ... a[2*n] rosnąco.\nPamiętaj, że 'n' musi być większe lub równe 2.\n")
        n = 0
        while n < 2:
            while True:
                try:
                    n = int(input("Podaj 'n': "))
                    break
                except ValueError:
                    print("\nPodaj liczbę!!!\n")
        while True:
            try:
                x = int(input("\nPodaj dolny zakres liczb, które będą wylosowane: "))
                break
            except ValueError:
                print("\nPodaj liczbę!!!\n")
        while True:
            try:
                y = int(input("\nPodaj górny zakres liczb, które będą wylosowane: "))
                if y <= x:
                    print("\nGórny zakres musi być większy od dolnego zakresu!!!\n")
                    continue
                break
            except ValueError:
                print("\nPodaj liczbę!!!\n")
        zadanie3(n, x, y)

    if answer == "4":
        while True:
            try:
                n = int(input("\nPodaj długość ciągu, który ma być utworzony: "))
                break
            except ValueError:
                print("\nPodaj liczbę!!!\n")
        print("\nCzy chcesz podać własny ciąg odwrotnie V-kształtny? \nJeśli nie to program wygeneruje losowe elementy ciągu odwrotnie V-kształtnego (t/n) ", end="")
        A = []
        B = []
        ans = ""
        while ans not in ("T", "N", "t", "n"):
            ans = input()
        if ans == "T" or ans == "t":
            print("\nWprowadź poprawne wartości!\n")
            print("\nPodaj wartości ciągu\n")
            while True:
                for i in range(n):
                    while True:
                        try:
                            A.append(int(input()))
                            break
                        except ValueError:
                            print("\nPodaj liczbę!!!\n")
                if czy_v(A):
                    break
                else:
                    print("\nTo nie jest ciąg odwrotnie V-kształtny!\n")
                    print("\nPodaj ponownie wartości ciągu!\n")
                    A = []
                    continue
        if ans == "N" or ans == "n":
            while True:
                try:
                    x = int(input("\nPodaj dolny zakres liczb, które będą wylosowane: "))
                    break
                except ValueError:
                    print("\nPodaj liczbę!!!\n")
            while True:
                try:
                    y = int(input("\nPodaj górny zakres liczb, które będą wylosowane: "))
                    if y <= x:
                        print("\nGórny zakres musi być większy od dolnego zakresu!!!\n")
                        continue
                    break
                except ValueError:
                    print("\nPodaj liczbę!!!\n")
            while True:
                try:
                    g = int(input("\nObecnie generowany ciąg odwrotnie V-kształtny jest będzie składany z dwóch mniejszych ciągów(A i B). \nPodaj długość tj. ilość elementów pierwszego ciągu(A): "))
                    if n <= g:
                        print("\nPodaj liczbę mniejszą od długości ciągu!!!\n")
                        continue
                    break
                except ValueError:
                    print("\nPodaj liczbę!!!\n")
            for i in range(g):
                A.append(random.randint(x, y))
            A.sort()
            print("Ciąg A: ", A)
            for i in range(n - g):
                B.append(random.randint(x, y))
            B.sort()
            B.reverse()
            print("Ciąg B: ", B)
            A = A + B
        zadanie4(A, n)

    if answer == "5":
        print("\nZaraz zostanie utworzona dwuwymiarowa lista. \nPodaj liczbę 'n', która będzie określać długość wierszy i długość kolumn.\nPamiętaj, że 'n' musi być większe lub równe 1. \nOczywiście jeśli podasz do 'n' wartość 1 to zadanie nie będzie miało większego sensu. \nProponuję podać wartość nie mniejszą niż 3.\n")
        n = -1
        while n < 1:
            while True:
                try:
                    n = int(input("Podaj 'n': "))
                    break
                except ValueError:
                    print("\nPodaj liczbę!!!\n")
        while True:
            try:
                x = int(input("\nPodaj dolny zakres liczb, które będą wylosowane: "))
                break
            except ValueError:
                print("\nPodaj liczbę!!!\n")
        while True:
            try:
                y = int(input("\nPodaj górny zakres liczb, które będą wylosowane: "))
                if y <= x:
                    print("\nGórny zakres musi być większy od dolnego zakresu!!!\n")
                    continue
                break
            except ValueError:
                print("\nPodaj liczbę!!!\n")
        print()
        zadanie5(n, x, y)

    ans = ""
    print("\nCzy chcesz aby jeszcze jakieś zadanie było pokazane przez program? (t/n) ", end="")
    while ans not in ("T", "t", "N", "n"):
        ans = input()
    if ans == "T" or ans == "t":
        continue
    break

input()

