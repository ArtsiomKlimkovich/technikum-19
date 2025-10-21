def minimal_nominals_greedy(amount, denominations):
    count = 0
    for coin in denominations:
        if amount == 0:
            break
        use = amount // coin
        count += use
        amount -= use * coin
    return count

with open("dane.txt", "r") as file:
    denominations = list(map(int, file.readline().strip().split()))
    denominations.sort(reverse=True)
    amounts = [int(file.readline().strip()) for _ in range(10)]

results = []
for amount in amounts:
    nom_count = minimal_nominals_greedy(amount, denominations)
    results.append((amount, nom_count))

min_nom_count = min((count for _, count in results))

for amount, count in results:
    if count == min_nom_count:
        print(amount)