import numpy as np


# Třída pro celí program
class Jednotky_SI:
    def __init__(self, Znacka, Dalsi=None, Metr=0, Kilogram=0, Sekunda=0, Amper=0, Kelvin=0, Mol=0, Kandela=0,):
        self.Znacka = Znacka
        self.Metr = Metr
        self.Kilogram = Kilogram
        self.Sekunda = Sekunda
        self.Amper = Amper
        self.Kelvin = Kelvin
        self.Mol = Mol
        self.Kandela = Kandela
        self.Dalsi = Dalsi

    def __str__(self):
        return str(self.Znacka)

    def append(self, other):
        self.append(other)

    def __len__(self):
        return self.len()

    def __getitem__(self, item):
        self.__getitem__(item)

Veliciny = []

# Zadávání vstupních veličin
while True:
    A = input("Znacka")
    if A == "":
        break
    B = str(input("Jadnotky"))
    Veliciny.append(Jednotky_SI(A))
    Veliciny[len(Veliciny)-1].Dalsi = B

# Mechanické převedení jednotek na jednotky základní a jejich dosazení do třídy
# Vezme postupně každou velicinu a pro každou její jednotku jí přidá a příslušné rozměry
for j in range(0, len(Veliciny)):
    Veliciny[j].Dalsi = Veliciny[j].Dalsi.split('*')
    if Veliciny[j].Dalsi == str(Veliciny[j].Dalsi):
        Veliciny[j].Dalsi = [Veliciny[j].Dalsi]
    for i in Veliciny[j].Dalsi:
        if i.find("-") != -1:
            i = i.split("-")
            for k in range(int(i[1])+1):
                if i == "M" or "m" or "Mert" or "mert":
                   Veliciny[j].Metr -= 1
                elif i == "Kg" or "kg" or "Kilogram" or "kilogram":
                  Veliciny[j].Kilogram -= 1
                elif i == "Sekunda" or "sekunda" or "s":
                  Veliciny[j].Sekunda -= 1
                elif i == "A" or "a" or "Amper" or "amper":
                  Veliciny[j].Amper -= 1
                elif i == "K" or "k" or "Kelvin" or "kelvin" or "°C" or "°c":
                    Veliciny[j].Kelvin -= 1
                elif i == "mol" or "Mol":
                    Veliciny[j].Mol -= 1
                elif i == "Kandela" or "kandela" or "cd" or "Cd":
                    Veliciny[j].Kandela -= 1
                elif i == "Hz" or "hz" or "hertz" or "Hertz":
                    Veliciny[j].Sekunda += 1
                elif i == "newton" or "Newton" or "N" or "n":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Metr -= 1
                    Veliciny[j].Sekunda += 2
                elif i == "P" or "p" or "Pa" or "pa" or "pascal" or "Pascal":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Metr += 1
                elif i == "J" or "j" or "joule" or "Joule":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Metr -= 2
                elif i == "Watt" or "watt" or "W" or "w":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 3
                    Veliciny[j].Metr -= 2
                elif i == "Coulomb" or "coulomb" or "C" or "c":
                    Veliciny[j].Amper -= 1
                    Veliciny[j].Sekunda += 1
                elif i == "Volt" or "volt" or "V" or "v":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 3
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 1
                elif i == "farad" or "Farad" or "F" or "f":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 4
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 2
                elif i == "ohm" or "Ohm" or "Ω":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 3
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 2
                elif i == "siemens" or "Siemens" or "S":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 3
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 2
                elif i == "Weber" or "weber" or "Wb" or "wb":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 1
                elif i == "tesla" or "Tesla" or "T" or "t":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Amper += 1
                elif i == "henry" or "Henry" or "H" or "h":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 2
        else:
            if i.find("+") != -1:
                i = i.split('+')
            if len(i) == 1:
                i = [i, 1]
            for k in range(int(i[1])+1):
                if i == "M" or "m" or "Mert" or "mert":
                    Veliciny[j].Metr += 1
                elif i == "Kg" or "kg" or "Kilogram" or "kilogram":
                    Veliciny[j].Kilogram += 1
                elif i == "Sekunda" or "sekunda" or "s":
                    Veliciny[j].Sekunda += 1
                elif i == "A" or "a" or "Amper" or "amper":
                    Veliciny[j].Amper += 1
                elif i == "K" or "k" or "Kelvin" or "kelvin" or "°C" or "°c":
                    Veliciny[j].Kelvin += 1
                elif i == "mol" or "Mol":
                    Veliciny[j].Mol += 1
                elif i == "Kandela" or "kandela" or "cd" or "Cd":
                    Veliciny[j].Kandela += 1
                elif i == "Hz" or "hz" or "hertz" or "Hertz":
                    Veliciny[j].Sekunda -= 1
                elif i == "newton" or "Newton" or "N" or "n":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Metr += 1
                    Veliciny[j].Sekunda -= 2
                elif i == "P" or "p" or "Pa" or "pa" or "pascal" or "Pascal":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Metr -= 1
                elif i == "J" or "j" or "joule" or "Joule":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Metr += 2
                elif i == "Watt" or "watt" or "W" or "w":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 3
                    Veliciny[j].Metr += 2
                elif i == "Coulomb" or "coulomb" or "C" or "c":
                    Veliciny[j].Amper += 1
                    Veliciny[j].Sekunda -= 1
                elif i == "Volt" or "volt" or "V" or "v":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 3
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 1
                elif i == "farad" or "Farad" or "F" or "f":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 4
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 2
                elif i == "ohm" or "Ohm" or "Ω":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 3
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 2
                elif i == "siemens" or "Siemens" or "S":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 3
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 2
                elif i == "Weber" or "weber" or "Wb" or "wb":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 1
                elif i == "tesla" or "Tesla" or "T" or "t":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Amper -= 1
                elif i == "henry" or "Henry" or "H" or "h":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 2


