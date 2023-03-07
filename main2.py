import math
import numpy as np

# stałe
lambda_ = 30  # długość fali elektromagnetycznej w cm
plate_size = 50  # wymiary płyty w cm
min_dist = lambda_ / 4  # minimalna odległość między trójkątami w cm

def attenuation(length, n):
    """
    Funkcja obliczająca tłumienie elektromagnetyczne dla danego trójkąta.
    """
    return 20 * np.log10(lambda_ / (2 * length)) - 20 * np.log10(math.sqrt(n))

def triangle_area(length):
    """
    Funkcja obliczająca pole powierzchni trójkąta o boku o zadanej długości.
    """
    return math.sqrt(3) / 4 * length ** 2

max_triangles = 0  # maksymalna ilość trójkątów
best_config = None  # najlepsza konfiguracja trójkątów

# iterujemy po różnych długościach boków trójkątów
for length in range(5, 26):
    # obliczamy liczbę trójkątów, które zmieszczą się na płycie
    num_triangles = int((plate_size / length) ** 2)

    # iterujemy po różnych położeniach pierwszego trójkąta
    for i in range(num_triangles):
        for j in range(num_triangles):
            x = i * length + length / 2
            y = j * length + length / 2

            # sprawdzamy, czy wszystkie trójkąty mieszczą się na płycie
            if x > plate_size or y > plate_size:
                continue

            # sprawdzamy, czy trójkąty są oddalone od siebie o co najmniej λ/4
            valid_config = True
            for k in range(num_triangles):
                for l in range(num_triangles):
                    if k == i and l == j:
                        continue
                    dist = math.sqrt((k * length + length / 2 - x) ** 2 + (l * length + length / 2 - y) ** 2)
                    if dist < min_dist:
                        valid_config = False
                        break
                if not valid_config:
                    break

            # jeśli konfiguracja jest poprawna, obliczamy tłumienie i pole powierzchni
            if valid_config:
                area = num_triangles * triangle_area(length)
                att = attenuation(length, num_triangles - 1)

                # jeśli tłumienie mieści się w wymaganym przedziale i pole powierzchni jest większe niż dotychczasowe, zapisujemy konfigurację
                if 7.5 <= att <= 8.5 and area > max_triangles:
                    max_triangles = area
                    best_config = [(x + length / 2, y + length / 2) for x in range(0, length * num_triangles, length) for y in range(0, length * num_triangles, length)]

if best_config is not None:
    print(f"Liczba trójkątów: {len(best_config)}, Konfiguracja najlepszej konfiguracji: {best_config}")
    print(f"Powierzchnia trójkątów: {max_triangles} cm^2")
else:
    print("Nie znaleziono żadnej konfiguracji spełniającej kryteria.")

