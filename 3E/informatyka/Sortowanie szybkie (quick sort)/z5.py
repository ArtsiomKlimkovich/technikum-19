import random
import time
from memory_profiler import memory_usage


def sortowanie_szybkie_1(ciag, lewy, prawy):
    pivot = ciag[(lewy + prawy) // 2]
    i = lewy
    j = prawy
    while i <= j:
        while ciag[i] < pivot:
            i += 1
        while ciag[j] > pivot:
            j -= 1
        if i <= j:
            ciag[i], ciag[j] = ciag[j], ciag[i]
            i += 1
            j -= 1
    if lewy < j:
        sortowanie_szybkie_1(ciag, lewy, j)
    if i < prawy:
        sortowanie_szybkie_1(ciag, i, prawy)


def sortowanie_szybkie_2(ciag):
    n = len(ciag)
    if n < 2:
        return ciag
    pivot = ciag[n // 2]
    lewy = [x for x in ciag if x < pivot]
    srodek = [x for x in ciag if x == pivot]
    prawy = [x for x in ciag if x > pivot]
    return sortowanie_szybkie_2(lewy) + srodek + sortowanie_szybkie_2(prawy)


def compare_algorithms():
    liczby = [random.randint(1, 100000) for _ in range(10000)]

    start_time = time.time()
    mem_usage_1 = memory_usage((sortowanie_szybkie_1, (liczby.copy(), 0, len(liczby) - 1)))
    time_1 = time.time() - start_time

    start_time = time.time()
    mem_usage_2 = memory_usage((sortowanie_szybkie_2, (liczby.copy(),)))
    time_2 = time.time() - start_time

    print(f"Algorytm 1 - Czas: {time_1:.4f} s, Zużycie pamięci: {max(mem_usage_1)} MiB")
    print(f"Algorytm 2 - Czas: {time_2:.4f} s, Zużycie pamięci: {max(mem_usage_2)} MiB")


if __name__ == '__main__':
    compare_algorithms()