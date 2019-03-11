from fractions import Fraction
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


def odcitani_matic(Matice, n, k):  # n - kolikátý sloupec    k - kolikátá řáda k odečtení
    Podil = Matice[k][n]/Matice[n][n]
    for i in range(k, len(Matice)+1):
        Matice[k][i] -= Podil*Matice[n][i]

def razeni(Matice, n):
     for i in range (n, len(Matice)):
         if Matice[i][n] != 0:
             if i == n:
                 break
             else:
                 D = Matice[n]
                 Matice[n] = Matice[i]
                 Matice[i] = D
                 break


def reseni_matic(Matice):
    for i in range(0,len(Matice)-1):
        razeni(Matice, i)
        for k in range(i+1, len(Matice)):
            odcitani_matic(Matice, i, k)

def ziskat_reseni(Matice):
    Vysledky = []
    for i in range(len(Matice)):
        for k in range(0, i):
            odcitani_matic(Matice, i, k)
    for i in range(0,len(Matice)):
        Vysledky.append(Matice[i][len(Matice)]/Matice[i][i])
    Vysledky.reverse()
    return Vysledky

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
            for k in range(int(i[1])):
                if i[0] == "m":
                    Veliciny[j].Metr -= 1
                elif i[0] == "kg":
                    Veliciny[j].Kilogram -= 1
                elif i[0] == "s":
                    Veliciny[j].Sekunda -= 1
                elif i[0] == "A":
                    Veliciny[j].Amper -= 1
                elif i[0] == "K":
                    Veliciny[j].Kelvin -= 1
                elif i[0] == "mol":
                    Veliciny[j].Mol -= 1
                elif i[0] == "cd":
                    Veliciny[j].Kandela -= 1
                elif i[0] == "Hz":
                    Veliciny[j].Sekunda += 1
                elif i[0] == "N":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Metr -= 1
                    Veliciny[j].Sekunda += 2
                elif i[0] == "Pa":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Metr += 1
                elif i[0] == "J":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Metr -= 2
                elif i[0] == "W":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 3
                    Veliciny[j].Metr -= 2
                elif i[0] == "C":
                    Veliciny[j].Amper -= 1
                    Veliciny[j].Sekunda += 1
                elif i[0] == "V":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 3
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 1
                elif i[0] == "F":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 4
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 2
                elif i[0] == "ohm" or i[0] == "Ω":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 3
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 2
                elif i[0] == "S":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 3
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 2
                elif i[0] == "Wb":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 1
                elif i[0] == "T":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Amper += 1
                elif i[0] == "H":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 2
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 2
                elif i[0] != "rad" or i[0] != "sr":
                    print("neznámé veličiny")
        else:
            if i.find("+") != -1:
                i = i.split('+')
            else:
                i = [i, 1]
            for k in range(int(i[1])):
                if i[0] == "m":
                    Veliciny[j].Metr += 1
                elif i[0] == "kg":
                    Veliciny[j].Kilogram += 1
                elif i[0] == "s":
                    Veliciny[j].Sekunda += 1
                elif i[0] == "A":
                    Veliciny[j].Amper += 1
                elif i[0] == "K":
                    Veliciny[j].Kelvin += 1
                elif i[0] == "mol":
                    Veliciny[j].Mol += 1
                elif i[0] == "cd":
                    Veliciny[j].Kandela += 1
                elif i[0] == "Hz":
                    Veliciny[j].Sekunda -= 1
                elif i[0] == "N":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Metr += 1
                    Veliciny[j].Sekunda -= 2
                elif i[0] == "Pa":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Metr -= 1
                elif i[0] == "J":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Metr += 2
                elif i[0] == "W":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 3
                    Veliciny[j].Metr += 2
                elif i[0] == "C":
                    Veliciny[j].Amper += 1
                    Veliciny[j].Sekunda -= 1
                elif i[0] == "V":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 3
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 1
                elif i[0] == "F":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 4
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 2
                elif i[0] == "ohm" or i[0] == "Ω":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 3
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 2
                elif i[0] == "S":
                    Veliciny[j].Kilogram -= 1
                    Veliciny[j].Sekunda += 3
                    Veliciny[j].Metr -= 2
                    Veliciny[j].Amper += 2
                elif i[0] == "Wb":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 1
                elif i[0] == "T":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Amper -= 1
                elif i[0] == "H":
                    Veliciny[j].Kilogram += 1
                    Veliciny[j].Sekunda -= 2
                    Veliciny[j].Metr += 2
                    Veliciny[j].Amper -= 2
                elif i[0] != "rad" or i[0] != "sr":
                    print("neznámé veličiny")

