#indeks 259004
#f = 0,04 / 100 * 25 = 1 GHz
#figura - trójkąt równoboczny
import numpy
import math

f = 1 # GHz = 1000000000 Hz
c = 300000000 # m/s
lamb = c/(f*1000000000) # 0,3 m = 30 cm
min_odleglosc = lamb/4 # 0,075 m = 7,5 cm
max_wymiar_liniowy = lamb/2 # 0,15 m = 15 cm

def tlumienie(bok, n):
    s = 20*math.log10(lamb/(2*bok)) - 20*math.log10(math.sqrt(n))
    return s

for l in numpy.arange(0.1, 15, 0.1):
    a = 50 # 50 cm boku przesłony
    suma = 0 # suma bok + odległość
    n = 0 # liczba otworów
    while suma < 50:
        if (suma+l) < 50:
            suma += l
            n += 1
            if (suma + min_odleglosc*100) < 50:
                suma += min_odleglosc*100
            else:
                suma += 50
                print(l)
                s = tlumienie(l / 100, n)
                if (s > 8) and (s < 9):
                    print(f'Długość boku: {l} cm\tOdległość: {min_odleglosc * 100} cm\tLiczba wszystkich otworów: {n * n}\t '
                        f'Tłumienie {s} [dB]')
        else:
            suma += 50
            print(l)
            s = tlumienie(l / 100, n)
            if (s > 8.9) and (s < 9.1):
                print(
                    f'Długość boku: {l} cm\tOdległość: {min_odleglosc * 100} cm\tLiczba wszystkich otworów: {n * n}\t '
                    f'Tłumienie {s} [dB]')





