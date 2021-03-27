
import numpy as np
import pygame as pg

pg.init()

numar_incorect = 1
numar_jucatori = 0
nume_jucator = 0

while numar_incorect == 1:
    try:
          numar_jucatori = int(input("Introdu numarul de jucatori:"))
    except:
            print("Date gresite!")

    if numar_jucatori >=3 and numar_jucatori <= 6:
         numar_incorect = 0

    else:
          print("Numarul de jucatori este incorect, incearca din nou.")


list_nume_jucatori = []

for nume in range(numar_jucatori):
    nume_jucator = input("Introdu un nume:")
    list_nume_jucatori.append(nume_jucator)

print(list_nume_jucatori)

if numar_jucatori == 3:
    col1 = "111234567888765432111"
    i = 0
elif numar_jucatori == 4:
    col1 = "111123456788887654321111"
    i = 1
elif numar_jucatori == 5:
    i = 2
    col1 = "111112345678888876543211111"
else:
    i = 3
    col1 = "111111234567888888765432111111"


coloane = numar_jucatori * 3 + 1
randuri = 15 + i + (numar_jucatori * 2)              # 21   24   27   30

def matricea():
    matrix = np.zeros((randuri, coloane))
    return matrix


def prima_coloana(matrix, r, c, nr):
    poz = 0
    for r in range(randuri):
        for nr in col1[poz]:
            matrix[r][c] = int(nr)
            poz += 1

    return matrix


def intreaba_jucator(matrix, r, numarP):
    maini = ''
    poz = 0
    for nr in col1[r]:
        for numar in range(numar_jucatori):
            if numar + numarP < numar_jucatori:
                numar = numar + numarP
            else:
                numar = numar + numarP - numar_jucatori

            corect = 0
            while corect == 0:
                try:
                    intreaba_jucatori = input(f"Cate maini faci, {list_nume_jucatori[numar]}?")
                    if int(intreaba_jucatori) <= int(nr):
                        corect += 1
                        maini += intreaba_jucatori
                    elif int(intreaba_jucatori) > int(nr):
                        print("Numar de maini incorect!")
                except:
                    print("Tasta gresita!")

        for numar in range(numar_jucatori):
            if numar + numarP < numar_jucatori:
                numar = numar + numarP
            else:
                numar = numar + numarP - numar_jucatori
            for mana in maini[poz]:
                matrix[r][3*numar+1] = int(mana)
                poz += 1

    return matrix


def raspuns(matrix, r, numarP):
    #corect = 0
    poz = 0
    maini_reale = ''
    for nr in col1[r]:
        for raspuns_final in range(numar_jucatori):
            if raspuns_final + numarP < numar_jucatori:
                raspuns_final = raspuns_final + numarP
            else:
                raspuns_final = raspuns_final + numarP - numar_jucatori
            corect = 0
            while corect == 0:
                try:
                    rasp = input(f"Cate maini ai facut, {list_nume_jucatori[raspuns_final]}?")
                    if int(rasp) <= int(nr):
                        maini_reale += rasp
                        corect = 1
                    else:
                        print("Numar de maini facute este incorect!")
                except:
                    print("Tasta gresita!")

        for numar in range(numar_jucatori):
            if numar + numarP < numar_jucatori:
                numar = numar + numarP
            else:
                numar = numar + numarP - numar_jucatori
            for mana_reala in maini_reale[poz]:
                matrix[r][3*numar+2] = int(mana_reala)
                poz += 1

    return matrix


def rezultat(matrix, c, r):
    ars = 0
    perfect = 0
    for c in range(1, coloane, 3):
        if matrix[r][c] == matrix[r][c+1]:
           matrix[r][c+2] = matrix[r][c] + 5 + matrix[r-1][c+2]
           perfect += 1
        elif matrix[r][c+1] > matrix[r][c]:            # am facut prea multe
             matrix[r][c+2] = matrix[r][c] - matrix[r][c+1] + matrix[r-1][c+2]
             ars += 1
        elif matrix[r][c+1] < matrix[r][c]:                                          #am facut prea putine
             matrix[r][c+2] = matrix[r][c+1] - matrix[r][c] + matrix[r-1][c+2]
             ars += 1

    return matrix, ars, perfect              # apare 2 si ',.' dupa matrice dar sa vad cum rezolv


ars = numar_jucatori
perfect = numar_jucatori
r = 0           # are treaba cu randurile
maini_jucatori = ''
matricea_schimbata = matricea()
numarP = 0
GameOver = False

width = 1000
height = 750

while GameOver != True:
    if numarP < numar_jucatori:
        for r in range(randuri):
            while ars == numar_jucatori or perfect == numar_jucatori:
                matrix = matricea_schimbata
                prima_coloana(matrix, 0, 0, 0)
                intreaba_jucator(matrix, r, numarP)
                raspuns(matrix, r, numarP)
                print(rezultat(matrix, 0, r))
                matricea_schimbata, ars, perfect = rezultat(matrix, 0, r)
                print(r)
                if ars == numar_jucatori or perfect == numar_jucatori:
                    print("Introdu datele din nou.")

            if ars != numar_jucatori and perfect != numar_jucatori:
                r += 1
                ars = numar_jucatori
                perfect = numar_jucatori
                numarP += 1
                if numarP == numar_jucatori:
                    numarP = 0

    if r > randuri:
        GameOver = True

