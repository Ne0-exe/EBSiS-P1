#indeks 259004
#f = 0,04 / 100 * 25 = 1 GHz
#figura - trójkąt równoboczny


import numpy
import math

f = 1 # GHz = 1000000000 Hz
c = 300000000 # m/s
lamb = c/(f*1000000000) # 0,3 m = 30 cm
min_odleglosc = lamb/4 # 0,075 m = 7,5 cm - "odległość nie powinna przekracać lambda/4"
max_wymiar_liniowy = lamb/2 # 0,15 m = 15 cm - " całkowity wymiar rzędu otworów nie przekracza połowy długości fali"

def tlumienie(bok, n):
    s = 20*numpy.log10(lamb/(2*bok)) - 20*numpy.log10(math.sqrt(n))
    return s

for d in numpy.arange(min_odleglosc*100, 30, 0.1):
    for l in numpy.arange(0.1, 15, 0.1):
        a = 50 # 50 cm boku przesłony
        suma = 0 # suma bok + odległość
        suma_rzedu = 0
        n = 0 # liczba otworów
        while (suma < 50) and (suma_rzedu < 15):
            if ((suma+l) < 50) and (suma_rzedu < 15):
                suma += l
                suma_rzedu += l
                n += 1
                if (suma + d) < 50:
                    suma += d
                else:
                    suma += 50
                    s = tlumienie(l / 100, n-1)
                    if (s >= 7.9) and (s < 8.1):
                        if (50 - ((l**2*math.sqrt(3))/4) * n) < (((l**2*math.sqrt(3))/4) + d):
                            print(f'Długość boku: {round(l, 2)} cm\tPole powierzchni: {(l**2*math.sqrt(3))/4}\tOdległość: {round(d, 2)} cm\tLiczba wszystkich otworów: {n * n}\t '
                                f'Tłumienie {round(s, 2)} [dB]\t Suma rzędu: {round(suma_rzedu, 2)} cm')
                        else:
                            print(f'Długość boku: {round(l, 2)} cm\tPole powierzchni: {(l ** 2 * math.sqrt(3)) / 4}\tOdległość: {round(d, 2)} cm\tLiczba wszystkich otworów: {(n +1)*n}\t '
                                f'Tłumienie {round(s, 2)} [dB]\t Suma rzędu: {round(suma_rzedu, 2)} cm')
            else:
                suma += 50
                s = tlumienie(l / 100, n-1)
                if (s >= 8) and (s < 9):
                    print(
                        f'Długość boku: {round(l, 2)} cm\tPole powierzchni: {(l**2*math.sqrt(3))/4}\tOdległość: {round(d, 2)} cm\tLiczba wszystkich otworów: {n * n}\t '
                        f'Tłumienie {round(s, 2)} [dB]\t Suma rzędu: {round(suma_rzedu, 2)} cm')





