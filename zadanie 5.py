import random
def suma_poteg_cyfr(n, potega):
    s = 0
    for znak in str(n):
        s += int(znak) ** potega
    return s # do każdego z zadań które są poniżej



# ZADANIE 1:
# suma kwadratów cyfr, stop gdy n == 1 lub n == 4

def algorytm_kwadraty(n):
    if n <= 0:
        raise ValueError("n musi być > 0")

    ciag = [n]
    iteracje = 0

    while n != 1 and n != 4:
        n = suma_poteg_cyfr(n, 2)
        ciag.append(n)
        iteracje += 1  

    return ciag, iteracje

# ZADANIE 2:
# suma sześcianów cyfr, stop gdy n == 153 (n startowe podzielne przez 3)+ LICZNIK ITERACJI

def algorytm_szesciany(n):
    if n <= 0:
        raise ValueError("n musi być > 0")
    if n % 3 != 0:
        raise ValueError("dla tego algorytmu n musi być podzielne przez 3")

    ciag = [n]
    iteracje = 0

    while n != 153:
        n = suma_poteg_cyfr(n, 3)
        ciag.append(n)
        iteracje += 1  

    return ciag, iteracje


# ZADANIE 3:
# Eksperyment: ile iteracji wychodzi dla liczb o 1,2,3,4,5 cyfrach

def losuj_liczbe_o_cyfach(ile_cyfr):
    if ile_cyfr == 1:
        return random.randint(1, 9)
    return random.randint(10 ** (ile_cyfr - 1), 10 ** ile_cyfr - 1)


def losuj_podzielna_przez_3(ile_cyfr):
    x = losuj_liczbe_o_cyfach(ile_cyfr)
    x -= (x % 3)
    if x == 0:
        x = 3
    return x


def test_iteracji(algorytm, ile_cyfr, proby, wymaga_podzielnosci_przez_3=False):
    wyniki = []

    for _ in range(proby):
        if wymaga_podzielnosci_przez_3:
            n = losuj_podzielna_przez_3(ile_cyfr)
        else:
            n = losuj_liczbe_o_cyfach(ile_cyfr)

        _, it = algorytm(n)
        wyniki.append(it)

    minimum = min(wyniki)
    maksimum = max(wyniki)
    srednia = sum(wyniki) / len(wyniki)
    return minimum, maksimum, srednia


def main():
    print("=== ZADANIE 1/2: pojedyncze uruchomienie z podanym n ===")
    n = int(input("Podaj n (>0): "))
    wybor = input("Wybierz algorytm (1=kwadraty, 2=sześciany): ").strip()

    if wybor == "1":
        ciag, it = algorytm_kwadraty(n)
    elif wybor == "2":
        ciag, it = algorytm_szesciany(n)
    else:
        print("Błędny wybór.")
        return

    print("Ciąg:", " -> ".join(map(str, ciag)))
    print("Koniec:", ciag[-1])
    print("Iteracje:", it)

    print("\n=== ZADANIE 3: eksperyment (iteracje vs liczba cyfr) ===")
    proby = 10  
    cyfry_test = [1, 2, 3, 4, 5]

    print("\nAlgorytm 1 (kwadraty) - po", proby, "prób dla każdej liczby cyfr:")
    for k in cyfry_test:
        mn, mx, avg = test_iteracji(algorytm_kwadraty, k, proby)
        print(f"{k} cyfr -> min={mn}, max={mx}, średnia={avg:.2f}")

    print("\nAlgorytm 2 (sześciany do 153) - po", proby, "prób dla każdej liczby cyfr:")
    for k in cyfry_test:
        mn, mx, avg = test_iteracji(algorytm_szesciany, k, proby, wymaga_podzielnosci_przez_3=True)
        print(f"{k} cyfr -> min={mn}, max={mx}, średnia={avg:.2f}")


if __name__ == "__main__":
    main()