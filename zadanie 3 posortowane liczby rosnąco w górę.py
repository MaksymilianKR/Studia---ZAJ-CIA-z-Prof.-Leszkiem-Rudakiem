#zadanie 3A
def bubble_sort(a):
    a = a[:]                 # robie kopię żeby nie zmieniać listy wejściowej
    n = len(a)

    for i in range(n):       
        for j in range(1, n):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]  

    return a

# .split() dzieli ten tekst po spacjach -> ["10", "3", "-5", "7"] (to nadal są napisy)
# map(int, ...) zamienia każdy napis na liczbę całkowitą -> 10, 3, -5, 7

numbers = list(map(int, input("Podaj liczby oddzielone spacjami: ").split()))

# bubble_sort(numbers) zwraca posortowaną listę
print("Posortowane:", bubble_sort(numbers))






#zadanie 3B
# import random


# def sortowanie_babelkowe(lista):
#     lista = lista[:]
#     porownania = zamiany = 0

#     for i in range(len(lista) - 1):
#         byla_zamiana = False

#         for j in range(len(lista) - 1 - i):
#             porownania += 1
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#                 zamiany += 1
#                 byla_zamiana = True

#         if not byla_zamiana:
#             break

#     return lista, porownania, zamiany


# liczby = list(map(int, input("Podaj liczby oddzielone spacjami: ").split()))
# posortowane, porownania, zamiany = sortowanie_babelkowe(liczby)

# print("Posortowane:", posortowane)
# print("Porównania:", porownania)
# print("Zamiany:", zamiany)


# print("\nEksperyment (najwięcej porównań):")
# for n in (5, 10, 20):
#     przypadki = {
#         "rosnąco": list(range(n)),
#         "malejąco": list(range(n - 1, -1, -1)),
#         "losowo": random.sample(range(1000), n),
#     }

#     wyniki = {nazwa: sortowanie_babelkowe(tablica)[1] for nazwa, tablica in przypadki.items()}
#     najgorszy = max(wyniki, key=wyniki.get)

#     print(f"n={n} -> {wyniki} -> najgorzej: {najgorszy}")