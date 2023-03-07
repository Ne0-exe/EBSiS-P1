#indeks 259004
#f = 0,04 / 100 * 25 = 1 GHz
#figura - trójkąt równoboczny


import numpy
import math

f = 1 # GHz = 1000000000 Hz
c = 300000000 # m/s
lamb = c/(f*1000000000) # 0,3 m = 30 cm
min_odleglosc = lamb/10 # 0,075 m = 7,5 cm - "odległość nie powinna przekracać lambda/10"
max_wymiar_liniowy = lamb/2 # 0,15 m = 15 cm - " całkowity wymiar rzędu otworów nie przekracza połowy długości fali"
srednia = []

def tlumienie(bok, n):
    s = 20*numpy.log10(lamb/(2*bok)) - 20*numpy.log10(math.sqrt(n))
    return s

for d in numpy.arange(min_odleglosc*100, 30, 0.1):
    for l in numpy.arange(0.1, 15, 0.1):
        pole = (pow(l, 2)*math.sqrt(3))/4
        a = 50 # 50 cm boku przesłony
        suma = 0 # suma bok + odległość
        suma_rzedu = 0
        n = 0 # liczba otworów
        while (suma < 50) and (suma_rzedu < 15):
            opty = n * (l ** 2 * math.sqrt(3)) / 4
            if ((suma+l) < 50) and (suma_rzedu < lamb*100):
                suma += l
                suma_rzedu += l
                n += 1
                if (suma + d) < 50:
                    suma += d
                else:
                    suma += 50
                    if n == 1:
                        s = 20*numpy.log10(lamb/(2*(l/100)))
                    else:
                        s = 20*numpy.log10(lamb/(2*(l/100))) - 20*numpy.log10(math.sqrt(n-1))

                    if s >= 8:
                        if (50 - ((l**2*math.sqrt(3))/4) * n) < (((l**2*math.sqrt(3))/4) + d):
                            print(f'Optymalizacja dla rzędu: {opty}\tDługość boku: {round(l, 2)} cm\tPole powierzchni: {pole}\tOdległość: {round(d, 2)} cm\tLiczba wszystkich otworów: {n * n}\t '
                                f'Tłumienie {round(s, 2)} [dB]\t Suma rzędu: {round(suma_rzedu, 2)} cm')
                            srednia.append(l)

                        else:
                            print(f'Optymalizacja dla rzędu: {opty}\tDługość boku: {round(l, 2)} cm\tPole powierzchni: {pole}\tOdległość: {round(d, 2)} cm\tLiczba wszystkich otworów: {(n +1)*n}\t '
                                f'Tłumienie {round(s, 2)} [dB]\t Suma rzędu: {round(suma_rzedu, 2)} cm')
                            srednia.append(l)

            else:
                suma += 50
                s = tlumienie(l / 100, n-1)
                if s >= 8:
                    if (50 - ((l ** 2 * math.sqrt(3)) / 4) * n) < (((l ** 2 * math.sqrt(3)) / 4) + d):
                        print(f'Optymalizacja dla rzędu: {opty}\tDługość boku: {round(l, 2)} cm\tPole powierzchni: {pole}\tOdległość: {round(d, 2)} cm\tLiczba wszystkich otworów: {n * n}\t '
                            f'Tłumienie {round(s, 2)} [dB]\t Suma rzędu: {round(suma_rzedu, 2)} cm')
                        srednia.append(l)

                    else:
                        print(f'Optymalizacja dla rzędu: {opty}\tDługość boku: {round(l, 2)} cm\tPole powierzchni: {pole}\tOdległość: {round(d, 2)} cm\tLiczba wszystkich otworów: {(n + 1) * n}\t '
                            f'Tłumienie {round(s, 2)} [dB]\t Suma rzędu: {round(suma_rzedu, 2)} cm')
                        srednia.append(l)

sredni_bok = 0
for i in srednia:
    sredni_bok += i

print(f'srednia_bok: {round(sredni_bok/len(srednia), 2)} cm')






