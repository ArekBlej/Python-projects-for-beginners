def Fibonaci_1(n):
    a, b = 0, 1
    while n >= 1:
        print(b, end=" ")
        a, b = b, a+b
        n -= 1

def Fibonaci_2(n):
    a, b = 0, 1
    for i in range(n):
        print(b, end=" ")
        a, b = b, a+b

def Fibonaci_3(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return Fibonaci_3(n-1) + Fibonaci_3(n-2)

x = int(input("Podaj n, które będzis stanowić o długości ciągu Fibonaciego: "))
Fibonaci_1(x)
print()
Fibonaci_2(x)
print()
print(Fibonaci_3(x))