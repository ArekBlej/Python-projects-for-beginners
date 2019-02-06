

def szyfruj(txt):
    KLU = int(input("Podaj klucz: "))
    KLUCZ = KLU % 26
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ :
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        elif ord(txt[i]) > 91 - KLUCZ and ord(txt[i]) < 91:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny

def deszyfruj(txt):
    KLU = int(input("Podaj klucz: "))
    KLUCZ = KLU % 26
    odszyfrowany = ""
    for i in range(len(txt)):
        if ord(txt[i]) - KLUCZ < 97 and ord(txt[i]) > 96:
            odszyfrowany += chr(ord(txt[i]) - KLUCZ + 26)
        if ord(txt[i]) - KLUCZ < 65 and ord(txt[i]) > 64:
            odszyfrowany += chr(ord(txt[i]) - KLUCZ + 26)
        else:
            odszyfrowany += chr(ord(txt[i]) - KLUCZ)
    return odszyfrowany

def main(args):
    tekst = input("Podaj ciąg do zaszyfrowania:\n")
    sz = szyfruj(tekst)
    print("Ciąg zaszyfrowany:\n", sz)
    print("Ciąg odszyfrowany:\n", deszyfruj(sz))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))