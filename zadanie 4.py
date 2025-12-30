# zadanie 4
def suma_poteg_cyfr(n, potega):
    # zamieniam liczbę na napis, każdą cyfre zamieniam sobie do potęgi
    return sum(int(cyfra) ** potega for cyfra in str(n))


def zrob_ciag(n, potega, stop):
    ciag = [n]
    while n != stop:
        n = suma_poteg_cyfr(n, potega)
        ciag.append(n)
    return ciag


n = int(input("Podaj n (>0): "))

wybor = input("Wybierz algorytm (1=kwadraty, 2=sześciany): ").strip()

if wybor == "1":
    ciag = [n]
    while n != 1 and n != 4:
        n = suma_poteg_cyfr(n, 2)
        ciag.append(n)

elif wybor == "2":
    # algorytm 2: suma sześcianów cyfr, kończymy gdy dojdzie do 153 (zgodnie z zadaniem startowa liczba ma być podzielna przez 3)
    if n % 3 != 0:
        print("Błąd: dla algorytmu 2 liczba musi być podzielna przez 3.")
        quit()
    ciag = zrob_ciag(n, 3, 153)

else:
    print("Błędny wybór.")
    quit()

print(" -> ".join(map(str, ciag)))
print("Koniec:", ciag[-1])




#zadanie 4b
# import random

# def suma_poteg_cyfr(n, potega):
#     return sum(int(cyfra) ** potega for cyfra in str(n))


# def algorytm_kwadraty(n):
#     iteracje = 0
#     ciag = [n]

#     while n != 1 and n != 4:
#         n = suma_poteg_cyfr(n, 2)
#         ciag.append(n)
#         iteracje += 1

#     return ciag, iteracje


# def algorytm_szesciany_153(n):
#     if n % 3 != 0:
#         raise ValueError("Dla algorytmu 2 liczba musi być podzielna przez 3.")

#     iteracje = 0
#     ciag = [n]

#     while n != 153:
#         n = suma_poteg_cyfr(n, 3)
#         ciag.append(n)
#         iteracje += 1

#     return ciag, iteracje


# def testuj_wg_wielkosci(algorytm, cyfry, proby=5):
#     wyniki = []
#     for _ in range(proby):
#         start = 10 ** (cyfry - 1)
#         stop = 10 ** cyfry - 1
#         n = random.randint(start, stop)
#         wyniki.append((n, algorytm(n)[1])) 
#     return wyniki


# n = int(input("Podaj n (>0): "))
# wybor = input("Wybierz algorytm (1=kwadraty, 2=sześciany): ").strip()

# if wybor == "1":
#     ciag, iteracje = algorytm_kwadraty(n)
#     print(" -> ".join(map(str, ciag)))
#     print("Koniec:", ciag[-1])
#     print("Iteracje:", iteracje)

#     print("\nTest iteracji wg liczby cyfr (po 5 prób):")
#     for cyfry in [1, 2, 3, 4, 5]:
#         wyniki = testuj_wg_wielkosci(algorytm_kwadraty, cyfry, 5)
#         print(f"{cyfry} cyfr:", wyniki)

# elif wybor == "2":
#     if n % 3 != 0:
#         print("Błąd: dla algorytmu 2 liczba musi być podzielna przez 3.")
#         quit()

#     ciag, iteracje = algorytm_szesciany_153(n)
#     print(" -> ".join(map(str, ciag)))
#     print("Koniec:", ciag[-1])
#     print("Iteracje:", iteracje)

#     print("\nTest iteracji wg liczby cyfr (po 5 prób):")
#     for cyfry in [1, 2, 3, 4, 5]:
#         # tu losuje tylko liczby podzielne przez 3
#         wyniki = []
#         for _ in range(5):
#             start = 10 ** (cyfry - 1)
#             stop = 10 ** cyfry - 1
#             x = random.randint(start, stop)
#             x = x - (x % 3)  # dociągam w dół do najbliższej podzielnej przez 3
#             if x == 0:
#                 x = 3
#             wyniki.append((x, algorytm_szesciany_153(x)[1]))
#         print(f"{cyfry} cyfr:", wyniki)

# else:
#     print("Błędny wybór.")