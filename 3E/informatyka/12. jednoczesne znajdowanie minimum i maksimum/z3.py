import random
liczby = [random.randint(1, 1000) for _ in range(100)]

def minMaks(t):
    n = len(t)

    if t[0] < t[1]:
        min = t[0]
        max = t[1]
    else:
        min = t[1]
        max = t[0]

    comparisons = 1

    for i in range(2, n, 2):
        comparisons += 1
        if i + 1 < n:
            if t[i] < t[i + 1]:
                if t[i] < min:
                    min = t[i]
                if t[i + 1] > max:
                    max = t[i + 1]
            else:
                if t[i + 1] < min:
                    min = t[i + 1]
                if t[i] > max:
                    max = t[i]
        else:
            if t[i] < min:
                min = t[i]
            elif t[i] > max:
                max = t[i]

    return min, max, comparisons


min, max, comparisons = minMaks(liczby)

print(f"Minimum: {min}")
print(f"Maksimum: {max}")
print(f"Liczba porównań: {comparisons}")