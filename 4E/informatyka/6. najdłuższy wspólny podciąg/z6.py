def lcs_len(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i-1][j-1] + 1 if s1[i-1] == s2[j-1] else max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

max_len = -1
best_pairs = []

with open("pary.txt") as f:
    for line in f:
        a, b = line.strip().split()
        length = lcs_len(a, b)
        if length > max_len:
            max_len = length
            best_pairs = [(a, b)]
        elif length == max_len:
            best_pairs.append((a, b))

for x, y in best_pairs:
    print(x, y)