import random

def losuj_kule(biale, czarne, rng):
    r = rng.randrange(biale + czarne)
    return "B" if r < biale else "C"


def symuluj(biale, czarne, niezmiennik, opis_niezmiennika, seed=42):
    if biale < 0 or czarne < 0:
        raise ValueError("Liczby kul muszą być nieujemne.")
    if czarne % 2 == 0:
        raise ValueError("Liczba czarnych kul musi być nieparzysta.")

    rng = random.Random(seed)
    start_biale, start_czarne = biale, czarne

    sprawdzen = 0
    spelnionych = 0

    def sprawdz():
        nonlocal sprawdzen, spelnionych
        sprawdzen += 1
        if niezmiennik(biale, czarne, start_biale, start_czarne):
            spelnionych += 1

    while biale + czarne > 1:
        sprawdz()

        k1 = losuj_kule(biale, czarne, rng)
        if k1 == "B":
            biale -= 1
        else:
            czarne -= 1

        k2 = losuj_kule(biale, czarne, rng)
        if k2 == "B":
            biale -= 1
        else:
            czarne -= 1

        if k1 != k2:
            czarne += 1

        sprawdz()

    ostatnia = "czarna" if czarne == 1 else "biała"
    return ostatnia, opis_niezmiennika, sprawdzen, spelnionych


def testuj_niezmienniki(biale, czarne):
    kandydaci = [
        ("czarne % 2 == 1",
         lambda w, c, w0, c0: c % 2 == 1),

        ("czarne % 2 == start_czarne % 2",
         lambda w, c, w0, c0: c % 2 == c0 % 2),

        ("czarne > 0",
         lambda w, c, w0, c0: c > 0),

        ("biale % 2 == 0  (przykład błędnego niezmiennika)",
         lambda w, c, w0, c0: w % 2 == 0),
    ]

    print("\nEksperyment (te same dane, różne kandydaty na niezmiennik):")
    for opis, f in kandydaci:
        _, _, spr, ok = symuluj(biale, czarne, f, opis, seed=123)
        print(f"- {opis:45s}  spełniony: {ok}/{spr}")


def main():
    biale = int(input("Podaj liczbę kul białych: ").strip())
    czarne = int(input("Podaj liczbę kul czarnych (nieparzysta): ").strip())

    kandydaci = [
        ("czarne % 2 == 1",
         lambda w, c, w0, c0: c % 2 == 1),

        ("czarne % 2 == start_czarne % 2",
         lambda w, c, w0, c0: c % 2 == c0 % 2),

        ("czarne > 0",
         lambda w, c, w0, c0: c > 0),

        ("biale % 2 == 0  (przykład błędnego niezmiennika)",
         lambda w, c, w0, c0: w % 2 == 0),
    ]

    print("\nWybierz niezmiennik do sprawdzania:")
    for i, (opis, _) in enumerate(kandydaci, start=1):
        print(f"{i}) {opis}")

    wybor = int(input("Numer (1-4): ").strip())
    opis, f = kandydaci[wybor - 1]

    wynik, opis_n, sprawdzen, spelnionych = symuluj(biale, czarne, f, opis)

    print("\nWynik algorytmu:", wynik)
    print("Niezmiennik:", opis_n)
    print("Sprawdzeń niezmiennika:", sprawdzen)
    print("Spełniony razy:", spelnionych)

    testuj_niezmienniki(biale, czarne)

    print("\nWniosek końcowy:")
    print("- Najlepszy niezmiennik: parzystość liczby czarnych kul się nie zmienia (czarne % 2 stałe).")
    print("- Skoro na wejściu czarnych jest nieparzyście, to na końcu musi zostać czarna kula.")


if __name__ == "__main__":
    main()