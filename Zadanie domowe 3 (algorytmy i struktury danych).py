import random, os

#=======================================================================================
#=======================================================================================
#KLASY RÓŻNYCH STRUKTUR DANYCH

class Node:         #węzeł
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.left = None
        self.right = None

class Stack:        #stos
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

class Queue:        #kolejka
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return


class DoublyLinkedList:     #lista dwukierunkowa
    def __init__(self):
        self.first = None
        self.last = None

    def get_node(self, index):
        current = self.first
        for i in range(index - 1):
            if current is None:
                return None
            current = current.next
        return current

    def insert_at_beg(self, new_node):
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.insert_before(self.first, new_node)

    def insert_before(self, ref_node, new_node):
        new_node.next = ref_node
        if ref_node.prev is None:
            self.first = new_node
        else:
            new_node.prev = ref_node.prev
            new_node.prev.next = new_node
        ref_node.prev = new_node

    def display(self):
        current = self.first
        while current:
            print(current.data, end=' ')
            current = current.next

class Binary_Tree:      #drzewo binarne
    def __init__(self, data):
        self.root = Node(data)

#=======================================================================================
#=======================================================================================
#PRZYKŁADOWE DRZEWA

def drzewo_binarne(x):
    T = Binary_Tree(x)
    T.root.left = Node(10)
    T.root.left.left = Node(10)
    T.root.left.right = Node(7)
    T.root.left.left.left = Node(6)
    T.root.left.left.right = Node(5)
    T.root.left.left.left.left = Node(10)
    T.root.right = Node(5)
    T.root.right.left = Node(7)
    T.root.right.right = Node(10)
    T.root.right.left.left = Node(2)
    T.root.right.left.right = Node(7)
    T.root.right.right.right = Node(10)
    return T

def drzewo_BST():
    T = Binary_Tree(30)
    T.root.left = Node(20)
    T.root.left.left = Node(10)
    T.root.left.right = Node(21)
    T.root.left.left.left = Node(5)
    T.root.left.left.right = Node(15)
    T.root.left.left.left.left = Node(3)

    T.root.right = Node(55)
    T.root.right.left = Node(40)
    T.root.right.right = Node(65)
    T.root.right.left.left = Node(35)
    T.root.right.left.right = Node(45)
    T.root.right.right.right = Node(80)
    return T

#=======================================================================================
#=======================================================================================
#ISTOTNE FUNKCJE Z POSZCZEGÓLNYCH ZADAŃ

#Funkcje do zadania 1
def zadanie1(n, a, b):
    S = Stack()
    for i in range(n):
        S.push(random.randint(a, b))
    A = []
    print("\nElementy stosu: ", end="")
    for i in range(n):
        element = S.pop()
        A.append(element)
        print(element, end=" ")
    print("\nTablica przed sortowaniem: ", A)
    for i in range(0, n - 1):
        k = i
        for j in range(i + 1, n):
            if A[j] > A[k]:
                k = j
        A[i], A[k] = A[k], A[i]
    print("Posortowana tablica: ", A)
    Q = Queue()
    print("Elementy kolejki: ", end="")
    for i in range(n):
        Q.enqueue(A[i])
    for i in range(n):
        print(Q.dequeue(), end=" ")
    print("\n")

#Funkcje do zadania 2
def lista(n, a, b):
    nowa_lista = DoublyLinkedList()
    for i in range(n):
        new_node = Node(random.randint(a, b))
        nowa_lista.insert_at_beg(new_node)
    return nowa_lista

def WKLEJ(L, M, x):
    if x == L.last:
        x.next = M.first
        M.first.prev = x
        L.last = M.last
    else:
        M.last.next = x.next
        x.next.prev = M.last
        x.next = M.first
        M.first.prev = x

#Funkcje do zadania 3
def zadanie3():
    print("\nOto odpowiedź do zadania 3:\n\nPREORDER: 7, 2, 1, 5, 4, 11, 8, 14, 15\nINORDER: 1, 2, 4, 5, 7, 8, 11, 14, 15\nPOSTORDER: 1, 4, 5, 2, 8, 15, 14, 11, 7\n")

#Funkcje do zadania 4
def licz_klucze(root, r): #r to też root tylko że się nie zmienia jest stały; r.data odzwierciedla wartość korzenia
    ret_val = 0
    if root is not None:
        if root.left is not None:
            if root.left.data == r.data:
                ret_val += 1 + licz_klucze(root.left, r)
            else:
                ret_val += 0 + licz_klucze(root.left, r)
        if root.right is not None:
            if root.right.data == r.data:
                ret_val += 1 + licz_klucze(root.right, r)
            else:
                ret_val += 0 + licz_klucze(root.right, r)
    return ret_val

