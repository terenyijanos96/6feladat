def keres(karakter, karakterek):
    i = 0
    kimenet = 0
    karakter = karakter.upper()
    while i < len(karakterek):
        if karakter == karakterek[i]:
            kimenet = i
            break
        i += 1

    return kimenet

def titkositas(karakterek, karakterek_2):
    szoveg = input("Kérek egy szöveget és én titkosítom azt!\n>> ")
    kimenet = ""

    i = 0
    while i < len(szoveg):
        karakter_index = keres(szoveg[i], karakterek)
        kimenet += karakterek_2[karakter_index]
        i += 1

    print(f"A {szoveg.upper()} szöveg titkosítva -> {kimenet}")
    return kimenet