while True:
# Výpočetní část
    Gmetr = 0
    Gkilogram = 0
    Gsekunda = 0
    Gamper = 0
    Gkelvin = 0
    Gmol = 0
    Gkandela = 0
    Gglobal = 0
    validator = 0
    for i in Veliciny:
        if i.Metr != 0:
            Gmetr +=1
        if i.Kilogram != 0:
            Gkilogram += 1
        if i.Sekunda != 0:
            Gsekunda += 1
        if i.Amper != 0:
            Gamper += 1
        if i.Kelvin != 0:
            Gkelvin += 1
        if i.Mol != 0:
            Gmol += 1
        if i.Kandela != 0:
            Gkandela += 1
# kontrola vstup
    if Gmetr == 1:
        if Veliciny[0].Metr == 0:
            for i in range(0,len(Veliciny)):
                if Veliciny[i].Metr != 0:
                    Veliciny.pop(i)
                    validator = 1
                    break
        else:
            raise ValueError
    if Gkilogram == 1:
        if Veliciny[0].Kilogram == 0:
            for i in range(0,len(Veliciny)):
                if Veliciny[i].Kilogram != 0:
                    Veliciny.pop(i)
                    validator = 1
                    break
        else:
            raise ValueError
    if Gsekunda == 1:
        if Veliciny[0].Sekunda == 0:
            for i in range(0,len(Veliciny)):
                if Veliciny[i].Sekunda != 0:
                    Veliciny.pop(i)
                    validator = 1
                    break
        else:
            raise ValueError
    if Gamper == 1:
        if Veliciny[0].Amper == 0:
            for i in range(0,len(Veliciny)):
                if Veliciny[i].Amper != 0:
                    Veliciny.pop(i)
                    validator = 1
                    break
        else:
            raise ValueError
    if Gkelvin == 1:
        if Veliciny[0].Kelvin == 0:
            for i in range(0,len(Veliciny)):
                if Veliciny[i].Kelvin != 0:
                    Veliciny.pop(i)
                    validator = 1
                    break
        else:
            raise ValueError
    if Gmol == 1:
        if Veliciny[0].Mol == 0:
            for i in range(0,len(Veliciny)):
                if Veliciny[i].Mol != 0:
                    Veliciny.pop(i)
                    validator = 1
                    break
        else:
            raise ValueError
    if Gkandela == 1:
        if Veliciny[0].Kandela == 0:
            for i in range(0,len(Veliciny)):
                if Veliciny[i].Kandela != 0:
                    Veliciny.pop(i)
                    validator = 1
                    break
        else:
            raise ValueError
    if validator == 0:
        break

if Gmetr != 0:
    Gglobal += 1
if Gkilogram != 0:
    Gglobal += 1
if Gsekunda != 0:
    Gglobal += 1
if Gamper != 0:
    Gglobal += 1
if Gkelvin != 0:
    Gglobal += 1
if Gmol != 0:
    Gglobal += 1
if Gkandela != 0:
    Gglobal += 1

metr = []
kilogram = []
sekunda = []
amper = []
kelvin = []
mol = []
kandela = []
Matrix = []
if len(Veliciny)-1 != Gglobal:
    print("Nelze vypočítat")
else :
    metr = []
    kilogram = []
    sekunda = []
    amper = []
    kelvin = []
    mol = []
    kandela = []
    Matrix = []
    for i in range(0, len(Veliciny)):
        metr.append(Veliciny[i].Metr)
        kilogram.append(Veliciny[i].Kilogram)
        sekunda.append(Veliciny[i].Sekunda)
        amper.append(Veliciny[i].Amper)
        kelvin.append(Veliciny[i].Kelvin)
        mol.append(Veliciny[i].Mol)
        kandela.append(Veliciny[i].Kandela)
    if Gmetr != 0:
        metr.reverse()
        Matrix.append(metr)
    if Gkilogram != 0:
        kilogram.reverse()
        Matrix.append(kilogram)
    if Gsekunda != 0:
        sekunda.reverse()
        Matrix.append(sekunda)
    if Gamper != 0:
        amper.reverse()
        Matrix.append(amper)
    if Gkelvin != 0:
        kelvin.reverse()
        Matrix.append(kelvin)
    if Gmol != 0:
        mol.reverse()
        Matrix.append(mol)
    if Gkandela != 0:
        kandela.reverse()
        Matrix.append(kandela)
    reseni_matic(Matrix)
    Vysledky = ziskat_reseni(Matrix)
    Vystup = str(Veliciny[0].Znacka) + ' = '
    for i in range(1,len(Veliciny)):
        Vystup += str(Veliciny[i].Znacka)
        if "1" != str(Fraction.from_float(Vysledky[i-1]).limit_denominator(100)):
            Vystup += str(Fraction.from_float(Vysledky[i-1]).limit_denominator(100))
        if i != len(Veliciny)-1:
            Vystup += '*'
    print(Vystup)