# Výpočetní část
Gmetr = 0
Gkilogram = 0
Gsekunda = 0
Gamper = 0
Gkelvin = 0
Gmol = 0
Gkandela = 0
Gglobal = 0
for i in Veliciny:
    if i.Metr != 0:
        Gmetr =+1
    if i.Kilogram != 0:
        Gkilogram =+ 1
    if i.Sekunda != 0:
        Gsekunda =+ 1
    if i.Amper != 0:
        Gamper =+ 1
    if i.Kelvin != 0:
        Gkelvin =+ 1
    if i.Mol != 0:
        Gmol =+ 1
    if i.Kandela != 0:
        Gkandela =+ 1
if Gmetr != 0:
    Gglobal =+ 1
if Gkilogram != 0:
    Gglobal =+ 1
if Gsekunda != 0:
    Gglobal =+ 1
if Gamper != 0:
    Gglobal =+ 1
if Gkelvin != 0:
    Gglobal =+ 1
if Gmol != 0:
    Gglobal =+ 1
if Gkandela != 0:
    Gglobal =+ 1
import numpy.linalg as lin
metr = []
kilogram = []
sekunda = []
amper = []
kelvin = []
mol = []
kandela = []
MatrixA = []
if (len(Veliciny)-1) > Gglobal:
    print("Nelze vypočítat")
elif (len(Veliciny)-1) == Gglobal:
    metr = []
    kilogram = []
    sekunda = []
    amper = []
    kelvin = []
    mol = []
    kandela = []
    MatrixA = []
    MatrixB = []
    for i in range(1, len(Veliciny)):
        metr.append(Veliciny[i].Metr)
        kilogram.append(Veliciny[i].Kilogram)
        sekunda.append(Veliciny[i].Sekunda)
        amper.append(Veliciny[i].Amper)
        kelvin.append(Veliciny[i].Kelvin)
        mol.append(Veliciny[i].Mol)
        kandela.append(Veliciny[i].Kandela)
    if Gmetr != 0:
        MatrixA.append(metr)
    if Gkilogram != 0:
        MatrixA.append(kilogram)
    if Gsekunda != 0:
        MatrixA.append(sekunda)
    if Gamper != 0:
        MatrixA.append(amper)
    if Gkelvin != 0:
        MatrixA.append(kelvin)
    if Gmol != 0:
        MatrixA.append(mol)
    if Gkandela != 0:
        MatrixA.append(kandela)

    if Gmetr != 0:
        MatrixB.append(Veliciny[0].Metr)
    if Gkilogram != 0:
        MatrixB.append(Veliciny[0].Kilogram)
    if Gsekunda != 0:
        MatrixB.append(Veliciny[0].Sekunda)
    if Gamper != 0:
        MatrixB.append(Veliciny[0].Amper)
    if Gkelvin != 0:
        MatrixB.append(Veliciny[0].Kelvin)
    if Gmol != 0:
        MatrixB.append(Veliciny[0].Mol)
    if Gkandela != 0:
        MatrixB.append(Veliciny[0].Kandela)

    Vysledky = lin.solve(MatrixA, MatrixB)

    print(Vysledky)
