from __future__ import annotations

def kaprekar_step_4(n: int) -> int:
    s = f"{n:04d}"
    big = int("".join(sorted(s, reverse=True)))
    small = int("".join(sorted(s)))
    return big - small

def kaprekar_sequence_4(n: int, max_steps: int = 50) -> list[int]:
    if not (0 <= n <= 9999):
        raise ValueError("n musi być w zakresie 0..9999 (cztery cyfry, dopuszczalne zera z przodu).")
    seq = [n]
    for _ in range(max_steps):
        if n == 6174 or n == 0:
            break
        n = kaprekar_step_4(n)
        seq.append(n)
    return seq

def format_seq(seq: list[int]) -> str:
    return " -> ".join(f"{x:04d}" for x in seq)

def main() -> None:
    print("Algorytm Kaprekara (4 cyfry)")
    try:
        n = int(input("Podaj liczbę 0..9999 (może mieć zera z przodu): ").strip())
        seq = kaprekar_sequence_4(n)
        print("Ciąg:", format_seq(seq))
        print("Wynik:", f"{seq[-1]:04d}")
    except ValueError as e:
        print("Błąd danych:", e)

if __name__ == "__main__":
    main()


## Opis algorytmu
Dla liczby czterocyfrowej (może mieć zera z przodu):
1. Z jej cyfr układamy największą możliwą liczbę czterocyfrową `n1`.
2. Z tych samych cyfr układamy najmniejszą możliwą liczbę czterocyfrową `n2`.
3. Liczymy `n := n1 - n2`.
4. Powtarzamy, aż `n = 6174` albo `n = 0000`.

## Próby (liczba wejściowa → wygenerowany ciąg)
1) 0001 → 0001 -> 0999 -> 8991 -> 8082 -> 8532 -> 6174  
2) 0002 → 0002 -> 1998 -> 8082 -> 8532 -> 6174  
3) 0005 → 0005 -> 4995 -> 5355 -> 1998 -> 8082 -> 8532 -> 6174  
4) 0010 → 0010 -> 0999 -> 8991 -> 8082 -> 8532 -> 6174  
5) 1000 → 1000 -> 0999 -> 8991 -> 8082 -> 8532 -> 6174  
6) 2111 → 2111 -> 0999 -> 8991 -> 8082 -> 8532 -> 6174  
7) 3524 → 3524 -> 3087 -> 8352 -> 6174  
8) 1234 → 1234 -> 3087 -> 8352 -> 6174  
9) 9831 → 9831 -> 8442 -> 5994 -> 5355 -> 1998 -> 8082 -> 8532 -> 6174  
10) 9990 → 9990 -> 8991 -> 8082 -> 8532 -> 6174  
11) 7641 → 7641 -> 6174  
12) 1111 → 1111 -> 0000  

## Wnioski
- Dla większości liczb czterocyfrowych ciąg kończy się w **6174**.
- Gdy wszystkie cyfry są takie same (np. 1111, 2222, 0000), od razu (lub po 1 kroku) dostajemy **0000**.
- 6174 jest „punktem stałym” algorytmu: po wykonaniu kroku z 6174 znowu wyszłoby 6174, więc pętla się zatrzymuje.

## Dlaczego algorytm kończy działanie?
- W każdej iteracji wynik nadal jest liczbą z zakresu **0..9999**, więc istnieje tylko **10 000 możliwych stanów**.
- Algorytm jest deterministyczny (z tej samej liczby zawsze dostajemy tę samą następną).
- W skończonym zbiorze stanów deterministyczny proces musi po pewnym czasie wejść w powtórzenie (cykl).
- Dla tego algorytmu (4 cyfry w systemie dziesiętnym) jedyne „zatrzymujące” przypadki to **6174** oraz **0000**, co widać także w eksperymentach powyżej.