import random
from collections import Counter

# a. Zapisz 20 losowych liczb do pliku
random_numbers = [random.randint(1, 10) for _ in range(20)]
with open('losowe_w_linii.txt', 'w') as file:
    file.write(' '.join(map(str, random_numbers)) + '\n')

# b. Znajdź liczby, które występują najczęściej
number_counts = Counter(random_numbers)
max_count = max(number_counts.values())

most_common_numbers = [num for num, count in number_counts.items() if count == max_count]

print("Najczęściej występujące liczby:", most_common_numbers)   