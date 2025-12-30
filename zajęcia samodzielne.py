import random
# zad 1. Struktura danych SL + zliczanie kosztu (wersja B)
class SL_B:
    def __init__(self, start):
        self.a = start[:]
        self.koszt = 0

    def access(self, x):
        for v in self.a:
            self.koszt += 1
            if v == x:
                return True
        return False

    def insert(self, x):
        if not self.access(x):
            self.a.insert(0, x)

    def delete(self, x):
        for i, v in enumerate(self.a):
            self.koszt += 1
            if v == x:
                self.a.pop(i)
                return True
        return False


# zad 1. Struktura danych SL + zliczanie kosztu (wersja MF) 
class SL_MF:
    def __init__(self, start):
        self.a = start[:]
        self.koszt = 0

    def access(self, x):
        for i, v in enumerate(self.a):
            self.koszt += 1
            if v == x:
                self.koszt += i
                self.a.pop(i)
                self.a.insert(0, x)
                return True
        return False

    def insert(self, x):
        if not self.access(x):
            self.a.insert(0, x)

    def delete(self, x):
        for i, v in enumerate(self.a):
            self.koszt += 1
            if v == x:
                self.a.pop(i)
                return True
        return False


# zad 2. Generowanie losowego ciągu operacji wg założeń 
def losuj_operacje():
    return random.choices(["access", "insert", "delete"], weights=[100, 1, 1], k=1)[0]


def losuj_access(uniwersum, hot):
    wagi = [10 if x == hot else 1 for x in uniwersum]
    return random.choices(uniwersum, weights=wagi, k=1)[0]


def losuj_insert(uniwersum, obecne):
    kandydaci = [x for x in uniwersum if x not in obecne]
    return random.choice(kandydaci) if kandydaci else random.choice(uniwersum)


def losuj_delete(obecne, hot):
    kandydaci = [x for x in obecne if x != hot]
    return random.choice(kandydaci) if kandydaci else None


def generuj_ciag(uniwersum, hot, dlugosc, start):
    obecne = set(start)
    ciag = []

    for _ in range(dlugosc):
        op = losuj_operacje()

        if op == "access":
            x = losuj_access(uniwersum, hot)
            ciag.append((op, x))

        elif op == "insert":
            x = losuj_insert(uniwersum, obecne)
            ciag.append((op, x))
            obecne.add(x)

        else:
            x = losuj_delete(obecne, hot)
            if x is None:
                x = losuj_access(uniwersum, hot)
                ciag.append(("access", x))
            else:
                ciag.append((op, x))
                obecne.remove(x)

    return ciag


#zad 3. Badanie średniego kosztu dla B i MF + przykład ciągu 
def wykonaj(struktura, ciag):
    for op, x in ciag:
        if op == "access":
            struktura.access(x)
        elif op == "insert":
            struktura.insert(x)
        else:
            struktura.delete(x)
    return struktura.koszt


def eksperyment(proby=30, dlugosc=500, seed=42):
    random.seed(seed)

    uniwersum = list(range(1, 51))
    hot = 1
    start = list(range(1, 21))

    przyklad = generuj_ciag(uniwersum, hot, 20, start)

    koszty_b = []
    koszty_mf = []

    for _ in range(proby):
        ciag = generuj_ciag(uniwersum, hot, dlugosc, start)
        koszty_b.append(wykonaj(SL_B(start), ciag))
        koszty_mf.append(wykonaj(SL_MF(start), ciag))

    print("Przykładowy ciąg (20 operacji):")
    print(przyklad)

    print("\nŚredni koszt:")
    print("B :", sum(koszty_b) / len(koszty_b))
    print("MF:", sum(koszty_mf) / len(koszty_mf))


if __name__ == "__main__":
    eksperyment()