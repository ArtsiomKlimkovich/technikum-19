def binary_search(arr, n):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < n:
            left = mid + 1
        elif arr[mid] > n:
            right = mid - 1
        else:
            return True
    return False


with open('ciagi2.txt', 'r') as file:
    lines = file.readlines()

    number_of_sequences = int(lines[0].strip())
    results = []

    index = 1
    for i in range(number_of_sequences):
        count_of_numbers = int(lines[index].strip())
        sequence = list(map(int, lines[index + 1].strip().split()))

        if binary_search(sequence, 10):
            results.append(sequence)

        index += 2

    for seq in results:
        print(' '.join(map(str, seq)))