licznik = 0     #zmienna globalna
def licz(root, r):      #jest tu druga wersja tej samej fnkcji co jest powyżej
    global licznik
    if root is not None:
        if root.left is not None:
            if root.left.data == r.data:
                licznik += 1
            licz(root.left, r)
        if root.right is not None:
            if root.right.data == r.data:
                licznik += 1
            licz(root.right, r)
    return licznik

#Funkcje do zadania 5
def ROZPIETOSC(drzewo_BST):
    left_branch = drzewo_BST.root
    right_branch = drzewo_BST.root
    while left_branch:
        min = left_branch.data
        left_branch = left_branch.left
    while right_branch:
        max = right_branch.data
        right_branch = right_branch.right
    print("Najmniejsza wartość klucza: ", min)
    print("Największa wartość klucza: ", max)
    return  max - min

#=======================================================================================
#=======================================================================================
#FUNKCJE "POMOCNICZE"

def wstawianie(a, dodatnia = True):
    while True:
        try:
            n = int(input("\n{}: ".format(a)))
            if dodatnia:
                if n < 1:
                    print("\nLiczba musi być większa od 0!!!\n")
                    continue
            break
        except ValueError:
            print("\nPodaj liczbę!!!\n")
    return n

def dolny_zakres():
    while True:
        try:
            x = int(input("\nPodaj dolny zakres liczb, które będą wylosowane: "))
            break
        except ValueError:
            print("\nPodaj liczbę!!!\n")
    return x

def gorny_zakres(x):
    while True:
        try:
            y = int(input("\nPodaj górny zakres liczb, które będą wylosowane: "))
            if y <= x:
                print("\nGórny zakres musi być większy od dolnego zakresu!!!\n")
                continue
            break
        except ValueError:
            print("\nPodaj liczbę!!!\n")
    return y

#=======================================================================================
#=======================================================================================
#PROGRAM GŁÓWNY

while True:
    os.system("cls")
    answer = None
    while answer not in ("1", "2", "3", "4", "5"):
        answer = input("\nKtóre zadanie domowe ma być pokazane przez program? 1, 2, 3, 4 czy 5? ")

    if answer == "1":
        os.system("cls")
        print("\nZaraz program utworzy stos.")
        n = wstawianie("Podaj długość stosu")
        x = dolny_zakres()
        y = gorny_zakres(x)
        os.system("cls")
        zadanie1(n, x, y)

    if answer == "2":
        os.system("cls")
        print("\nZaraz program wygeneruje dwie listy dwukierunkowe 'L' i 'M'.")
        n = wstawianie("Podaj długość listy 'L'")
        x = dolny_zakres()
        y = gorny_zakres(x)
        L = lista(n, x, y)
        os.system("cls")

        nn = wstawianie("Podaj długość listy 'M'")
        x = dolny_zakres()
        y = gorny_zakres(x)
        M = lista(nn, x, y)
        os.system("cls")

        print("Lista 'L': ", end="")
        L.display()
        print("\nLista 'M': ", end="")
        M.display()

        x = n + 1
        while x > n:
            x = wstawianie("Po którym elemencie listy 'L' chcesz wstawić liste 'M'? ")
            if x > n:
                print("\nTa liczba nie może być większa od ilości elementów listy 'L'!!!\n")
        WKLEJ(L, M, L.get_node(x))
        print("\nLista 'L' po dodaniu listy 'M': ", end="")
        L.display()

    if answer == "3":
        os.system("cls")
        zadanie3()

    if answer == "4":
        os.system("cls")
        x = wstawianie("Zaraz podasz wartość klucza korzenia drzewa binarnego, które zaraz będzie utworzone.\n"
                      "Podpowiedź: wpisz 10, 7, 6, 5 lub 2. To właśnie te pola kluczy się powtarzają w innych węzłach.\n"
                      "Podaj liczbę", False)
        T = drzewo_binarne(x)
        print("\nZliczone klucze:", licz_klucze(T.root, T.root))
        print("\nZliczone klucze:", licz(T.root, T.root))
        licznik = 0

    if answer == "5":
        os.system("cls")
        print("\nZaraz zostanie utworzone przykładowe drzewo BST.\n")
        T = drzewo_BST()
        print("Różnica pomiędzy największą i najmniejszą wartością klucza w drzewie T wynosi: ", ROZPIETOSC(T))

    ans = ""
    while ans not in ("T", "t", "N", "n"):
        ans = input("\nCzy chcesz aby jeszcze jakieś zadanie było pokazane przez program? (t/n) ")
    if ans == "T" or ans == "t":
        continue
    break
